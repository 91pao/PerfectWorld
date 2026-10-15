# UE PerfectWorld

Unreal Engine 项目的阶段门禁开发工作流插件。适用于任何 UE5 项目的 C++ / 蓝图混合开发。

<p>
  <a href="https://github.com/91pao/PerfectWorld/tags"><img alt="Latest version tag" src="https://img.shields.io/github/v/tag/91pao/PerfectWorld?style=flat-square&label=version"></a>
  <a href="https://github.com/91pao/PerfectWorld/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/91pao/PerfectWorld?style=flat-square&color=e8b86d"></a>
  <a href="https://github.com/91pao/PerfectWorld/blob/main/LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/91pao/PerfectWorld?style=flat-square"></a>
  <img alt="Codex plugin" src="https://img.shields.io/badge/Codex-plugin-7387ff?style=flat-square">
  <img alt="Stage-gated workflow" src="https://img.shields.io/badge/workflow-S0%E2%80%93S6-4c9f70?style=flat-square">
</p>

<p align="center">
  <img src="assets/overview.svg" alt="UE PerfectWorld 项目总览图：证据优先、强门禁、UE 语境、可追溯交付，并通过 S0 到 S6 推进工作" width="100%">
</p>

UE PerfectWorld 的重点不是让模型“直接改代码”，而是把 UE 工作拆成可检查的阶段：先理解需求，核实项目证据，确认变更规格，再实现、验证、评审和交付。

## 安装

```bash
codex plugin marketplace add 91pao/PerfectWorld
codex plugin add ue-perfectworld@perfectworld
codex plugin list
```

更新已安装插件：

```bash
codex plugin marketplace upgrade perfectworld
codex plugin list
```

安装或更新后，重启 Codex 或新开对话以加载技能。插件安装后可运行 `ue-setup` 检查项目位置和可选工具。

## 技能路由

| 技能 | 何时使用 | 边界 |
| --- | --- | --- |
| `ue-investigate` | 已有报错、日志或可复现症状，需要只读定位根因 | 不用于新功能规划或已有改动审查 |
| `ue-draft` | 用户要方案、变更规格、可粘贴代码，或实现意图仍有歧义 | 只读；不替代故障根因排查 |
| `ue-implement` | S2 落点表已获批准，且用户明确授权修改 | 不接手未批准落点表的实现 |
| `ue-review` | 用户要求审查已有 diff、补丁或已应用改动 | 只审查，不修改文件 |
| `ue-blueprint` | 任务实际涉及蓝图资产、编辑器配置或 C++/蓝图交接 | 协作参考；主任务仍由规划、实现、排查或审查技能承接 |
| `ue-dev-doc` | 一次 UE 改动完成后，需要开发、交接或技术文档 | 不用于新功能方案 |

技能不需要在每轮对话重复角色口号；直接说明当前阶段和要处理的结果即可。

## 工作流概览

所有以项目变更为终点的任务，走 S0→S6 七阶段门禁：

<p align="center">
  <img src="assets/s0-s6.svg" alt="S0 到 S6 阶段门禁图：每一阶段都有产出物和停止条件，S2 是实现前最重的用户批准门禁" width="100%">
</p>

| 阶段 | 职责 | 产出物 | 门禁 |
| --- | --- | --- | --- |
| S0 需求接入 | 重述目标、范围、非目标 | 理解卡＋待答问题 | 用户确认理解 |
| S1 证据底座 | 逐点核实既有能力（path:line） | 证据矩阵 | 与 S0 共停 |
| S2 变更规格 | 落点表：改哪些文件、为什么、零改动证明 | 变更清单 | **用户批准（最重门禁）** |
| S3 实现 | 仅改清单内文件、小步可编译 | 代码集＋自审记录 | 停给 S4 |
| S4 验证 | 先写探针清单再跑 | 验证记录 | 用户看证据 |
| S5 对抗评审 | 按三轴审查＋占用审计 | 按严重度排序的发现 | P1/P2 清零 |
| S6 交付 | 开发文档＋单工单提交 | 文档＋提交 | 用户确认 |

## 技能

| 技能 | 职责 | 对应阶段 |
| --- | --- | --- |
| `ue-draft` | 只读方案与落点表 | S0-S2 |
| `ue-implement` | 按落点表实现代码 | S3 |
| `ue-review` | 三轴对抗评审 | S5 |
| `ue-investigate` | 根因排查（只读） | S0-S1 |
| `ue-blueprint` | 蓝图与 C++ 协作规则 | 全程 |
| `ue-dev-doc` | 开发文档撰写 | S6 |
| `ue-setup` | 首次安装后的项目与可选 RAG 检查 | 安装配置 |

## 核心规则

- **证据优先**：不动文件前每个需求点必须有项目内证据（path:line），缺口如实上报不编造
- **工作区只读**：未经用户明确授权不改项目文件；版本控制操作逐次征得同意
- **阻断性自审**：交付前必须通过 `ue-self-review`（含环境矩阵审计、Claim Audit 共享占用三向审计）
- **贴码门禁**：将要写入项目的代码，写前逐符号查证声明处、读实现处确认参数语义、include 照抄同模块先例
- **用户偏好覆盖**：用户明确表达的验证偏好（如 PIE 实测＋日志探针）覆盖插件默认推荐

## RAG（可选）

UE PerfectWorld 不包含 RAG 服务或索引器。只有当前 Codex 环境另行提供 `ue_rag_*` 工具时，技能才会使用 RAG：

- 先检查 `ue_rag_status`，再用有界查询找候选位置；索引缺失或过期时按已配置工具的能力处理。
- RAG 结果只用于发现候选，不是代码、蓝图、生命周期、联网行为或清理逻辑的证据；结论仍须回到项目文件直接核实。
- 如果没有 `ue_rag_*` 工具，直接使用 `rg` 和项目文件读取，不要假称已检索索引。

## 版本历史

见 [CHANGELOG.md](CHANGELOG.md)。

## 许可

MIT
