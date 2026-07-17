# UE Comment And Log Rules

## Guided Implementation Comments

- Treat detailed comments as a required part of code delivered for manual teaching
- Give every added or meaningfully changed class, struct, function, and important property a clear purpose comment
- Explain business or gameplay intent, why the code belongs in this owner, when it runs in the UE lifecycle, and what state or side effects it controls
- Document parameters, return meaning, ownership and lifetime expectations, authority or replication requirements, thread or async constraints, and failure behavior when relevant
- Add inline comments before critical validation, state transitions, delegate binding or removal, replication handling, transactions, asset loading, persistence, and non-obvious engine calls
- Explain why a branch or engine pattern is necessary, not merely what the syntax does
- Keep comments accurate enough to remain in production if the user chooses to type them
- Use the user's requested language; otherwise follow the surrounding project's language and terminology while keeping the explanation understandable to the user
- The user decides whether to enter the comments, but Codex must include them in the teaching code
- Do not replace detailed code comments with prose outside the code block

## Direct Project Edits

- Match the nearby project's comment language, terminology, formatting, and general density
- Preserve useful existing comments and update comments made inaccurate by the code change
- Add enough comments to explain non-obvious intent, ownership, lifecycle, authority, and safety constraints
- Do not add personal author tags, signatures, or generated-code markers

## Comment Quality

- Do not narrate trivial syntax, punctuation, assignments, or obvious control flow line by line
- Do not use comments to excuse unclear or overcomplicated code; simplify the implementation first
- Do not put tutorial-only instructions, unresolved assumptions, placeholders, or TODOs inside transcription-ready code
- Keep comments synchronized with the final implementation after any self-review rewrite

## Logs And User Feedback

- Follow the project's existing log categories, verbosity levels, macros, and user-facing notification path
- Log important rejected conditions that would otherwise be difficult to diagnose
- Include the operation and relevant non-sensitive object, player, config, asset, or record identifiers when available
- Do not expose secrets, credentials, personal data, or unnecessary server internals in logs or user messages
- Avoid noisy logs in ticks, replication callbacks, animation updates, or other high-frequency paths
- Keep repetitive defensive checks quiet only when the failure is expected and nearby maintained code follows the same convention
