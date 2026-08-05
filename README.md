# PerfectWorld

PerfectWorld 是一套面向编程 Agent 的工程工作流集合。它把 Unreal Engine 项目协作、本地项目检索和通用软件开发拆成三个可以独立运行、也可以相互组合的组件。

```text
面对 UE 功能、Bug 或跨模块改动：先找项目证据，再决定怎么改
面对几十万行代码：先缩小候选范围，再回到原始文件完成核验
面对通用工程任务：按当前目标选择规格、实现、排查、审查、QA 或发布流程
```

PerfectWorld 可以作为 Codex 插件使用，也可以通过 `core/` 规则、`adapters/` 入口和标准 MCP 服务接入 Claude Code、Cursor、GitHub Copilot / VS Code 以及其他编程 Agent。

## 三个组件

| 组件 | 当前版本 | 解决的问题 | 主要产物 |
| --- | --- | --- | --- |
| `ue-perfectworld` | 0.3.0 | UE 工程中的功能、Bug、资产、Blueprint 和跨系统改动如何找到正确所有者 | 规划、变更规格、实现、排查、审查和 Blueprint 协作结果 |
| `ue-project-rag` | 0.1.0 | 项目文件太多，单次搜索难以找到相关实现和配置 | 本地索引、候选检索、受限内容片段和索引状态 |
| `perfectworld` | 0.4.0 | 通用软件项目从需求到发布涉及多个专业方向 | 规格、计划、实现、QA、审查、设计、发布、文档和维护流程 |

：UE PerfectWorld 负责工程判断，RAG 负责候选发现，PerfectWorld 负责非 UE 的通用开发路由。UE 项目使用前两个组件。

## 组件关系

```text
用户目标
   |
   v
任务路由与工程约束
   |
   +--> UE PerfectWorld ----------------------------+
   |       项目所有权、生命周期、网络、资产、验证      |
   |                                                 |
   +--> UE Project RAG                               |
   |       本地索引、候选检索、片段读取 --------------+--> 原始项目核验
   |                                                 |
   +--> PerfectWorld                                 |
           通用规格、实现、排查、审查、QA、发布
```

RAG 返回的是“可能相关的地方”，不是最终结论。UE PerfectWorld 必须回到原始源码、配置、资产和调用链确认；PerfectWorld 的通用工作流也遵守同样的证据、授权和验证边界。

## UE PerfectWorld

`ue-perfectworld` 是 Unreal Engine 项目的工程协作层。它不只是给出一段 C++ 或 Blueprint 代码，而是先判断当前项目中谁拥有这项职责、数据从哪里来、状态如何流转、什么时候创建和清理，以及改动会影响哪些系统。

### 覆盖的工作流

| 工作流 | 进入条件 | 主要处理 | 交付结果 |
| --- | --- | --- | --- |
| 规划 | 新功能、架构或跨系统需求 | 目标、现有能力、职责归属、依赖和风险 | 可执行计划与验证条件 |
| 排查 | 编译错误、运行异常、回归或行为不一致 | 复现、调用链、数据流、生命周期和根因 | 根因、证据、修复范围和回归检查 |
| 变更规格 | 用户需要完整方案但暂不写入文件 | 文件、资产、配置、接口、依赖和验证边界 | 可直接执行的变更规格 |
| 直接实现 | 用户明确授权修改项目 | 最小范围修改 C++、Blueprint、配置或资产 | 改动文件与聚焦测试结果 |
| 审查 | 当前改动、PR 或 AI 生成代码 | 缺陷、职责重复、边界条件、兼容性和测试缺口 | 按优先级排列的审查结论 |
| Blueprint 协作 | Widget、资产、绑定、编辑器配置或暴露 API | C++ 与 Blueprint 的接口、默认值、资产引用和运行时关系 | 一致的代码、资产和配置变更面 |

### 工程判断模型

UE 任务会围绕以下几类证据展开：

