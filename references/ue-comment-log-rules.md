# UE Comment And Log Rules

## Comment Principles

- Comments are for humans scanning quickly. Target reader: a programmer who has never seen this code and should grasp what each block does at a glance, not after study.
- Comments state what the code cannot: intent, contract, ownership, units, and failure behavior. They never narrate syntax.
- Use `//` line comments exclusively. Do not use `/* */` or `/** */` block comments.
- Do not end a comment with 句号 (。) or other sentence-ending punctuation. Separate clauses with `；` when needed.
- Be concise but never empty: `// 处理数据` says nothing; `// 按 FX 表行 ID 查池组件，查不到走兜底` says the right amount.
- Prefer deleting a comment over maintaining a stale one. A wrong comment is worse than no comment: it poisons every later reader and every later agent investigation.

## Distribute Comments Inside The Function

- A function body made of several logical steps must carry a one-line `//` comment on each block — validation, branch, loop with purpose, async binding, state transition, cleanup — so the function reads top-to-bottom like a checklist. Only trivially short or self-evident bodies (such as one-line accessors) may go without internal comments.
- Do not open a function (or any single spot) with a multi-line comment block that tries to explain everything up front. Long blocks get skipped, and then the code has no guidance inside.
- A multi-line comment is acceptable only when a genuinely complex contract cannot be split (network authority, replication edge cases, engine workaround), and it must stay as short as possible.
- Scannable order: a reader moving through the function should be able to reconstruct the execution logic from the one-line comments alone.

## Declaration And Definition Comments

- Every function gets its one-line purpose comment at both sites: above the declaration in the header and above the implementation in the `.cpp`. One without the other is incomplete.
- The two comments must be identical: write the text once and copy it verbatim. If the purpose changes, change both sites together. Divergent header and source comments mislead readers about which one is current.
- Functions declared and defined in the same `.cpp` (file-local helpers) carry the comment once, above the definition.
- For `UFUNCTION`s the header comment doubles as the Blueprint editor tooltip, so the shared text must read well for both programmers and designers.

## What To Comment

- Give every added or meaningfully changed class, struct, function, and important property a one-line purpose comment.
- State units and valid ranges on numeric configuration and parameters: seconds versus milliseconds, clamped ranges, and sentinel values such as `0`, `-1`, or `INDEX_NONE`.
- Wherever a call starts async work, state the completion expectation: which callback fires, and what the caller does on failure or cancellation.
- Comment critical validation, state transitions, delegate lifetime, replication handling, asset loading, and non-obvious engine calls at the exact line they occur.
- Explain why a branch or engine pattern is necessary instead of narrating what the syntax does.

## Blueprint-Exposed API Comments

- A comment directly above a `UPROPERTY` or `UFUNCTION` becomes the designer-facing tooltip in the Blueprint editor. Write exposed-API comments for designers, not for programmers.
- For exposed properties: what it configures, its units, its valid range, and how the default value behaves.
- For exposed functions: what it does, when it is safe to call, and its failure behavior — not the implementation route.

## Modification Markers

- Wrap every modified or added block with the team marker format: `// <作者> begin: <一句话说明本次改动>` on the line above, `// <作者> end` on the line below. Example:

```cpp
// ppz begin: 激光改为资源就绪回调驱动，去掉 Tick 轮询
// 每次启动重置绑定状态，防止上一轮残留委托生效
bLaserResourceReadyCallbackBound = false;

// 池组件可能已缓存资源，同步检查命中则直接激活，不等异步回调
if (PoolComponent->IsResourceReady())
{
	ActivateLaserImmediately();
	return;
}
// ppz end
```

- The marker summary states what the change does in one line; it is not a changelog or a place for background story.
- Do not add other author tags, dates, signatures, or banners beyond this format.
- When marked code is later removed or migrated, remove its markers too. Do not leave empty, duplicated, or nested marker pairs.

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

Prefer this: declaration and implementation carry the identical comment, each logic block inside gets a one-liner, no trailing periods.

```cpp
// GFBeaconLaserFxComponent.h
// 资源就绪回调：句柄失效或组件已回池时直接返回
void HandleLaserResourceReady(int32 SpawnHandle);
```

```cpp
// GFBeaconLaserFxComponent.cpp —— 注释与声明处一字不差
// 资源就绪回调：句柄失效或组件已回池时直接返回
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

- Match nearby comment density and formatting: a sparsely commented production file should not gain banner comments; a heavily commented module should not gain undocumented code.
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
