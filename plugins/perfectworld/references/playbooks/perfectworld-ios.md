# 完美世界 iOS 工程师 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## ios-qa

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Connects to a real iPhone via USB
CoreDevice IPv6 tunnel, reads Swift source to understand every screen, then
runs a vision-driven agent loop: screenshot  analyze  decide  act 
verify  repeat. All interaction happens via HTTP to an embedded
StateServer in the app under test. Optionally exposes the device over
Tailscale so remote agents (OpenClaw, Codex, any HTTP-capable agent) can
run iOS QA from anywhere without touching the hardware.
Use when asked to "ios qa", "test my iPhone app", "find bugs on the device",
or "qa the iOS app".

Voice triggers (speech-to-text aliases): "iOS quality check", "test the iPhone app", "run iOS QA".

## ios-fix

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Takes a bug found by perfectworld-ios-qa, reads the source,
writes the fix, rebuilds, redeploys, and verifies the fix on the real
device. Closes the loop: find bug  fix bug  confirm fix  zero human
intervention. Captures the pre-bug state snapshot as a regression test
fixture, so the bug can never recur silently.
Use when perfectworld-ios-qa reports a bug and you want it fixed automatically, or
when asked to "fix this iOS bug", "patch the iPhone app", or "auto-fix
the iOS issue".

Voice triggers (speech-to-text aliases): "fix the iOS bug", "patch the iPhone app", "auto-fix the iOS issue".

## ios-design-review

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Connects to a real
iPhone via the same StateServer as perfectworld-ios-qa, screenshots every screen,
evaluates against Apple HIG, DESIGN.md, and design best practices. Scores
each dimension 0-10 with "what would make it a 10" framing  mirrors
perfectworld-plan-design-review for browser. For plan-stage design review (before
implementation), use perfectworld-plan-design-review. For live web visual audits, use
perfectworld-design-review.
Use when asked to "review the iOS design", "audit the iPhone app's
visuals", or "design QA the iOS app".

Voice triggers (speech-to-text aliases): "review the iOS design", "audit the iPhone app's visuals", "design QA the iPhone app".

## ios-clean

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Cleans up StateServer, DebugOverlay, accessor codegen output, and
app-side hooks installed by perfectworld-ios-qa. This is a convenience wrapper 
the structural Release-build guard (Package.swift conditional + CI
swift build -c release check) is the safety-critical path.
Use when asked to "clean the iOS debug bridge", "remove DebugBridge",
or "strip the perfectworld iOS instrumentation".

Voice triggers (speech-to-text aliases): "clean the iOS debug bridge", "remove DebugBridge", "strip the perfectworld iOS instrumentation".

## ios-sync

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Updates StateServer.swift, DebugOverlay.swift, Package.swift,
and the typed @Observable state accessors. Use after you upgrade perfectworld
or add new ViewModels/properties that need accessor coverage.
Use when asked to "resync the iOS debug bridge", "regenerate iOS
accessors", or "update the perfectworld iOS instrumentation".

Voice triggers (speech-to-text aliases): "resync the iOS debug bridge", "regenerate iOS accessors", "update the perfectworld iOS instrumentation".
