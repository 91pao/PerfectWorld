# UE Comment And Log Rules

## Comment Principles

- Comments are for humans scanning quickly. Target reader: a programmer who has never seen this code and should grasp what each block does at a glance, not after study.
- Comments state what the code cannot: intent, contract, ownership, units, and failure behavior. They never narrate syntax.
- Comments describe standing behavior and contracts of the code as it exists now. They never narrate the change that introduced them — change rationale belongs in the review response or commit message, not in the code. A comment like `// 含 Direct，一键检查即全图重刷` narrates a past decision; `// 全部点刷新圈色` describes current behavior.
- Comments and modification markers must not reference task IDs, ticket numbers, phase names, or project-management artifacts. These are workflow labels, not code documentation.
- Use `//` line comments exclusively. Do not use `/* */` or `/** */` block comments.
- Do not end a comment with 句号 (。) or other sentence-ending punctuation. Separate clauses with `；` when needed.
- Be concise but never empty: `// 处理数据` says nothing; `// 按 FX 表行 ID 查池组件，查不到走兜底` says the right amount.
- Prefer deleting a comment over maintaining a stale one. A wrong comment is worse than no comment: it poisons every later reader and every later agent investigation.

## Distribute Comments Inside The Function

- In a new or meaningfully changed multi-step function, add a concise one-line `//` comment before each meaningful logical step — validation, branch, loop purpose, async binding, state transition, or cleanup — so its execution is easy to scan.
- Do not add comments to untouched code just to make the surrounding function look uniformly documented. Do not narrate obvious assignments, calls, or control flow; the comment must explain intent, a contract, ownership, or a non-obvious reason.
- Keep comments to one line by default. A multi-line comment is only acceptable for a genuinely complex contract that cannot be split into short notes, such as network authority, replication edge cases, or an engine workaround.
- Do not open a function (or any single spot) with a multi-line comment block that tries to explain everything up front. Long blocks get skipped, and then the code has no guidance inside.
- Scannable order: a reader moving through the function should be able to reconstruct the execution logic from the one-line comments alone.

## Declaration And Definition Comments

- Add a purpose comment to a new or meaningfully changed function only when its contract or role is not clear from its name and signature. Do not add duplicate purpose comments above both declaration and definition by default.
- For `UFUNCTION`s, a needed header comment doubles as the Blueprint editor tooltip and must describe exposed behavior for designers.
- Do not edit comments on untouched declarations or definitions merely to satisfy a blanket comment rule.

## What To Comment

- Give a new or meaningfully changed class, struct, function, or important property a one-line purpose comment when its role or contract is not already clear from its name and surrounding code.
- State units and valid ranges on numeric configuration and parameters: seconds versus milliseconds, clamped ranges, and sentinel values such as `0`, `-1`, or `INDEX_NONE`.
- Wherever a call starts async work, state the completion expectation: which callback fires, and what the caller does on failure or cancellation.
- Comment critical validation, state transitions, delegate lifetime, replication handling, asset loading, and non-obvious engine calls at the exact line they occur.
- Explain why a branch or engine pattern is necessary instead of narrating what the syntax does.

## Blueprint-Exposed API Comments

- A comment directly above a `UPROPERTY` or `UFUNCTION` becomes the designer-facing tooltip in the Blueprint editor. Write exposed-API comments for designers, not for programmers.
- For exposed properties: what it configures, its units, its valid range, and how the default value behaves.
- For exposed functions: what it does, when it is safe to call, and its failure behavior — not the implementation route.

## Modification Markers

- At the first point in each task that requires adding or changing code comments or markers, ask the user who the author is. Do not infer the author from previous tasks, repository history, or a default. Once confirmed, use that author marker consistently for this task.
- Wrap every code block added or modified in this task with `// <作者> begin: <用一行说明这段改动>` on the line above and `// <作者> end` on the line below. The begin line is the explanation for the marked change; do not add a second comment immediately below it that repeats the same explanation.
- Keep marker boundaries limited to code actually added or changed. Do not add markers around untouched code or comments just to provide context, and do not change another author's marker range.
- Preserve existing comments and marker blocks owned by other authors. Do not add this task's author markers to their unchanged code or comments. If an existing comment has become semantically wrong because of this change, edit only the necessary comment text and preserve its original marker boundaries.
- If this task changes code inside another author's marker range, preserve that author's begin/end lines and scope exactly; add a narrow pair using the confirmed author only around the code changed by this task.
- Each logical block inside a marked region may still have its own concise one-line explanation when needed to distinguish a non-obvious step. Do not repeat the begin-line explanation immediately below the marker.
- Fuse adjacent or nearby regions owned by the confirmed author when they describe one cohesive change and can be combined without pulling unrelated untouched code or another author's region into the marker. Never merge across another author's marker block.
- Example:

