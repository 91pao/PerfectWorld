# PerfectWorld Codex Plugins

本仓库是一个 Codex marketplace，同时发布两个可以独立安装的插件：

- `perfectworld`：面向通用软件项目的完整产品开发专家团队。
- `ue-perfectworld`：面向所有 Unreal Engine 项目的安全开发与教学工作流。

它们共用一个 GitHub 仓库和 marketplace，但不存在安装依赖。添加 marketplace 只是让 Codex
知道插件来源；安装其中一个插件不会自动安装另一个。

## 插件怎么选

| 对比项 | PerfectWorld | UE PerfectWorld |
| --- | --- | --- |
| 插件 ID | `perfectworld` | `ue-perfectworld` |
| 主要对象 | Web、App、服务端、产品和通用软件项目 | Unreal Engine C++、Blueprint、Gameplay、UI、网络、资产、编辑器和构建配置 |
| 核心范围 | 从产品立项到设计、开发、QA、安全、发布和复盘的完整流程 | UE 功能规划、只读排查、教学实现、授权后直接实现、代码审查和 Blueprint 协作 |
| 内置工作流 | 23 个通用专家角色 | 7 个 UE 专用技能和 10 份工程规则 |
| 默认写文件策略 | 根据任务和用户要求执行 | 默认不修改工作区，只有明确要求写入文件时才修改 |
| 代码交付重点 | 完成通用工程任务并验证结果 | 可在对话中按真实编写顺序给出可逐字录入的完整代码和全面、简洁的 `//` 注释 |
| 项目适配方式 | 根据当前软件项目选择专家角色 | 读取当前 UE 项目的真实类型、调用链、生命周期、网络权威和资产配置，不硬编码具体项目惯例 |
| 是否可以单独安装 | 可以 | 可以 |

PerfectWorld 是一套面向 Codex 的专家角色插件，用来覆盖从 0 立项、需求澄清、架构规划、编码实现、调试、代码审查、QA、设计打磨、安全审计、文档、发布到复盘的完整开发流程。

它的核心目标不是让你手动记住一堆命令，而是让 Codex 在每一轮任务开始时自动判断当前最合适的专家角色，并用中文开场说明：

```text
我是完美世界 XXX，我擅长 XXX，本轮我负责 XXX 问题。
```

## 适合谁

- 想用 Codex 从 0 做完整项目的人。
- 想让 Codex 在多轮目标模式里自动切换角色的人。
- 想把产品、架构、开发、QA、发布这些流程串起来的人。
- 想要一个中文友好、角色明确、能解释自己为什么这样做的 Codex 插件的人。

## 当前仓库

- GitHub: <https://github.com/91pao/PerfectWorld>
- 插件 ID: `perfectworld`、`ue-perfectworld`
- Marketplace 名称: `perfectworld`
- 开发者: `Liutianyuan / PerfectWorld`
- 官网: <https://games.wanmei.com/>

## 安装

先在 Codex CLI 中添加本仓库的 marketplace。这个命令只登记插件来源，不会安装任何插件：

```powershell
codex plugin marketplace add 91pao/PerfectWorld
```

### 只安装 UE PerfectWorld

只运行下面这一条安装命令：

```powershell
codex plugin add ue-perfectworld@perfectworld
```

这只会安装 `ue-perfectworld`，不会安装通用的 `perfectworld`。这是只需要 Unreal Engine
工作流时的推荐安装方式。

### 只安装 PerfectWorld

```powershell
codex plugin add perfectworld@perfectworld
```

这只会安装通用的 PerfectWorld，不会安装 UE PerfectWorld。

### 同时安装两个插件

需要同时处理通用产品流程和 UE 专项开发时，可以分别安装：

```powershell
codex plugin add perfectworld@perfectworld
codex plugin add ue-perfectworld@perfectworld
```

安装完成后，建议开启一个新的 Codex 任务，让 Codex 重新加载插件技能。仓库更新后可以刷新 marketplace：

