# UE Project Consistency

Discover each project's conventions at runtime. This plugin must not carry implementation details from one project into another.

## Reference Discovery

- Start with the same feature domain, module or plugin, base class, lifecycle phase, and authority side
- Confirm candidates through active call sites, registrations, asset references, tests, configuration, or other production usage
- Prefer maintained code that is close to the target in responsibility, not merely close in filename or search results
- Check whether a candidate is generated, deprecated, experimental, disabled, duplicated, or temporary before treating it as precedent
- When candidates disagree, explain the evidence and follow the closest trustworthy production pattern

## Adaptation Rules

- Preserve the project's observed naming, module boundaries, ownership, reflection usage, lifecycle, error reporting, and data access conventions
- Do not assume a feature belongs in any particular framework class, subsystem, component, Blueprint, directory, or data asset type
- Do not assume C++ or Blueprint should own a behavior; infer the existing split and keep network authority and security constraints intact
- Reuse an existing abstraction only when it is active and appropriate for the target domain
- Do not introduce a manager, service, controller, subsystem, generic wrapper, or framework layer unless the project already uses it for the same responsibility or the task proves a real need
- Keep changes local when the project has no stable shared pattern
- Use standard Unreal Engine conventions as the fallback when project evidence is missing or unreliable

## Consistency Limits

- Do not normalize unrelated legacy code
- Do not copy a nearby defect or unnecessary abstraction merely for visual consistency
- Do not infer a project-wide rule from one implementation
- State which observed conventions materially influenced the result
