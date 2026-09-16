# UE Code Style And Readability

Use this reference when a task changes Unreal Engine C++ or the C++/Blueprint handoff, or when the user asks about naming, formatting, readability, or code review conventions.

## Evidence And Priority

- Treat the current project's active code as the primary style evidence. Prefer a nearby implementation with the same responsibility, module, lifecycle, and ownership.
- Unreal Header Tool, reflection, serialization, module API, networking, and engine-required conventions take precedence over this reference.
- Do not reformat an entire file or module for a local feature. Keep style-only edits limited to touched code and directly adjacent interfaces.
- A WIP guideline or a single precedent is not enough to create a blocking rule. Report uncertainty and preserve the established project pattern.

## Blocking Checks

Block only when the change creates a real correctness, maintainability, or review risk:

- An uninitialized pointer or built-in member can be read before assignment.
- A control-flow statement with a meaningful body omits braces and creates ambiguity or a maintenance hazard.
- Consecutive `switch` cases intentionally fall through without an explicit project-approved annotation such as `[[fallthrough]]`.
- A new C++/Blueprint API conflicts with Unreal reflection, generated-code, replication, or module boundaries.
- A public shared API hides ownership, completion, failure, cancellation, or cleanup behavior behind an undocumented contract.

## Default Recommendations

- Use descriptive names and avoid non-standard abbreviations. Match the project's established casing for variables, members, globals, classes, and functions.
- Prefer verb-noun or noun-verb names for functions and PascalCase for types when that matches the surrounding module.
- Mark immutable locals and members `const` or `constexpr` where it improves the contract; mark non-mutating member functions `const` when compatible with the API.
- Pass class types by reference or `const` reference when copying is not part of the contract. Name output reference parameters with the project's established `out` convention when one exists.
- Keep non-trivial function definitions in `.cpp`; keep only simple, deliberately inline accessors in headers. Use `inline` or `FORCEINLINE` only when the project or measured hot path justifies it.
- Prefer explicit pointer checks such as `Pointer != nullptr` when they improve readability or avoid an unintended conversion.
- Prefer composition and components over adding inheritance layers without a verified ownership reason.
- Prefer explicit types when `auto` would hide a meaningful conversion, ownership, or search term. `auto` remains appropriate for iterators, lambda types, and function-pointer types.

## Context-Dependent Checks

These are review prompts, not universal errors:

- `foreach` can improve readability when the index has no semantic role; retain indexed loops for paired arrays, ring buffers, explicit indices, or measured hot paths.
- Avoid division or square root only when profiling, call frequency, or a documented performance path shows that the operation matters. Do not replace clear code speculatively.
- Member prefixes such as `m_`, global prefixes such as `g_`, and boolean prefixes such as `b`, `is`, or `has` are project conventions. Do not enforce one prefix when the project has not settled it.
- Access should normally be `private`, with `public` limited to required external APIs and `protected` limited to verified subclass contracts. Do not change access solely for stylistic preference.

## Review Output

When reporting a style finding, label it as one of:

- **Blocking**: correctness, generated-code, ownership, lifecycle, or API risk.
- **Recommendation**: clear readability or consistency improvement supported by project evidence.
- **Context-dependent**: reasonable alternative exists; explain the tradeoff and do not block delivery.

Always state whether the finding is based on a documented project convention, a nearby active precedent, or a general C++ recommendation. Do not present a general recommendation as a project fact.
