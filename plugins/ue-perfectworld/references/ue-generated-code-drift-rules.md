# UE Generated-Code Drift Rules

Reject code that drifts away from verified current-project conventions or adds complexity without a present requirement.

- Do not add unused delegates, callbacks, events, or extension points for hypothetical future needs
- Do not add managers, services, generic result wrappers, or helper layers unless they remove meaningful current complexity or match a verified project pattern
- Do not add multiple state flags when one local condition or an existing state representation is sufficient
- Do not create broad result objects merely to carry intermediate state
- Do not split one simple operation into several RPCs; follow `ue-client-server-boundary-rules.md` for networked work
- Do not add collections or generic handling when the current requirement has a single known shape
- Do not prepare for expansion without a concrete requirement
- For guided implementation, include comprehensive but concise `//` comments for intent and non-obvious UE behavior, using multiple lines only when one line is insufficient
- Do not rewrite working code into a more abstract style without a demonstrated need
- Prefer clear feature code near the existing flow over clever generic utilities
- Do not add unused variables, functions, enum values, delegates, fields, or configuration
- Keep one-use helpers inline unless extraction materially improves readability, testing, or correctness
- Before delivery, compare the implementation with the smallest complete project-consistent solution; if the current design is several times larger because of avoidable structure, rewrite it instead of merely noting the complexity
- Treat extra files, types, states, branches, delegates, RPCs, and configuration as part of the complexity budget, not only source line count
