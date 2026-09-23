# UE Final Self Review

Run this as a blocking gate before delivering code, direct edits, or a code-review conclusion.

## Correctness

- Trace the primary success path and important failure paths end to end
- Confirm the result implements the user's latest requirement and hard scope, and contains no mechanism retained only for a superseded requirement
- Confirm each required behavior maps to a verified project capability; when requirement and allowed scope conflict, require the exact conflict, strict implementation cost, and closest project-native alternative before implementation
- Confirm the target type, full base-class hierarchy, inherited editor properties, Blueprint Designer configuration, and responsibility-compatible tables or routers were inspected before accepting new UI interaction or navigation code
- Confirm every selected action is classified as `reuse`, `configure`, `extend`, or `create`, and reject `extend` or `create` while a compatible existing capability remains unchecked rather than disproven
- Recheck every project-specific symbol and assumption against the current workspace
- Recheck every introduced mechanism against the responsibility evidence matrix; one similar feature is insufficient when UI composition, navigation, state, diagnostics, or lifecycle use different project owners
- For non-trivial cross-system work, verify the evidence gate is complete: authoritative data, runtime lifecycle, trigger, read path, persistence boundary, and cleanup path all have project evidence
- Reject any solution that infers one responsibility from another, such as deriving message creation from display aggregation or deriving cleanup from a trigger condition
- Confirm selected precedents have active production evidence and compatible ownership, lifecycle, authority, and responsibility
- Recheck reflection declarations, includes, module dependencies, object lifetime, null handling, delegate cleanup, threading, assets, configuration, persistence, and network rules where applicable
- Audit each new guard and diagnostic against the closest maintained same-responsibility path. Remove invented logging policies, repeated boundary logs, and inconsistent HUD, player, optional-widget, or callback handling
- Confirm bug fixes correct the root cause instead of hiding it with fallback state, retries, delays, or silent returns
- Distinguish proven guarantees from mitigations and unresolved assumptions
- For shared user-visible state, confirm the producer and persistence owner, acknowledgement owner, and display-only consumers are distinct and correct
- If two surfaces are required to stay identical, confirm they resolve the same authoritative identity instead of maintaining synchronized copies or proxy state
- Reject new red-point identities, save data, RPCs, proxy state, delegates, managers, or lifecycle overrides when the requirement is only navigation or another presentation of an existing state
- Trace each participating mechanism by execution stage and reject both missing stages and parallel paths that perform the same responsibility
- Cross-check code, factory registration, DataAssets, DataTables, GameplayTags, Blueprint bindings, UI extension or platform overrides, external payloads, persistence, and cleanup as one final contract

## Interruption And Latecomer Audit

- For changes touching budgets, transactions, lifecycle, cancellation, timers, leases, or multi-stage asynchronous chains, enumerate interruption entries by searching every Stop, Cancel, Reset, Abort, Close, EndPlay, and TearDown call site, plus framework-initiated closes, timeouts, repeat activation, and owner invalidation — never from memory
- Cross each entry with each lifecycle stage and state what survives the interrupt: transaction state, lease, timer, flags, binding or weak references, budget occupancy. A cell with no answer is a defect, not a blank
- Hunt latecomers and flag lifecycles explicitly: when an interrupt lands at stage N, name what stops the stage N+1 startup callback; a cancel flag cleared unconditionally at registration reopens the door a waiting-window cancellation closed
- Positive confirmation (compiles, probes zero, call sites alive) does not cover this class; an interruption path without a runtime trigger stays unverified in the conclusion

## Maintainability

- Compare the result with the smallest complete project-consistent implementation
- Reopen the requirement-and-capability fit gate if complexity grew through another file, shared integration point, state owner, persistence path, RPC, cache, delegate, timer, manager, or configuration source
- Require every added file, class, function, field, delegate, override, configuration item, and abstraction to have a current requirement and real consumer
- Remove duplicate data authority, unused state, empty lifecycle overrides, speculative extension points, one-use wrappers, generic managers, compatibility branches, and parallel execution paths
- If a later discovery exposes an existing capability, remove all code and configuration introduced only to compensate for its previously assumed absence
- Keep one authoritative source for each tag, ID, state, and configuration value
- Apply the change test: a normal requirement change has an obvious bounded edit location
- Apply the deletion test: the feature can be removed without hidden registration, duplicate state, or undocumented coupling
- Apply the no-chat test: a teammate can trace, modify, and remove the implementation without the generation conversation
- Rewrite avoidable overdesign before delivery; do not merely document it as a concern
- Compare the delivered file and asset list with the change-surface manifest; reject undeclared shared changes, stale fields from earlier designs, duplicated configuration, and dependencies incorrectly described as modifications
- Treat a visual variant as presentation unless a verified business rule requires a separate persisted or acknowledged state

