param(
  [Parameter(Mandatory = $false)]
  [string]$Message = "Update PerfectWorld plugin",

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

Write-Host "Published: https://github.com/91pao/PerfectWorld"