```powershell
codex plugin marketplace upgrade perfectworld
```

## UE PerfectWorld

`ue-perfectworld` 是供 Codex 使用的项目中立 Unreal Engine 工作流插件，不是安装到 Unreal
Engine 项目 `Plugins` 目录中的 `.uplugin`，也不包含会进入游戏包体的运行时代码。它通过技能和
规则约束 Codex 如何理解、讲解、修改和审查 UE 项目。

它适用于 UE C++、Blueprint、Gameplay、UI、网络、资产与数据、编辑器工具、模块与构建配置、
问题排查和代码审查。插件不会把任何具体项目 API、模块名或旧代码当作通用模板。

### 里面有什么

| Skill | 作用 |
| --- | --- |
| `ue-router` | 判断当前 UE 任务应该进入规划、教学实现、直接实现、排查、审查还是 Blueprint 工作流。 |
| `ue-plan` | 在不修改文件的前提下拆解功能、确认架构边界、依赖、生命周期、网络权威和验证方案。 |
| `ue-investigate` | 先读取证据、复现和追踪调用链，定位根因；不会用重试、延迟或静默返回掩盖问题。 |
| `ue-draft` | 默认模式，在对话中按用户实际编写顺序给出完整代码和编辑器步骤。 |
| `ue-implement` | 只有用户明确要求修改文件、应用补丁或写入工作区时，才直接实现并验证改动。 |
| `ue-review` | 审查 C++、Blueprint 集成、生命周期、网络权威、资产配置、生成代码漂移和回归风险。 |
| `ue-blueprint` | 处理 C++ 与 Blueprint 的职责边界、暴露 API、事件、资产、控件和编辑器配置步骤。 |

除了 7 个技能，插件还包含 10 份 UE 工程规则，按“核心加按需”方式加载：核心规则负责默认
只读、项目证据与一致性、完整实现和最终自审；网络、事务、UI 参数、编码、注释日志和 bug 修复
规则只在任务确实需要时读取，避免重复上下文。

### 核心行为

- **默认不修改项目**：读取和分析工作区是允许的，但只有“直接修改文件”“应用这个补丁”这类明确要求才会写入。
- **非简单任务先过证据门禁**：不能只看类名或附近一个文件；必须追踪真实调用、注册、数据与资产、运行时所有者、生命周期、网络权威、持久化和 C++/Blueprint 分工，并先建立入口、权威数据源、清理路径等所有权图。
- **不同职责必须分别取证**：相似功能不能同时证明 UI 组合、导航、状态、生命周期、空值处理和日志策略；新增遍历、直接访问管理器、绕过封装或改变日志路径时，必须重新调查对应职责的项目先例。
- **跨系统教学先确认最小设计**：先展示已验证证据、所有权图、与参考实现的差异和最小方案，得到确认后再给完整可逐字录入代码；用户明确要求跳过时除外。
- **可以完全在对话里实现**：按照真实依赖顺序说明要修改的准确文件、位置、完整声明、完整函数体、调用点、Blueprint 操作和验证步骤，不使用伪代码或省略关键实现。
- **代码可以逐字录入**：代码块不使用省略号、`TODO`、占位类型或“其余自行补充”，需要的 include、宏、模块依赖、绑定和失败分支必须完整。
- **注释全面但简洁**：类、结构体、函数、关键属性和非显然逻辑都应覆盖；默认使用一行 `//` 说明一个必要意图，只有生命周期、所有权、网络权威或失败行为确实无法一行说清时才扩展为连续多行 `//`。
- **遵循当前项目而不是某个样板项目**：只采用在当前仓库中有活跃调用证据、职责兼容且生命周期一致的先例。
- **代码必须能脱离聊天记录维护**：坚持单一权威数据源和清晰执行路径；每个新类型、字段、委托、覆写和抽象都要有当前需求与真实调用者，并通过需求变更、功能删除和无聊天上下文三项测试。
- **连续失败时回溯架构**：反复出现编译、链接、反射、资产或配置失败时，停止叠加局部补丁，重新追踪所有权、数据流、生命周期、注册和项目先例。
- **失败处理遵循项目路径**：不强制所有提前返回都记录日志，也不默认静默失败；先区分预期拒绝、可恢复异常和真实缺陷，再沿用同职责代码的防护、反馈与诊断方式。
- **最终自审是阻断阶段**：交付前重新检查正确性、安全、反射、生命周期、网络、持久化和失败路径；发现已知 BUG 必须先修复。若一个约 50 行可以清楚完成的功能被写成约 300 行，则视为复杂度审查失败，删除无用抽象并重写后再交付。

