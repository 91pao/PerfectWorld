[CmdletBinding()]
param(
    [string]$RepositoryRoot
)

if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = Split-Path -Parent $PSScriptRoot
}

$RepositoryRoot = (Resolve-Path -LiteralPath $RepositoryRoot).Path
$requiredFiles = @(
    'core/AGENT-CONTRACT.md',
    'core/workflows/task-routing.md',
    'core/workflows/general-development.md',
    'core/workflows/unreal-engine.md',
    'core/policies/retrieval.md',
    'core/contracts/change-record.md',
    'mcp/ue-project-rag/server.py',
    'adapters/claude-code/CLAUDE.md',
    'adapters/claude-code/mcp.json.example',
    'adapters/cursor/.cursor/rules/perfectworld.mdc',
    'adapters/cursor/mcp.json.example',
    'adapters/github-copilot/.github/copilot-instructions.md',
    'adapters/github-copilot/mcp.json.example',
    'adapters/generic/AGENTS.md',
    'adapters/generic/mcp.json.example'
)

foreach ($relativePath in $requiredFiles) {
    $path = Join-Path $RepositoryRoot $relativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Missing cross-agent file: $relativePath"
    }
}

$mcpTemplates = @(
    'adapters/claude-code/mcp.json.example',
    'adapters/cursor/mcp.json.example',
    'adapters/github-copilot/mcp.json.example',
    'adapters/generic/mcp.json.example'
)

foreach ($relativePath in $mcpTemplates) {
    $content = Get-Content -LiteralPath (Join-Path $RepositoryRoot $relativePath) -Raw -Encoding UTF8
    $null = $content | ConvertFrom-Json
    if ($content -notmatch 'mcp/ue-project-rag/server\.py') {
        throw "MCP template does not use the shared server entry point: $relativePath"
    }
}

Write-Host 'Cross-agent adapter layout check passed.'
