param(
  [Parameter(Mandatory = $false)]
  [string]$Message = "Update PerfectWorld plugin",

  [Parameter(Mandatory = $false)]
  [string]$Summary,

  [Parameter(Mandatory = $false)]
  [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

$Git = (Get-Command git -ErrorAction SilentlyContinue).Source
if (-not $Git) {
  $DefaultGit = "C:\Program Files\Git\cmd\git.exe"
  if (Test-Path -LiteralPath $DefaultGit) {
    $Git = $DefaultGit
  } else {
    throw "Git is not installed or available on PATH."
  }
}

$Repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
if (-not (Test-Path -LiteralPath (Join-Path $Repo ".git"))) {
  throw "The PerfectWorld publish directory is not connected to Git yet."
}

$Remote = (& $Git -C $Repo remote get-url origin).Trim()
if ($LASTEXITCODE -ne 0 -or -not $Remote) {
  throw "Git remote 'origin' is missing."
}

& $Git -C $Repo fetch origin $Branch
if ($LASTEXITCODE -ne 0) {
  throw "git fetch failed"
}

$Status = & $Git -C $Repo status --porcelain
if ($Status) {
  if (-not $Summary) {
    $Summary = $Message
  }

  $ManifestPath = Join-Path $Repo "plugins\perfectworld\.codex-plugin\plugin.json"
  $Version = (Get-Content -Raw -Encoding UTF8 $ManifestPath | ConvertFrom-Json).version
  $Date = Get-Date -Format "yyyy-MM-dd"
  $Entry = "- $Date | v$Version | $Summary"
  $ChangelogPath = Join-Path $Repo "CHANGELOG.md"
  $Marker = "<!-- publish-entries -->"
  $Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

  if (-not (Test-Path -LiteralPath $ChangelogPath)) {
    [System.IO.File]::WriteAllText(
      $ChangelogPath,
      "# PerfectWorld 更新日志`r`n`r`n## 自动发布记录`r`n`r`n$Marker`r`n",
      $Utf8NoBom
    )
  }

  $Changelog = [System.IO.File]::ReadAllText($ChangelogPath)
  if (-not $Changelog.Contains($Marker)) {
    throw "CHANGELOG.md is missing the publish marker: $Marker"
  }
  if (-not $Changelog.Contains($Entry)) {
    $UpdatedChangelog = $Changelog.Replace($Marker, "$Marker`r`n$Entry")
    [System.IO.File]::WriteAllText($ChangelogPath, $UpdatedChangelog, $Utf8NoBom)
  }

  & $Git -C $Repo add --all
  if ($LASTEXITCODE -ne 0) {
    throw "git add failed"
  }

  & $Git -C $Repo commit -m $Message
  if ($LASTEXITCODE -ne 0) {
    throw "git commit failed"
  }
} else {
  Write-Host "No working-tree changes. Checking for an earlier unpushed commit."
}

& $Git -C $Repo rebase "origin/$Branch"
if ($LASTEXITCODE -ne 0) {
  throw "git rebase failed; resolve the conflict before publishing"
}

& $Git -C $Repo push origin $Branch
if ($LASTEXITCODE -ne 0) {
  throw "git push failed"
}

Write-Host "Published with changelog: https://github.com/91pao/PerfectWorld"