### 两种实现方式

默认采用对话教学模式：

```text
用 UE PerfectWorld 实现这个功能。不要修改项目文件，按照我应当编写的顺序给出完整代码和全面、简洁的 // 注释。
```

只有明确授权后才直接写入项目：

```text
用 UE PerfectWorld 直接修改项目文件实现这个功能，并在结束前完成最终自审和验证。
```

### 快速使用

```text
用 UE PerfectWorld 规划这个 Unreal Engine 功能
```

```text
用 UE PerfectWorld 排查这个 UE bug 的根因
```

```text
用 UE PerfectWorld 按照我应当编写的顺序给出完整代码，不要修改文件
```

```text
用 UE PerfectWorld 审查当前 UE 改动，优先找会造成崩溃、网络越权、生命周期错误或数据损坏的问题
```

## 快速开始

可以直接这样和 Codex 说：

```text
用 PerfectWorld 帮我从 0 规划一个 SaaS 项目
```

```text
用 PerfectWorld 帮我 QA localhost:3000
```

```text
用 PerfectWorld 查这个 bug 的根因
```

```text
用 PerfectWorld review 当前改动
```

```text
这个 UI 看起来怪怪的，用 PerfectWorld 帮我看
```

```text
用 PerfectWorld 帮我准备发布
```

## 工作方式

PerfectWorld 的每个角色都会遵守同一个多轮协议：

1. 每一轮开始时重新判断当前项目状态和用户最新需求。
2. 如果当前角色不是最合适的，会切换到更合适的 PerfectWorld 角色。
3. 选定角色后，用中文说明自己是谁、擅长什么、本轮负责什么。
4. 按 Codex 原生工具执行任务，不依赖 Claude slash command、Claude hooks、Bun 或旧浏览器守护进程。
5. 对代码修改、网页 QA、发布检查等任务尽量做验证，而不是只给建议。

## 分阶段测试策略

PerfectWorld `0.4.0` 把长项目的验证分成两种模式，避免在每个中间轮次重复执行全量测试、浪费时间和 token。

### ITERATION：开发中间轮次

这是默认模式。新增功能、局部修改、修复单个 bug、完成一个子任务或结束一轮对话，都仍然属于 `ITERATION`。

- 只运行与本轮改动直接相关的测试文件、模块、包或页面路径。
- 类型检查、lint、构建和浏览器 QA 也尽量限制在受影响范围内。
- 涉及共享接口、数据库 schema、认证、安全边界或公共基础设施时，可以扩大到受影响的依赖边界，但不会自动运行整个仓库的测试。
- 每轮说明实际验证了什么，以及哪些全量检查被有意留到最终交付。

### FINAL_DELIVERY：最终交付

只有用户明确表示“最终版本”“最终交付”“准备发布”“全量验收”“跑全量测试”，或确认实现已经完成并要求最终验收时，才进入 `FINAL_DELIVERY`。

- 等所有实现稳定后，再统一运行完整测试、构建、lint 和必要的全流程 QA。
- 完整套件通常集中运行一次；修复失败项时先做局部复测，必要时最后再做一次完整确认。
- 选中 `perfectworld-qa`、`perfectworld-review`、`perfectworld-investigate` 或 `perfectworld-release` 本身，不代表自动获得运行全量测试的许可。

