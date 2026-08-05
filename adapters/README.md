# Agent 适配层

核心规则统一放在 [core](../core/README.md)，本目录只保存平台入口和 MCP 配置模板。每个模板中的 `<repo-root>` 都应替换为 PerfectWorld 仓库的绝对路径。

| 平台 | 规则入口 | MCP 模板 |
| --- | --- | --- |
| Codex | [说明](codex/README.md) | 由现有 marketplace 插件提供 |
| Claude Code | [CLAUDE.md](claude-code/CLAUDE.md) | [mcp.json.example](claude-code/mcp.json.example) |
| Cursor | [规则](cursor/.cursor/rules/perfectworld.mdc) | [mcp.json.example](cursor/mcp.json.example) |
| GitHub Copilot / VS Code | [指令](github-copilot/.github/copilot-instructions.md) | [mcp.json.example](github-copilot/mcp.json.example) |
| 其他 Agent | [AGENTS.md](generic/AGENTS.md) | [mcp.json.example](generic/mcp.json.example) |

不同客户端的 MCP 配置位置会随产品版本变化；模板定义的传输方式保持不变：`python <repo-root>/mcp/ue-project-rag/server.py`，工作目录为 `<repo-root>`。
