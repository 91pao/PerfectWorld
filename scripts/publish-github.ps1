param(
  [Parameter(Mandatory = $true)]
  [string]$Owner,

  [Parameter(Mandatory = $false)]
  [string]$Repo = "perfectworld",

  [Parameter(Mandatory = $false)]
  [string]$Description = "PerfectWorld Codex plugin marketplace",

  [Parameter(Mandatory = $false)]
  [switch]$Private,

  [Parameter(Mandatory = $false)]
  [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

$Token = $env:GITHUB_TOKEN
if (-not $Token) {
  throw "Missing GITHUB_TOKEN. Create a GitHub fine-grained token with repository Contents read/write permission, then set `$env:GITHUB_TOKEN."
}

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Headers = @{
  "Authorization"        = "Bearer $Token"
  "Accept"               = "application/vnd.github+json"
  "X-GitHub-Api-Version" = "2022-11-28"
  "User-Agent"           = "perfectworld-publisher"
}

function Invoke-GitHubJson {
  param(
    [Parameter(Mandatory = $true)] [string]$Method,
    [Parameter(Mandatory = $true)] [string]$Uri,
    [Parameter(Mandatory = $false)] $Body
  )

  $Params = @{
    Method  = $Method
    Uri     = $Uri
    Headers = $Headers
  }
  if ($null -ne $Body) {
    $Params.Body = ($Body | ConvertTo-Json -Depth 20)
    $Params.ContentType = "application/json"
  }

  $LastError = $null
  foreach ($Attempt in 1..4) {
    try {
      return Invoke-RestMethod @Params
    } catch {
      $LastError = $_
      $StatusCode = $_.Exception.Response.StatusCode.value__
      if ($StatusCode -and $StatusCode -lt 500 -and $StatusCode -ne 429) {
        throw "GitHub API $Method $Uri failed with HTTP $StatusCode. $($_.ErrorDetails.Message)"
      }
      if ($Attempt -lt 4) {
        Start-Sleep -Seconds (2 * $Attempt)
      }
    }
  }
  throw $LastError
}

function Test-RepoExists {
  param([string]$Owner, [string]$Repo)
  try {
    Invoke-GitHubJson -Method "GET" -Uri "https://api.github.com/repos/$Owner/$Repo" | Out-Null
    return $true
  } catch {
    if ($_.Exception.Message -like "*HTTP 404*") {
      return $false
    }
    throw
  }
}

Write-Host "Publishing $Owner/$Repo from $Root"

if (-not (Test-RepoExists -Owner $Owner -Repo $Repo)) {
  Write-Host "Creating repository $Repo..."
  Invoke-GitHubJson -Method "POST" -Uri "https://api.github.com/user/repos" -Body @{
    name        = $Repo
    description = $Description
    private     = [bool]$Private
    auto_init   = $false
  } | Out-Null
} else {
  Write-Host "Repository already exists; uploading files into it."
}

$Files = Get-ChildItem -LiteralPath $Root -Recurse -File -Force |
  Where-Object {
    $_.FullName -notlike "*\.git\*" -and
    $_.FullName -notlike "*.zip"
  }

foreach ($File in $Files) {
  $RootUri = New-Object System.Uri(($Root.TrimEnd("\") + "\"))
  $FileUri = New-Object System.Uri($File.FullName)
  $Relative = [System.Uri]::UnescapeDataString($RootUri.MakeRelativeUri($FileUri).ToString()).Replace("\", "/")
  $Bytes = [System.IO.File]::ReadAllBytes($File.FullName)
  $Content = [Convert]::ToBase64String($Bytes)
  $EncodedPath = ($Relative -split "/" | ForEach-Object { [System.Uri]::EscapeDataString($_) }) -join "/"
  $Uri = "https://api.github.com/repos/$Owner/$Repo/contents/$EncodedPath"

  $Sha = $null
  try {
    $Existing = Invoke-GitHubJson -Method "GET" -Uri "${Uri}?ref=$Branch"
    $Sha = $Existing.sha
  } catch {
    if ($_.Exception.Message -notlike "*HTTP 404*") {
      throw
    }
  }

  $Body = @{
    message = "Publish PerfectWorld marketplace"
    content = $Content
    branch  = $Branch
  }
  if ($Sha) {
    $Body.sha = $Sha
  }

  Write-Host "Uploading $Relative"
  try {
    Invoke-GitHubJson -Method "PUT" -Uri $Uri -Body $Body | Out-Null
  } catch {
    if ($_.Exception.Message -like "*HTTP 422*" -and $_.Exception.Message -like "*sha*") {
      Start-Sleep -Seconds 2
      $Existing = Invoke-GitHubJson -Method "GET" -Uri "${Uri}?ref=$Branch"
      $Body.sha = $Existing.sha
      Invoke-GitHubJson -Method "PUT" -Uri $Uri -Body $Body | Out-Null
    } else {
      throw
    }
  }
}

Write-Host ""
Write-Host "Done: https://github.com/$Owner/$Repo"
Write-Host "Install:"
Write-Host "  codex plugin marketplace add $Owner/$Repo"
Write-Host "  codex plugin add perfectworld@perfectworld"
