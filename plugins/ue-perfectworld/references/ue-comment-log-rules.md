# UE Comment And Log Rules

## Complete Code Comments

- Include comprehensive but concise comments in code delivered for manual entry
- Default to one-line `//` comments that explain one purpose, reason, contract, or non-obvious constraint
- Use consecutive `//` lines only when lifecycle, ownership, authority, side effects, or failure behavior cannot be stated accurately in one line
- Give every added or meaningfully changed class, struct, function, and important property a concise purpose comment
- Cover gameplay intent, owner responsibility, UE lifecycle timing, state changes, parameters, return meaning, ownership, replication, async constraints, and failure behavior where relevant
- Comment critical validation, state transitions, delegate lifetime, replication handling, transactions, asset loading, persistence, and non-obvious engine calls
- Explain why a branch or engine pattern is necessary instead of narrating syntax
- Keep comments suitable for production and include them inside the complete code blocks

## Direct Project Edits

- Match nearby comment language, terminology, formatting, and density
- Preserve useful comments and update comments made inaccurate by the code change
- Do not add personal author tags, signatures, generated-code markers, or broad explanatory banners

## Comment Quality

- Keep comments close to the code they govern
- Do not repeat clear symbol names, types, signatures, assignments, or obvious control flow
- Do not use comments to excuse indirect code; simplify the implementation first
- Do not place operational instructions, unresolved assumptions, placeholders, or TODOs inside complete code
- Synchronize comments after every correctness or simplicity rewrite

## Logs And User Feedback

- Follow the project's existing log categories, verbosity levels, macros, and user-facing notification path
- Log rejected conditions when silence would make a real defect difficult to diagnose
- Include the operation and relevant non-sensitive identifiers needed for diagnosis
- Do not expose secrets, credentials, personal data, or unnecessary server internals
- Avoid noisy logs in ticks, replication callbacks, animation updates, and other high-frequency paths
- Keep expected defensive failures quiet only when nearby maintained code follows the same convention
