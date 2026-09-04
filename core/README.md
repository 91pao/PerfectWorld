# PerfectWorld Core

这里是 PerfectWorld 的跨 Agent 规则层。内容不依赖 Codex、Claude Code、Cursor 或 GitHub Copilot 的专有指令格式；各平台入口位于 [adapters](../adapters/README.md)。

## 加载顺序

1. 读取 [AGENT-CONTRACT.md](AGENT-CONTRACT.md)。
2. 先使用 [任务路由](workflows/task-routing.md) 选择方向，再读取 [通用开发](workflows/general-development.md) 或 [UE 工程](workflows/unreal-engine.md) 工作流。
3. 大型 UE 项目需要检索时，再读取 [本地检索规则](policies/retrieval.md)。
4. 涉及写入时，按 [变更记录约定](contracts/change-record.md) 交付。

核心层定义行为和交付边界；平台适配层只负责让对应 Agent 找到这些文件并连接 MCP 服务。
