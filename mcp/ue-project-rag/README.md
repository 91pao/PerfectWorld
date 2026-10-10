# UE Project RAG MCP

这是跨 Agent 的 UE Project RAG 启动入口。服务通过标准输入输出传输 JSON-RPC，不依赖 Codex 运行时。

```powershell
python .\mcp\ue-project-rag\server.py
```

命令行索引和状态查询：

```powershell
python .\mcp\ue-project-rag\server.py --index <UE_PROJECT_PATH>
python .\mcp\ue-project-rag\server.py --status <UE_PROJECT_PATH>
```

每个 Agent 的配置模板位于 [adapters](../../adapters/README.md)。配置中将 `<repo-root>` 替换为本仓库的绝对路径。