例如，在一个从 0 搭建的长项目中：

```text
帮我加入用户头像上传
```

只验证头像上传相关模块和页面流程。

```text
功能已经全部完成，现在做最终交付和全量验收
```

此时才运行完整测试套件和最终 QA。

## 上下文与 token 优化

`0.4.0` 在不删除角色能力和完整方法论的前提下，减少长任务中的重复上下文消耗：

- 每轮只选择一个主角色；其他专业视角默认作为简短检查项，不重复加载多个完整角色。
- 角色正文只保留使命、核心能力和执行规则；继承的方法论移动到按需 playbook，需要时只读取相关章节。
- 先搜索符号、文件和标题，再读取最小必要范围，不反复打开未变化的完整文件。
- 复用仍然有效的测试结果和项目事实；只有相关代码、配置、依赖或环境变化时才重新验证。
- 成功日志只保留命令、范围、结果数量和必要耗时；只有失败时展开堆栈、日志和诊断。
- 计划只更新本轮变化、阻塞和下一步，不在每轮重复完整计划和历史总结。
- 多 Agent 只用于真正独立、可并行且收益高于协调成本的工作。

每轮验证会维护一个简短记录：改动范围、风险等级、已通过检查、延后到最终交付的检查，以及哪些变化会让旧结果失效。

## 角色清单

PerfectWorld 当前包含 23 个合并后的专家角色。

| Skill | 中文角色 | 主要职责 |
| --- | --- | --- |
| `perfectworld-router` | 完美世界路由官 | 自动判断需求并选择最合适的专家角色。 |
| `perfectworld-office-hours` | 完美世界产品顾问 | 打磨产品想法、挑战需求假设、判断方向是否值得做。 |
| `perfectworld-spec` | 完美世界规格作者 | 把模糊想法变成可执行规格、issue、ticket 或实现计划。 |
| `perfectworld-plan` | 完美世界计划总审官 | 综合 CEO、工程、设计、开发体验视角审查复杂计划和架构。 |
| `perfectworld-investigate` | 完美世界根因调查员 | 复现问题、定位根因、再进行修复。 |
| `perfectworld-review` | 完美世界代码审查员 | 审查 diff、PR 或当前改动，优先发现真实风险。 |
| `perfectworld-qa` | 完美世界 QA 工程师 | 测试网站、App、功能，发现并可修复问题。 |
| `perfectworld-qa-only` | 完美世界 QA 报告员 | 只测试和报告问题，不修改代码。 |
| `perfectworld-design` | 完美世界设计总监 | 设计咨询、多方案探索、视觉审查和 HTML/CSS 设计落地。 |
| `perfectworld-cso` | 完美世界首席安全官 | 安全审计、威胁建模、OWASP/STRIDE 风险分析。 |
| `perfectworld-release` | 完美世界发布总管 | 部署配置、发布前检查、PR 准备、合并部署和上线后验证。 |
| `perfectworld-docs` | 完美世界文档工程师 | 生成缺失文档，并在发布时同步维护文档。 |
| `perfectworld-health` | 完美世界代码健康检查员 | 检查代码健康、复杂度、技术债和维护风险。 |
| `perfectworld-devex-review` | 完美世界开发者体验审查员 | 审查 API、CLI、SDK、文档和上手路径。 |
| `perfectworld-benchmark` | 完美世界基准测试员 | 性能回归检测，比较模型效果、成本和速度。 |
| `perfectworld-web` | 完美世界 Web 操作员 | 浏览器操作、页面检查、登录态辅助和网页数据提取。 |
| `perfectworld-ios` | 完美世界 iOS 工程师 | iOS QA、SwiftUI 修复、设计审查、调试桥清理和同步。 |
| `perfectworld-memory` | 完美世界项目大脑管理员 | 项目长期记忆、PBrain、上下文保存与恢复。 |
| `perfectworld-pair-agent` | 完美世界多智能体协调员 | 协调多个 agent 或浏览器会话并行协作。 |
| `perfectworld-skillify` | 完美世界技能固化员 | 把成功流程沉淀成新的可复用 skill。 |
| `perfectworld-retro` | 完美世界工程复盘主持人 | 做阶段复盘，总结节奏、风险、质量和改进机会。 |
| `perfectworld-make-pdf` | 完美世界 PDF 制作员 | 把 Markdown 或报告制作成高质量 PDF。 |
| `perfectworld-upgrade` | 完美世界自升级维护员 | 维护 PerfectWorld 插件自身的更新和再生成。 |

