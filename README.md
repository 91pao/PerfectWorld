# PerfectWorld

面向 Codex 的插件集合。按项目类型安装需要的插件，不需要整套安装。

| 插件 | 适用场景 | 说明 |
| --- | --- | --- |
| `perfectworld` | 产品、应用、服务端、QA、审查、发布与文档 | 通用开发工作流 |
| `ue-perfectworld` | Unreal Engine 的规划、排查、实现、审查与 Blueprint 集成 | 以项目证据为依据；未经明确授权不修改项目文件 |
| `ue-project-rag` | 规模较大的 Unreal Engine 项目 | 本地检索代码、配置、文档与资产元数据 |

## 安装

先登记 marketplace：

```powershell
codex plugin marketplace add 91pao/PerfectWorld
```

再按需安装：

```powershell
codex plugin add perfectworld@perfectworld
codex plugin add ue-perfectworld@perfectworld
codex plugin add ue-project-rag@perfectworld
```

安装后新开一个 Codex 任务，让技能和 MCP 工具重新加载。仓库有更新时执行：

```powershell
codex plugin marketplace upgrade perfectworld
```

## Unreal Engine

`ue-perfectworld` 是 Codex 插件，不是 Unreal Engine 的 `.uplugin`。它不会进入项目的 `Plugins` 目录，也不会参与游戏打包。

处理 UE 任务时，它会先确认当前项目中的调用者、配置、资产、所有权、生命周期、网络权威、持久化和清理路径。只有用户明确要求修改文件时，才会写入工作区。

插件包含路由、规划、排查、只读变更规格、直接实现、审查和 Blueprint 集成七类工作流。具体规则保留在插件内部，不在 README 重复展开。

### 大型项目检索

当仓库规模大到单次搜索难以收敛时，可将 `ue-project-rag` 与 `ue-perfectworld` 一起安装。它会在 UE 项目内创建 `.ue-rag/` 索引，并提供四个 MCP 工具：

- `ue_rag_index`
- `ue_rag_search`
- `ue_rag_open`
- `ue_rag_status`

第一版只做本地结构化检索和全文检索，不调用 embedding 服务，也不上传项目内容。检索结果只是候选线索，UE PerfectWorld 仍会直接读取源码、配置和资产后再下结论。

请在 UE 项目的 `.gitignore` 中加入：

```gitignore
.ue-rag/
```

本地 MCP 服务需要 Python 3.10 或更高版本。

## 仓库结构

```text
.agents/plugins/marketplace.json
plugins/perfectworld/
plugins/ue-perfectworld/
plugins/ue-project-rag/
scripts/
```

## 开发验证

在仓库根目录校验插件：

```powershell
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-perfectworld
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-project-rag
```

RAG 服务的测试：

```powershell
python -m unittest plugins\ue-project-rag\tests\test_ue_rag_mcp.py
```

## 更新记录

Marketplace 的发布记录见 [CHANGELOG.md](CHANGELOG.md)。插件内部的行为变化分别记录在：

- [UE PerfectWorld](plugins/ue-perfectworld/CHANGELOG.md)
- [UE Project RAG](plugins/ue-project-rag/CHANGELOG.md)

## License

[MIT](LICENSE)