- **调用者**：谁在生产、读取、确认或消费这个状态。
- **权威源**：数据来自对象、配置、表、资产、服务端还是外部系统。
- **生命周期**：入口、创建、更新、确认、持久化、失效和清理分别在哪里发生。
- **网络边界**：客户端、服务端、RPC、代理状态和权限由谁负责。
- **编辑器边界**：继承属性、DataAsset、DataTable、GameplayTag、Widget 绑定和注册点如何参与运行时。
- **变更面**：哪些文件、资产、配置和接口需要新增、替换、调整或仅复用。

每项职责先在 `reuse`、`configure`、`extend` 和 `create` 中选择路径。项目已有能力可以承担职责时，不再创建平行的状态、管理器、缓存、委托或持久化机制。UI 角标、数量和 Brush 等表现差异默认不等于业务状态，必须有项目证据才能升级为独立规则。

### UE 任务流程

```text
用户目标
  -> 识别任务类型与硬边界
  -> 搜索当前项目的调用者、配置、资产和相似实现
  -> 判断职责归属：复用 / 配置 / 扩展 / 新建
  -> 映射入口、数据流、生命周期、网络和清理路径
  -> 生成计划、变更规格或直接实现
  -> 检查 C++、Blueprint、资产、配置和接口的一致性
  -> 按实际环境完成编译、测试、编辑器或运行时验证
```

没有得到写入授权时，工作流输出变更规格，不把“给出代码”当作已经修改项目；完成交付时会区分源码阅读、静态检查、编译、运行时、网络和持久化分别达到的验证等级。

### 与 RAG 的协作

小型项目可以直接使用项目搜索。大型项目安装 RAG 后，流程变成：

```text
RAG status
  -> 必要时建立或刷新索引
  -> 按符号、配置键、Gameplay Tag、资产名或错误文本搜索
  -> 打开最相关的少量片段
  -> 直接读取原始文件、配置和资产
  -> 将已核验事实交给 UE 规划、排查、实现或审查流程
```

RAG 不能证明所有权、生命周期、网络权威、持久化、清理、Blueprint 运行时行为或线上调用关系。它的职责是减少搜索成本，不是替代工程判断。

## UE Project RAG

`ue-project-rag` 是一个完全本地运行的标准 `stdio` MCP 服务。它面向“项目太大，先找到可能相关的实现”这一问题，不要求向量数据库、embedding 服务或远程项目上传。

### 索引组成

```text
UE 项目文件
  -> 路径与敏感文件过滤
  -> 按类型分类
       C/C++/C#       -> 固定行块与符号识别
       INI            -> 配置段
       Markdown/RST  -> 标题段
       assets.json    -> 资产元数据记录
  -> SQLite documents 表
  -> SQLite FTS5 全文索引
  -> .ue-rag/index.sqlite3
```

索引记录文件路径、证据类型、符号、起止行、内容块和内容哈希。支持的内容包括：

| 类型 | 默认范围 |
| --- | --- |
| 源码 | C、C++、C#、Build.cs、Target.cs、头文件 |
| 配置 | INI 文件和配置段 |
| 文档 | Markdown、RST、TXT 等可读取文本 |
| 资产元数据 | `.ue-rag/assets.json` 中的对象路径、资产名和类型 |

常见生成目录 `Binaries`、`Build`、`DerivedDataCache`、`Intermediate`、`Saved`、版本控制目录和常见私钥文件会被跳过；过大的文本文件也不会进入索引。索引本身写入项目的 `.ue-rag/`，建议加入 `.gitignore`：

```gitignore
.ue-rag/
```

### MCP 工具

| 工具 | 输入重点 | 返回内容 |
| --- | --- | --- |
| `ue_rag_status` | 项目根目录 | 索引是否存在、路径和各类覆盖数量 |
| `ue_rag_index` | 项目根目录 | 重建结果、扫描文件数、索引块数和索引路径 |
| `ue_rag_search` | 项目根目录、查询、可选类型和数量 | 路径、类型、符号、行号、评分和摘要片段 |
| `ue_rag_open` | 项目根目录、命中 `result_id` | 指定索引块的完整内容和定位信息 |

检索结果必须带回路径、行号和类型，方便 Agent 从候选结果回到项目原文。评分只用于排序，不是可信度等级。

### RAG 的运行边界