## 路由规则

你可以直接描述需求，PerfectWorld 会按大致规则选择角色：

| 需求类型 | 默认角色 |
| --- | --- |
| 想法、产品方向、值不值得做 | `perfectworld-office-hours` |
| 写需求、写 issue、写 ticket、整理规格 | `perfectworld-spec` |
| 复杂功能、架构设计、计划评审 | `perfectworld-plan` |
| bug、报错、异常行为、回归 | `perfectworld-investigate` |
| diff、PR、当前改动审查 | `perfectworld-review` |
| 网站/App/功能测试并允许修复 | `perfectworld-qa` |
| 只要 QA 报告，不允许修改 | `perfectworld-qa-only` |
| UI 怪、视觉不统一、设计系统 | `perfectworld-design` |
| 安全审计、认证授权、数据泄露风险 | `perfectworld-cso` |
| 发布、部署、PR 准备、上线后验证 | `perfectworld-release` |
| 写文档、补 README、发布后同步文档 | `perfectworld-docs` |
| 性能、成本、速度、模型比较 | `perfectworld-benchmark` |
| iOS、SwiftUI、真机 QA | `perfectworld-ios` |

## 从 0 立项的推荐流程

如果你从 0 做一个项目，可以这样开始：

```text
用 PerfectWorld 目标模式帮我从 0 立项一个项目。每一轮都重新判断当前最合适的角色，并说明你是谁、擅长什么、本轮负责什么。
```

一个典型流程可能是：

1. `perfectworld-office-hours`：判断想法是否值得做，明确目标用户和核心价值。
2. `perfectworld-spec`：把想法变成规格、用户故事、验收标准和任务拆分。
3. `perfectworld-plan`：审查架构、边界、风险和实现计划。
4. `perfectworld-design`：建立界面方向、交互原则和视觉质量标准。
5. `perfectworld-investigate` / `perfectworld-qa`：开发中定位问题、测试功能。
6. `perfectworld-review`：发布前检查代码、测试覆盖和风险。
7. `perfectworld-release`：准备 PR、部署、上线后验证。
8. `perfectworld-docs` / `perfectworld-retro`：补文档并复盘。

## 示例对话

### 产品探索

```text
用 PerfectWorld 帮我判断这个 AI 工具想法值不值得做，并给我一个 MVP 版本。
```

预期会选择：`perfectworld-office-hours`

### 规格生成

```text
用 PerfectWorld 把这个需求整理成可以直接开发的 issue。
```

预期会选择：`perfectworld-spec`

### 架构审查

```text
用 PerfectWorld 看一下这个系统设计有没有架构风险。
```

预期会选择：`perfectworld-plan`

### 调试修复

```text
用 PerfectWorld 查这个 bug，先复现，再找根因，最后修复。
```

预期会选择：`perfectworld-investigate`

### QA 测试

```text
用 PerfectWorld QA localhost:3000，发现问题可以直接修。
```

预期会选择：`perfectworld-qa`

### 只报告不修改

```text
用 PerfectWorld 只做 QA 报告，不要改代码。
```