## Delivery

- Correct every known in-scope defect before presenting complete code or finalizing direct edits
- Complete the status ledger required by the completion claim gate; no applicable responsibility or execution stage may remain implicit
- Match the conclusion to the highest verification level actually reached. Do not describe source review as compile, runtime, authority, persistence, cross-session, or cross-platform validation
- Block complete, ready, best, and no-findings claims while any required item is `disproven` or `unavailable`; either correct it or state the precise verification gap and narrow the conclusion
- If the evidence gate has a gap, remove any speculative implementation from the response and state the missing proof instead
- Ensure complete-code responses contain no pseudocode, ellipses, placeholders, TODOs, omitted branches, or unverified project symbols
- Keep comments concise, production-suitable, and synchronized with the final implementation
- Confirm source text was not modified through incorrectly decoded shell output
- Confirm no unrelated files or stable release flows changed
- State which compile, editor, automation, and packaging checks were run or skipped
- If repeated local fixes accumulated, apply the recovery gate in `ue-bugfix-discipline.md` before finalizing
- Include the final create, replace, configure, and reuse-only surface summary so the user can distinguish required work from existing project infrastructure

## Runtime Log Acceptance

- Write the failure-probe list with expected values before the run; a probe list written after the run is narration, not acceptance
- Trace one request GUID across subsystems — lease, budget reserve and commit and finalize, presentation, settlement — and check closure, interval sanity, and terminal-state semantics against the design
- Judge warnings by tag census against older logs before calling a regression: a pattern present in history is not this change's defect

## Claim Audit（共享占用三向审计）

触发条件：本次改动给某个共享资源（点位/标志/租约/句柄/预算槽）新增了持有者（写入方）或门禁消费者（读它做拒绝条件）。三问缺一即回到评审台：

1. 方向矩阵：列出"每个持有者 × 每个后来者"的完整组合，逐格回答"后来者看得见持有吗"。只验证自己新代码单方向的占用（如"任务占用→增援不借"）而漏掉反向（"增援占用→任务能否激活"），就是占用反转缺口。审查视角必须从共享资源向外（谁会来抢这个资源），不是从新代码向内（我的门逻辑对不对）。
2. 最坏存活时间：消费的每个外部标志/锁，grep 其全部置位与清零点，回答"最坏能阻塞多久"。清零只发生在"下一次同类请求"或从不发生的，是无界阻塞，按缺陷处理。"不许改那边的代码"不等于不用深究——恰恰是消费别家生命周期的标志时最需要审计置位/清零全集，因为坏了也不能在那边修。
3. 接缝优先：未改动的旧路径与新逻辑的交点（既有投放模式、取消/清理机制、旧入口），审计精力分配要高于自己的新代码——新代码你想过一遍，接缝一遍都没想过。没有被任何用例走过的旧路径视为未审计：测试场景照心智模型搭建，等于把确认偏误焊进用例设计；Force 注入式用例验证门谓词，不覆盖真实生命周期。

事故案例（工单3 增援借用，S5 自评 P1/P2 清零后复议被抓回两处）：①借用使点位持有位置租约，但只验了"任务占用→增援不借"，未问"增援占用→任务激活"——Direct 投放走 LegacyPassthrough 全程不查位置租约，任务可在增援潜艇占点期间原地刷怪（方向矩阵缺格）；②借用门消费工单2 的取消闩，该闩清零只发生在下一次任务请求绑定——最后一波任务取消后共享点永久不可再借（无界阻塞）。修复：激活门加租约预检 + 借用门改为"闩住且请求未终态"。

验收口径：方向矩阵逐格有答案；每个被消费的外部标志留下"置位点/清零点/最坏时长"三行记录；至少一条自动化或 PIE 用例穿过真实生命周期（如真实取消流程之后借用），并在验证记录中点名。