- 本地运行，不调用远程 embedding，不上传工程内容。
- 不读取常见密钥文件和敏感证书后缀。
- 索引落后于分支切换、大范围重构或资产元数据更新时，应先刷新再搜索。
- RAG 不执行代码、不修改项目文件，也不判断 Blueprint 的真实运行时行为。
- RAG 不替代 `rg`、原始文件读取、编辑器检查、编译、运行时追踪或网络验证。

标准启动器位于 [mcp/ue-project-rag](mcp/ue-project-rag/README.md)，不依赖 Codex 运行时。Codex 的包装和技能仍位于 `plugins/ue-project-rag/`，其他 Agent 使用 [adapters](adapters/README.md) 中的 MCP 模板。

## PerfectWorld

`perfectworld` 是通用软件工程的任务路由与交付层。它覆盖从想法到发布后的完整周期，但不会对每个问题加载全部流程，而是根据当前目标选择一个主方向，并在每轮重新判断。

### 路由范围

| 任务方向 | 典型问题 | 主要工作流 |
| --- | --- | --- |
| 产品与方案 | 这个想法是否值得做、范围如何收敛 | 产品评估、规格、计划与架构评审 |
| 工程实现 | 如何改代码、接口或系统结构 | 实现、重构、依赖和开发体验 |
| 调查与质量 | 为什么坏了、是否存在回归 | 根因调查、健康检查、代码审查和 QA |
| 体验与安全 | UI 是否合理、是否有权限或数据风险 | 设计评审、安全分析和开发者体验 |
| 交付与维护 | 如何发布、记录、复盘和延续上下文 | 文档、发布、部署、记忆、复盘和基准 |

现有通用角色覆盖规格、计划、排查、审查、健康、安全、QA、设计、Web、开发者体验、文档、发布、记忆、性能、iOS、复盘、协作和技能沉淀等方向。路由表位于 [core/workflows/task-routing.md](core/workflows/task-routing.md)，通用执行规则位于 [core/workflows/general-development.md](core/workflows/general-development.md)。

### 通用执行流程

```text
最新用户目标
  -> 选择一个主方向
  -> 确认范围、禁止项、现有代码和依赖
  -> 搜索并读取最小必要上下文
  -> 复用 / 配置 / 局部扩展 / 新建
  -> 实施或输出变更规格
  -> 运行与风险匹配的验证
  -> 交付变更、证据、检查结果和未覆盖项
```

通用工作流同样遵守“候选线索不能替代事实”的规则，不把相似代码、搜索摘要或模型推断当作已经验证的项目行为。涉及写入时，交付内容按照 [变更记录约定](core/contracts/change-record.md) 说明目标、依据、变更、影响、验证和未覆盖项。

## 跨 Agent 架构

PerfectWorld 的可移植性来自规则和运行时的分层，而不是把某个 Agent 的插件格式强行复制到其他产品：

```text
Claude / Cursor / Copilot / Codex / 其他 Agent
                         |
                         v
              adapters/ 平台入口与配置
                         |
                         v
       core/ 证据规则、任务路由、UE 与通用工作流
                         |
                         +------------------+
                         |                  |
                         v                  v
                当前项目源码与配置      mcp/ue-project-rag
                                           本地候选检索
```

`plugins/` 保留 Codex marketplace 所需的 manifest、skills、references 和 MCP 包装；`core/` 不依赖任何单一 Agent；`adapters/` 只处理规则入口和客户端配置；`mcp/` 提供可以由多种客户端连接的标准服务。

## 安装与接入

Codex 使用仓库 marketplace：

```powershell
codex plugin marketplace add 91pao/PerfectWorld
codex plugin add ue-perfectworld@perfectworld
codex plugin add ue-project-rag@perfectworld
codex plugin add perfectworld@perfectworld
```

其他 Agent 使用 [adapters/README.md](adapters/README.md) 中对应的规则文件和 MCP 模板，将 `<repo-root>` 替换为本仓库绝对路径即可。安装方式因客户端而异，核心规则和 RAG 服务不随客户端改变。

## 仓库结构

```text
.agents/plugins/marketplace.json    Codex marketplace 定义
core/                                跨 Agent 规则、路由、工作流与交付约定
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
