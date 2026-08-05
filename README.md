# PerfectWorld

PerfectWorld 是一套面向工程团队的 Agent 工作流。它将 Unreal Engine 工程协作、本地项目检索和通用开发流程拆分为三个独立组件：可以单独使用，也可以组合使用；Codex、Claude Code、Cursor、GitHub Copilot / VS Code 与其他支持项目指令和 MCP 的 Agent 都可以接入。

## 组件一览

| 组件 | 当前版本 | 核心职责 | 适用场景 |
| --- | --- | --- | --- |
| `ue-perfectworld` | 0.3.0 | UE 功能规划、排查、实现、审查和 Blueprint 协作 | Unreal Engine 代码与资产工程 |
| `ue-project-rag` | 0.1.0 | 本地代码、配置、文档与资产元数据检索 | 文件多、模块多、历史实现复杂的 UE 项目 |
| `perfectworld` | 0.4.0 | 通用产品、工程、质量、发布与维护工作流 | 应用、服务端、工具和网站 |

## Codex 安装

先登记 marketplace：

```powershell
codex plugin marketplace add 91pao/PerfectWorld
```

按项目安装组件：

```powershell
# UE 工程
codex plugin add ue-perfectworld@perfectworld

# 大型 UE 工程的本地检索
codex plugin add ue-project-rag@perfectworld

# 通用开发项目
codex plugin add perfectworld@perfectworld
```

插件更新后执行：

```powershell
codex plugin marketplace upgrade perfectworld
```

## 其他 Agent

跨平台规则位于 [core](core/README.md)，RAG 使用标准 `stdio` MCP 服务，平台入口和配置模板位于 [adapters](adapters/README.md)。

| Agent | 工作流入口 | RAG 配置 |
| --- | --- | --- |
| Claude Code | `adapters/claude-code/CLAUDE.md` | `adapters/claude-code/mcp.json.example` |
| Cursor | `adapters/cursor/.cursor/rules/perfectworld.mdc` | `adapters/cursor/mcp.json.example` |
| GitHub Copilot / VS Code | `adapters/github-copilot/.github/copilot-instructions.md` | `adapters/github-copilot/mcp.json.example` |
| 其他支持项目指令与 MCP 的 Agent | `adapters/generic/AGENTS.md` | `adapters/generic/mcp.json.example` |

将模板中的 `<repo-root>` 替换为本仓库的绝对路径。各平台只适配入口与配置；工程约束、UE 工作流和检索规则都复用同一套 `core/` 文件。

## UE PerfectWorld

`ue-perfectworld` 用于在既有 Unreal Engine 项目中完成功能设计、代码改动、Bug 排查、代码审查和 Blueprint 集成。它将 C++、模块、Blueprint、Widget、DataAsset、DataTable、GameplayTag、INI 配置、网络边界、状态所有权、持久化和清理视为一个连续的工程变更面，而不是彼此独立的检查项。

在 Codex 中它以插件形式运行，不会写入 Unreal 工程的 `Plugins` 目录，也不会参与游戏打包。其他 Agent 则通过 [UE 核心工作流](core/workflows/unreal-engine.md) 使用相同的工程规则。

### 工作流

| 工作流 | 处理内容 | 交付重点 |
| --- | --- | --- |
| 规划 | 功能边界、架构选择、现有能力匹配 | 复用、配置、扩展或新建的明确选择 |
| 排查 | 编译错误、运行异常、回归与根因 | 可验证假设、调用链和真实根因 |
| 变更规格 | 暂不写入项目时的实现方案 | 文件、资产、配置、依赖、风险与验证条件 |
| 直接实现 | 用户授权后的代码与配置修改 | 最小改动、兼容调用者和聚焦验证 |
| 审查 | 当前改动、PR、AI 生成代码与回归风险 | 缺陷、边界条件、测试缺口和优先级 |
| Blueprint 协作 | 资产设置、Widget 绑定、暴露 API 与编辑器配置 | C++、资产、默认值和绑定关系的一致性 |

### 工程判断方式

- 先定位活跃调用者、权威数据或配置源、状态所有者、生命周期和清理路径，再决定改动位置。
- 每项职责优先选择 `reuse`、`configure`、`extend` 或 `create`。项目已有可用能力时，不用平行机制覆盖它。
- UI 角标、数量和 Brush 等表现默认不等于独立业务状态；多个界面展示同一状态时复用同一权威来源。
- 新增 DataAsset、RPC、委托、管理器、缓存、状态代理或生命周期覆写时，重新检查网络、持久化、确认和清理影响。
- 结束时说明源码、配置、编辑器和运行环境中已经验证的部分，以及仍未覆盖的风险。

### 与 RAG 协作

规模较大的项目可同时安装 `ue-project-rag`。RAG 先根据符号、Tag、配置键、资产名或报错文本定位候选；UE PerfectWorld 再打开原始源码、配置和资产完成核验。检索结果用于缩小调查范围，不替代调用链、运行时或生命周期判断。

