# UE PerfectWorld

让 UE 项目的需求、证据与实现，进入一套可检查、可交接的 Codex 工作流。

<p align="center">
  <a href="https://github.com/91pao/PerfectWorld/tags"><img alt="Latest version tag" src="https://img.shields.io/github/v/tag/91pao/PerfectWorld?style=flat-square&label=version"></a>
  <a href="https://github.com/91pao/PerfectWorld/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/91pao/PerfectWorld?style=flat-square&color=e8b86d"></a>
  <a href="https://github.com/91pao/PerfectWorld/blob/main/LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/91pao/PerfectWorld?style=flat-square"></a>
  <img alt="Codex plugin" src="https://img.shields.io/badge/Codex-plugin-7387ff?style=flat-square">
  <img alt="Unreal Engine 5" src="https://img.shields.io/badge/Unreal%20Engine-5-20232a?style=flat-square">
</p>

<p align="center">
  <img src="assets/overview.svg" alt="UE PerfectWorld 工作示意：从 UE 项目代码、蓝图和日志出发，经过 Codex 技能工作流与用户批准，形成证据、变更规格、验证和交付记录" width="100%">
</p>

<p align="center">
  <a href="#快速上手"><strong>快速上手</strong></a> &nbsp; · &nbsp;
  <a href="#适用任务">适用任务</a> &nbsp; · &nbsp;
  <a href="#s0-s6-阶段门禁">S0-S6 工作流</a> &nbsp; · &nbsp;
  <a href="#常见问题">常见问题</a> &nbsp; · &nbsp;
  <a href="https://github.com/91pao/PerfectWorld/issues">反馈问题</a>
</p>

UE PerfectWorld 是给 **Codex** 使用的 Unreal Engine 项目工作流插件，面向 UE5 的 C++、蓝图及两者协作场景。它提供一组专用技能和项目规则，帮助 Codex 先读懂当前项目，再提出有依据的改动，并把验证与交接结果说清楚。

**它不是 Unreal Editor 扩展，也不包含 RAG 服务或索引器。** 插件不会因为安装就自动扫描或修改 UE 项目；项目文件仍按当前任务的授权和 S0-S6 门禁处理。

## 适用任务

| 你正在处理 | 可以这样开始 | 主要结果 |
| --- | --- | --- |
| 新功能或系统改动 | `用 UE PerfectWorld 先分析这个功能的现有实现和改动方案` | 项目证据、范围说明、S2 变更规格 |
| 已有报错或运行异常 | `用 UE PerfectWorld 根据这段日志排查根因，先不要改文件` | 根因分析、证据链、尚缺的信息 |
| 已批准方案的实现 | `按刚批准的 S2 落点表实现，并按要求记录验证` | 限定范围内的改动、自审与验证记录 |
| 已有代码或补丁审查 | `用 UE PerfectWorld 审查当前 diff，按风险列出问题` | 分级审查发现与复验建议 |
| C++ 与蓝图协作 | `确认这个行为由 C++、蓝图还是两者共同负责，再分析改动` | 所有权、资产引用和交接约束 |
| 开发文档或交接 | `根据本次已完成改动整理 UE 开发文档` | 与实际改动和验证情况一致的交接文档 |

这些示例是自然语言入口，不是必须逐字使用的命令。任务涉及项目变更时，仍遵循完整的 S0-S6 流程。

## 快速上手

在已安装 Codex CLI 的环境中添加 marketplace 并安装插件：

```bash
codex plugin marketplace add 91pao/PerfectWorld
codex plugin add ue-perfectworld@perfectworld
codex plugin list
```

更新已安装版本：

```bash
codex plugin marketplace upgrade perfectworld
codex plugin add ue-perfectworld@perfectworld
codex plugin list
```

安装或更新后重启 Codex，或新开一个对话以加载技能。首次配置时可以运行 `ue-setup`：它会检查当前工作区及其父目录中的 `.uproject`，并说明可选 RAG 工具是否可用；它不会创建索引或修改项目。

安装完成后，在包含 UE 项目的工作区中直接描述任务即可。例如：

```text
用 UE PerfectWorld 帮我分析这个交互功能。
先确认现有 C++ 和蓝图分别负责什么，给出证据和变更规格，等我批准后再实现。
```

## S0-S6 阶段门禁

以项目变更为终点的任务按 S0 到 S6 逐阶段推进。阶段可以按任务规模简写，但不能跳过、合并或绕过门禁。

<p align="center">
  <img src="assets/s0-s6.svg" alt="S0 到 S6 阶段门禁：需求接入、证据底座、变更规格、实现、验证、对抗评审、交付；每阶段都列出产出与停止条件" width="100%">
</p>