```cpp
// <作者> begin: 重置激光资源回调绑定状态并同步处理缓存命中
bLaserResourceReadyCallbackBound = false;

// 池组件可能已缓存资源，同步检查命中则直接激活
if (PoolComponent->IsResourceReady())
{
	ActivateLaserImmediately();
	return;
}
// <作者> end
```

- The marker summary states what the change does in one line; it is not a changelog or a place for background story.
- Do not add other author tags, dates, signatures, or banners beyond this format.
- When marked code is later removed or migrated, remove its markers too. Do not leave empty or duplicated pairs. A narrowly scoped pair using this task's confirmed author inside another author's unchanged range is allowed only when this task actually changes code there and preserving the outer range requires it.
- Markers are territory fences, not logical sections: one contiguous run of this task's code gets ONE begin/end pair, no matter how many logical steps it contains. Sub-explanations inside the region are plain `//` comments; nested `ppz` pairs are used only for the foreign-range exception above.

```cpp
// <作者> begin: 增援按盒子引用链取点并引入 Map Check 消息支持
#include "AIZoneBox.h"

#include "Logging/MessageLog.h"
// <作者> end
```

- Replace `<作者>` with the author confirmed for this task. The marker description is required and always a short, single-line explanation, including for include changes.

## Language And Encoding

- Match the nearby comment language: a Chinese-commented module stays Chinese, an English module stays English. Do not mix languages inside one comment block.
- Use the project's established domain terminology; do not introduce synonyms for concepts the team already names.
- When writing or editing Chinese comments, follow the UTF-8 handling rules in `ue-edit-safety.md`; never let a wrongly decoded comment reach the file.

## What Not To Comment

- Do not repeat clear symbol names, types, signatures, assignments, or obvious control flow.
- Do not use comments to excuse indirect code; simplify the implementation first.
- Do not place operational instructions, unresolved assumptions, placeholders, or TODOs inside delivered code. Route genuine future work to the task tracker or handoff document instead.
- Do not keep commented-out code as a backup after a rewrite or migration. Delete it: version control preserves history, and stale commented code misleads later readers and agents.
- Do not leave a workaround uncommented or half-commented: a workaround comment must name the blocking cause and the condition under which the workaround can be removed.

## Comment Examples

Prefer this: changed code has one concise marker using the author confirmed for this task, logical steps have one-line explanations, no duplicate function-purpose comments, no trailing periods.

```cpp
// GFBeaconLaserFxComponent.cpp
// <作者> begin: 按句柄校验资源回调并安全激活激光
void UGFBeaconLaserFxComponent::HandleLaserResourceReady(int32 SpawnHandle)
{
	// 校验句柄，防止迟到回调写复用后的组件
	if (SpawnHandle != ActiveSpawnHandle)
	{
		return;
	}

	// 先摆 Tail 再激活，避免首帧闪现全长激光
	UpdateTailSocketTransform();
	NiagaraComponent->Activate();
}
// <作者> end
```

Not this: a top-of-function block that narrates everything, `/** */` style, trailing periods.

```cpp
/**
 * 这个函数用来处理资源就绪。首先会校验句柄，
 * 因为句柄可能已经失效了。校验通过之后，会先
 * 更新尾部的位置，然后再激活特效组件。
 */
void HandleLaserResourceReady(int32 SpawnHandle) { ... }
```

## Direct Project Edits

- Follow the rules above for new or meaningfully changed code; nearby comment density does not justify adding comments to untouched code.
- Preserve useful comments and update comments made inaccurate by the code change.
- Synchronize comments after every correctness or simplicity rewrite; a refactor that leaves old comments in place silently poisons later evidence.

## Logs And User Feedback

- Follow the project's existing log categories, verbosity levels, macros, and user-facing notification path.
- Before adding, removing, or changing a diagnostic, inspect maintained same-domain code with the same responsibility and lifecycle. Match how it handles equivalent player, HUD, owner, optional widget, callback parameter, table row, asset, and runtime-instance failures.
- Classify each failure before deciding its behavior: expected optional or transient absence, broken authoring or configuration contract, rejected gameplay action, or unexpected invariant violation. Use the current project's established handling for that class.
- Do not impose a universal rule that every defensive return must log or that every failure must stay silent.
- Keep routine optional-widget checks and expected owner or UI availability checks quiet when the closest production path uses a conditional or silent return.
- Reserve diagnostics for failures that the closest production path treats as actionable, and report them at the owning boundary instead of repeating the same failure through every helper and child widget.
- Log rejected conditions when silence would make a real defect difficult to diagnose.
- Include the operation and relevant non-sensitive identifiers needed for diagnosis.
- Do not expose secrets, credentials, personal data, or unnecessary server internals.
- Avoid noisy logs in ticks, replication callbacks, animation updates, and other high-frequency paths.
- Keep expected defensive failures quiet only when nearby maintained code follows the same convention.
- Never restructure ownership, lookup, traversal, or navigation merely to reduce logging volume.