预期会选择：`perfectworld-qa-only`

### 发布

```text
用 PerfectWorld 帮我准备发布，检查风险、文档、PR 和上线后验证。
```

预期会选择：`perfectworld-release`

## 本地开发和验证

这个仓库是一个 Codex marketplace 仓库，关键结构如下：

```text
.agents/plugins/marketplace.json
plugins/perfectworld/.codex-plugin/plugin.json
plugins/perfectworld/skills/
plugins/perfectworld/assets/
plugins/ue-perfectworld/.codex-plugin/plugin.json
plugins/ue-perfectworld/skills/
plugins/ue-perfectworld/references/
plugins/ue-perfectworld/assets/
scripts/publish-github.ps1
```

如果你 clone 了仓库，可以在仓库根目录添加本地 marketplace，然后按需要选择一个插件安装：

```powershell
codex plugin marketplace add .
codex plugin add perfectworld@perfectworld
codex plugin add ue-perfectworld@perfectworld
```

上面两个 `plugin add` 命令是两个可选项，不要求同时执行。

插件验证命令：

```powershell
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\perfectworld
python "$HOME\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .\plugins\ue-perfectworld
```

单个 skill 验证命令：

```powershell
python "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\plugins\perfectworld\skills\perfectworld-router
```

## FAQ

### `perfectworld` 和 `ue-perfectworld` 有什么区别？

`perfectworld` 覆盖通用产品开发全流程；`ue-perfectworld` 专注 Unreal Engine，并提供默认只读、项目惯例发现、完整教学代码、全面简洁的 `//` 注释和最终复杂度自审。两个插件可以独立安装。

### 怎样只安装 UE PerfectWorld？

先执行 `codex plugin marketplace add 91pao/PerfectWorld` 添加插件来源，再执行
`codex plugin add ue-perfectworld@perfectworld`。不要执行
`codex plugin add perfectworld@perfectworld`，就不会安装通用 PerfectWorld。

### UE PerfectWorld 是 Unreal Engine 的 `.uplugin` 吗？

不是。它是 Codex 插件，只决定 Codex 处理 UE 项目时使用的工作流和工程规则，不会被复制到
UE 项目的 `Plugins` 目录，也不会进入游戏运行时或最终包体。

### UE PerfectWorld 会默认修改我的 UE 项目吗？

不会。它默认只读取和分析项目，并在对话中给出教学实现。只有用户明确要求修改文件、应用补丁
或直接写入工作区时，才会进入直接实现模式。

### PerfectWorld 会自动选角色吗？

会。你可以直接说需求，也可以明确说“用 PerfectWorld”。插件里的 router 和每个角色都会要求 Codex 在每一轮重新判断是否需要切换角色。

### 我必须记住 23 个角色名吗？

不用。正常情况下说自然语言即可，比如“帮我查 bug”“帮我 QA”“帮我准备发布”。角色名主要用于调试、精确指定和文档说明。

### QA 是做什么的？

QA 是质量保证。`perfectworld-qa` 会像测试工程师一样检查功能是否真的能用、页面是否可操作、是否有明显 bug，并在允许时修复问题。`perfectworld-qa-only` 只报告问题，不改代码。

### 为什么有 QA 和 QA-only？

因为有些场景你只想要验收报告，不希望 Codex 动代码；有些场景你希望发现问题后直接修。两个角色分开可以减少误操作。

### PerfectWorld 能覆盖所有开发流程吗？

它覆盖的是完整产品开发流程的主要环节：产品、规格、架构、实现、调试、审查、测试、设计、安全、发布、文档、复盘和维护。具体项目仍然需要你提供目标、约束、代码仓库和验收标准。

### 这个插件会替我自动发布生产环境吗？

不会默认做高风险操作。发布角色会检查、准备、说明风险，并在需要执行真实部署、推送、删除、迁移等操作时遵守 Codex 的安全边界。

## License

MIT