| 阶段 | 处理内容 | 关键产物或停止条件 |
| --- | --- | --- |
| **S0 需求接入** | 明确目标、范围、非目标和成功标准 | 理解卡；问题未澄清时先停下确认 |
| **S1 证据底座** | 对照当前项目文件和可信先例核实需求 | 证据矩阵；结论标明 `path:line` 或证据缺口 |
| **S2 变更规格** | 明确改动文件、落点、理由及不改动范围 | 变更清单；**取得用户明确批准后才进入实现** |
| **S3 实现** | 按已批准范围小步修改并自审 | 改动集、自审记录；随后停在验证阶段 |
| **S4 验证** | 先列探针和预期结果，再执行可用验证 | 如实记录已通过、未运行和受限项目 |
| **S5 对抗评审** | 检查需求符合性、项目一致性、生命周期和过度设计 | 按严重度列出发现；未解决的 P1/P2 阻断交付 |
| **S6 交付** | 整理开发文档、验证证据和交付边界 | 对账各阶段产物；提交或推送仍需用户逐次授权 |

## 技能一览

| 技能 | 适用场景 | 工作边界 |
| --- | --- | --- |
| `ue-investigate` | 已有报错、日志或可复现故障 | 只读定位；不把诊断自动扩展成修复 |
| `ue-draft` | 方案、变更规格或实现范围仍需澄清 | 只读；输出 S0-S2 所需内容 |
| `ue-implement` | S2 落点表已获批准，且用户明确授权修改 | 只改批准范围；不替代验证和评审 |
| `ue-review` | 审查已有 diff、补丁或已应用改动 | 只审查，不修改文件 |
| `ue-blueprint` | 蓝图资产、编辑器配置或 C++/蓝图交接 | 按需协作；由主工作流负责规划、实现或审查 |
| `ue-dev-doc` | 一次改动完成后需要开发或交接文档 | 依据真实改动和验证记录，不推测补写 |
| `ue-setup` | 初次安装后了解工作区与可选工具 | 只检查，不配置 RAG、不改项目 |

## 工作边界

- **先有项目证据，再给结论。** 项目相关判断要回到源码、配置或资产引用核实；找不到就说明缺口。
- **批准规格后才进入实现。** 用户要求“帮我改”本身不替代 S2 变更规格批准。
- **验证结果不夸大。** 未运行的编译、PIE、自动化测试或打包验证会明确标为未验证。
- **提交与推送单独确认。** 文件编辑授权不自动包含版本控制操作授权。
- **UE 项目按用户授权处理。** 不因插件安装而扫描无关目录、修改工程设置或执行完整构建。

## RAG（可选）

UE PerfectWorld 不附带 RAG 服务、索引器或向量数据库。只有当前 Codex 环境另行提供 `ue_rag_*` 工具时，技能才会使用它们辅助发现候选文件。

- RAG 结果用于查找线索，不作为代码、蓝图、生命周期、联网行为或清理逻辑的最终证据。
- 候选内容仍需通过当前项目文件直接核实。
- 没有 RAG 工具时，直接使用 `rg` 和源码读取；不会假称检索过索引。

## 常见问题

<details>
  <summary><strong>这是安装在 Unreal Editor 里的插件吗？</strong></summary>

不是。UE PerfectWorld 是安装在 Codex 中的工作流插件，提供 UE 开发相关技能和规则；它不会向 Unreal Engine 工程添加 `.uplugin` 或 C++ 模块。

</details>

<details>
  <summary><strong>安装后会自动修改我的 UE 项目吗？</strong></summary>

不会。任务开始时先检查需求和项目证据；需要变更的任务必须先产出 S2 规格并获得明确批准，再按批准范围实现。安装插件本身不会修改项目。

</details>

<details>
  <summary><strong>必须配置 RAG 才能使用吗？</strong></summary>

不需要。RAG 是可选的外部检索工具；没有 `ue_rag_*` 工具时，工作流使用 `rg` 和项目文件直接读取。

</details>

<details>
  <summary><strong>我应该从哪个技能开始？</strong></summary>

直接描述当前任务即可：报错和日志走 `ue-investigate`，新功能方案走 `ue-draft`，获批后的代码变更走 `ue-implement`，已有 diff 走 `ue-review`。蓝图协作和文档技能会在任务需要时配合。

</details>

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `skills/` | Codex 可调用的 UE 工作流技能 |
| `references/` | UE 项目分析、代码边界、自审和 RAG 集成规则 |
| `assets/` | 插件图标及 README 信息图 |
| `evals/` | 技能路由人工回归用例及执行说明 |
| `tests/validate_plugin.py` | 插件清单、技能引用与 S0-S6 文档的静态校验 |
| `CHANGELOG.md` | 按版本整理的更新记录 |

路由用例是人工提示词评测，不是自动正确性证明。具体范围见 [evals/README.md](evals/README.md)。

## 版本与反馈

- 当前插件版本：`0.6.1`；更新内容见 [CHANGELOG.md](CHANGELOG.md)。
- 发现问题或希望补充使用场景：请到 [GitHub Issues](https://github.com/91pao/PerfectWorld/issues) 提交。附上复现步骤和相关版本号前，请先移除项目机密、访问令牌及个人信息。
- 许可：[MIT](LICENSE)。