## UE Project RAG

`ue-project-rag` 是一个完全本地运行的标准 `stdio` MCP 服务。它面向大型 UE 项目的“先找到哪里，再确认为什么”的问题：将可读取的项目内容建立为 SQLite 全文索引，返回带有路径、符号、行号、片段和评分的候选结果。

### 索引内容

| 类别 | 内容 |
| --- | --- |
| 源码 | C、C++、C#、Build.cs、Target.cs 与头文件 |
| 配置 | INI 文件及其配置段 |
| 文档 | Markdown、RST、TXT 与其他可读取说明文件 |
| 资产元数据 | `.ue-rag/assets.json` 中导出的对象路径、资产名和类型 |

索引以内容块保存文件路径、类型、符号、起止行和摘要。它自动跳过 `.git`、`Binaries`、`Build`、`DerivedDataCache`、`Intermediate`、`Saved`、常见私钥和环境文件，并忽略超过大小上限的文本。

### MCP 工具

| 工具 | 作用 | 典型用途 |
| --- | --- | --- |
| `ue_rag_status` | 查看索引是否存在及覆盖范围 | 开始调查前确认索引状态 |
| `ue_rag_index` | 新建或重建本地索引 | 首次使用、分支切换或大范围重构后 |
| `ue_rag_search` | 按关键词、符号或配置键检索候选 | 查找现有实现、资产引用和配置入口 |
| `ue_rag_open` | 读取某个命中块的完整受限内容 | 确认最相关候选的上下文 |

索引默认写入 UE 项目本地的 `.ue-rag/`：

```gitignore
.ue-rag/
```

服务不调用 embedding 服务，不上传工程内容。它的职责是候选发现，不能单独证明所有权、网络权威、持久化、清理、Blueprint 运行时行为或活跃生产调用关系。需要 Python 3.10 或更高版本。

### 跨 Agent 使用

标准启动入口位于 [mcp/ue-project-rag](mcp/ue-project-rag/README.md)。Claude Code、Cursor、Copilot 和其他 MCP 客户端均可使用 [适配层模板](adapters/README.md) 连接同一个服务端。

## PerfectWorld

`perfectworld` 面向非 UE 的通用工程任务。它不是固定的一套“开发步骤”，而是根据当前问题在产品、规格、实现、质量和交付之间选择主工作流；每一轮以最新需求和当前代码库状态为准，避免把上一步的假设带入下一步。

### 覆盖范围

| 方向 | 能力 |
| --- | --- |
| 产品与方案 | 想法评估、需求澄清、规格、Issue、验收标准、架构与计划评审 |
| 工程实现 | 功能实现、Bug 根因调查、代码审查、健康检查、性能与安全分析 |
| 体验与接口 | UI / UX 设计评审、网页操作、开发者体验、API、CLI 与 SDK 可用性 |
| 质量与发布 | 网站和应用 QA、只读 QA、文档维护、发布准备、部署检查与上线后观察 |
| 长期维护 | 项目记忆、阶段复盘、性能基准、跨 Agent 协作与可复用流程沉淀 |

### 执行方式

1. 根据任务选择一个主方向，例如规格、排查、审查、QA、发布或设计。
2. 搜索并读取必要的实现、配置、依赖和历史上下文，避免按通用模板臆测项目结构。
3. 在复用、配置、局部扩展和新建之间选择改动最小的路径。
4. 将验证范围与风险相匹配，优先执行高信号检查；功能稳定后再进入完整交付验证。
5. 交付时说明变更、验证结果、未覆盖项和风险，不用“已完成”代替实际验证。

通用 Agent 可通过 [任务路由](core/workflows/task-routing.md)、[通用开发工作流](core/workflows/general-development.md) 和 [工程约定](core/AGENT-CONTRACT.md) 使用同一套能力。

## 仓库结构

```text
.agents/plugins/marketplace.json    Codex marketplace 定义
core/                                跨 Agent 工作流、规则与交付约定
mcp/ue-project-rag/                  标准 stdio MCP 启动入口
adapters/                            Codex、Claude Code、Cursor、Copilot 与通用入口
plugins/perfectworld/               通用开发 Codex 插件
plugins/ue-perfectworld/            UE Codex 插件
plugins/ue-project-rag/             UE RAG Codex 包装、服务和测试
scripts/                            发布、验证与维护脚本
```

## 开发与验证

```powershell
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-perfectworld
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-project-rag
python -m unittest plugins\ue-project-rag\tests\test_ue_rag_mcp.py
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-agent-adapters.ps1
```

## 版本记录

- [仓库更新日志](CHANGELOG.md)
- [UE PerfectWorld](plugins/ue-perfectworld/CHANGELOG.md)
- [UE Project RAG](plugins/ue-project-rag/CHANGELOG.md)

## License

[MIT](LICENSE)
