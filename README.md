# PerfectWorld Codex Plugin

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
- 插件 ID: `perfectworld`
- Marketplace 名称: `perfectworld`
- 开发者: `Liutianyuan / PerfectWorld`
- 官网: <https://games.wanmei.com/>

## 安装

在 Codex CLI 中添加这个 marketplace：

```powershell
codex plugin marketplace add 91pao/PerfectWorld
```

然后安装插件：

```powershell
codex plugin add perfectworld@perfectworld
```

安装完成后，建议开启一个新的 Codex 线程，让 Codex 重新加载插件技能。

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
scripts/publish-github.ps1
```

如果你 clone 了仓库，可以在仓库根目录本地测试：

```powershell
codex plugin marketplace add .
codex plugin add perfectworld@perfectworld
```

插件验证命令：

```powershell
python C:\Users\DJDJDJmax\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .\plugins\perfectworld
```

单个 skill 验证命令：

```powershell
python C:\Users\DJDJDJmax\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\plugins\perfectworld\skills\perfectworld-router
```

## 不依赖什么

PerfectWorld 是 Codex-native 改写版本，正常使用不要求：

- Claude slash commands
- Claude `allowed-tools`
- Claude hooks
- `~/.claude`
- Bun
- Git
- 上游浏览器守护进程

如果需要网页 QA 或截图，优先使用 Codex Browser 插件能力。

## 发布和维护

推荐使用 Git + SSH 长期维护，不需要反复创建或发送 GitHub token：

```powershell
.\scripts\publish-git.ps1 `
  -Message "Optimize PerfectWorld execution" `
  -Summary "减少中间轮次测试和上下文消耗"
```

脚本会先同步远程、自动更新 `CHANGELOG.md`、暂存当前改动、创建提交并推送到 `main`。没有实际改动时不会制造更新日志或空提交；推送中断后再次运行也不会重复写相同记录。首次使用前需要把本机 SSH 公钥添加到 GitHub，并确保仓库 remote 指向 `git@github.com:91pao/PerfectWorld.git`。

如果当前机器没有安装 `git`，可以用内置脚本通过 GitHub API 发布：

```powershell
$env:GITHUB_TOKEN = "你的 GitHub token"
.\scripts\publish-github.ps1 -Owner 91pao -Repo PerfectWorld
```

token 权限建议使用 Fine-grained token，并只给目标仓库：

```text
Repository access:
  Only select repositories -> 91pao/PerfectWorld

Repository permissions:
  Contents: Read and write
  Metadata: Read-only
```

不要把 token 写进仓库、README、issue 或聊天记录。发布完成后，如果 token 曾经暴露，建议立刻 revoke。

## FAQ

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
