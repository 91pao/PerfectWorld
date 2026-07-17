# UE Comment And Log Rules

## Guided Implementation Comments

- Treat comprehensive but concise comments as a required part of code delivered for manual teaching
- Default to one-line `//` comments; each comment should explain one purpose, reason, contract, or non-obvious constraint
- Use consecutive `//` lines only when lifecycle, ownership, authority, side effects, or failure behavior cannot be explained accurately in one line
- Give every added or meaningfully changed class, struct, function, and important property a concise purpose comment
- Cover business or gameplay intent, owner responsibility, UE lifecycle timing, state changes, parameters, return meaning, ownership, replication, async constraints, and failure behavior wherever each is relevant
- Add a short `//` comment before critical validation, state transitions, delegate binding or removal, replication handling, transactions, asset loading, persistence, and non-obvious engine calls
- Explain why a branch or engine pattern is necessary, not merely what the syntax does
- Keep comments accurate enough to remain in production if the user chooses to type them
- Use the user's requested language; otherwise follow the surrounding project's language and terminology while keeping the explanation understandable to the user
- The user decides whether to enter the comments, but Codex must include them in the teaching code
- Do not replace required code comments with prose outside the code block

## Direct Project Edits

- Match the nearby project's comment language, terminology, formatting, and general density
- Preserve useful existing comments and update comments made inaccurate by the code change
- Add enough comments to explain non-obvious intent, ownership, lifecycle, authority, and safety constraints
- Prefer concise single-line comments when compatible with the project's established style
- Do not add personal author tags, signatures, or generated-code markers

## Comment Quality

- Keep each comment near the code it governs and normally to about one source line
- When multiple lines are necessary, use consecutive `//` lines with one clear idea per line rather than a long paragraph
- Do not use block comments, banner comments, or repeated summaries when short `//` comments are sufficient
- Do not narrate trivial syntax, punctuation, assignments, or obvious control flow line by line
- Do not repeat information already clear from the symbol name, type, signature, or immediately surrounding code
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
