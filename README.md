# PerfectWorld

PerfectWorld 是一组面向 Codex 的工程插件。通用开发、Unreal Engine 工作流和大型项目检索分别拆成独立组件，按项目需要组合安装。

## 插件一览

| 插件 | 当前版本 | 负责内容 | 适用项目 |
| --- | --- | --- | --- |
| `perfectworld` | 0.4.0 | 产品、规格、计划、实现、排查、审查、QA、发布与文档 | 应用、服务端、工具和网站 |
| `ue-perfectworld` | 0.3.0 | UE 规划、代码排查、实现、审查与 Blueprint 协作 | Unreal Engine 项目 |
| `ue-project-rag` | 0.1.0 | 本地代码、配置、文档与资产元数据检索 | 文件数量较多的 UE 项目 |

## 安装

先登记 marketplace：

```powershell
codex plugin marketplace add 91pao/PerfectWorld
```

再选择需要的组件：

```powershell
# 通用开发
codex plugin add perfectworld@perfectworld

# Unreal Engine 工作流
codex plugin add ue-perfectworld@perfectworld

# 大型 UE 项目的检索能力
codex plugin add ue-project-rag@perfectworld
```

插件更新后执行：

```powershell
codex plugin marketplace upgrade perfectworld
```

## PerfectWorld

`perfectworld` 面向通用工程任务，覆盖从需求收敛到发布后的完整开发周期。它会根据当前任务选择合适的工作流，而不是要求为每类问题单独安装插件。

| 工作方向 | 覆盖内容 |
| --- | --- |
| 产品与方案 | 需求梳理、规格、计划、架构与开发体验 |
| 工程实现 | 排查、代码审查、质量检查、性能与安全分析 |
| 交付维护 | QA、文档、发布准备、阶段复盘与项目记忆 |

适合应用、服务端、工具和网站项目。对于 Unreal Engine 项目，使用下方的 UE PerfectWorld 组件。

## UE PerfectWorld

| 工作内容 | 建议安装 | 结果 |
| --- | --- | --- |
| 功能设计、Bug 排查、代码审查、Blueprint 协作 | `ue-perfectworld` | 从当前项目的调用关系、配置、资产与生命周期中建立实施依据 |
| 数千文件的项目、跨模块查找、历史实现对照 | `ue-perfectworld` + `ue-project-rag` | 先定位候选，再回到项目源码和配置完成核验 |

`ue-perfectworld` 是 Codex 插件，不会写入 Unreal 工程的 `Plugins` 目录，也不会进入游戏打包流程。它把代码、Blueprint、配置、DataAsset、网络边界、状态所有权、持久化与清理视为同一个工程问题，而不是分散的独立检查项。

它包含规划、排查、只读变更规格、直接实现、审查与 Blueprint 集成等工作流，适合需要在既有 UE 项目约束下完成改动的任务。

## UE Project RAG

`ue-project-rag` 为本地 MCP 服务建立 `.ue-rag/` 索引，覆盖：

- C++、Blueprint 相关文本、INI、JSON、CSV、Markdown 与其他可读取项目文件
- 符号、路径、文件摘要与受支持资产的元数据
- 关键词、路径与内容片段检索

服务提供四个工具：

| 工具 | 用途 |
| --- | --- |
| `ue_rag_index` | 建立或刷新索引 |
| `ue_rag_search` | 检索候选代码、配置、文档和资产 |
| `ue_rag_open` | 读取命中的受限内容片段 |
| `ue_rag_status` | 查看索引覆盖范围与状态 |

索引默认保留在项目本地，不调用 embedding 服务，也不上传工程内容。将下列规则加入 UE 项目的 `.gitignore`：

```gitignore
.ue-rag/
```

运行本地 MCP 服务需要 Python 3.10 或更高版本。

## 仓库结构

```text
.agents/plugins/marketplace.json    Marketplace 定义
plugins/perfectworld/               通用开发插件
plugins/ue-perfectworld/            Unreal Engine 工作流
plugins/ue-project-rag/             UE 本地检索服务与测试
scripts/                            发布与维护脚本
```

## 开发与验证

```powershell
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-perfectworld
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-project-rag
python -m unittest plugins\ue-project-rag\tests\test_ue_rag_mcp.py
```

## 版本记录

- [仓库更新日志](CHANGELOG.md)
- [UE PerfectWorld](plugins/ue-perfectworld/CHANGELOG.md)
- [UE Project RAG](plugins/ue-project-rag/CHANGELOG.md)

## License

[MIT](LICENSE)
