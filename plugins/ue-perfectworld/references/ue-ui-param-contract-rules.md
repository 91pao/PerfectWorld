# UE UI Parameter Contract Rules

Use these rules for widget initialization, screen-opening arguments, Blueprint handoff data, and UI event payloads.

## Core Rule

Give each UI entry path one clear primary contract that matches the current project's UI framework.

## Discovery

- Search the widget or screen type and every active open, construct, initialize, refresh, and event call site
- Identify whether the project uses typed payloads, exposed properties, setters, interfaces, view models, subsystem calls, or another established mechanism
- Confirm parameter ownership, lifetime, nullability, and Blueprint visibility before changing the contract
- Verify legacy shapes through real callers, asset references, or editor configuration rather than comments alone

## Contract Rules

- Prefer typed, named data over positional or shape-dependent payloads when the project supports it
- Parse and validate required data once near the entry point
- Keep optional data explicit and prevent parameter positions or meanings from changing across branches
- Avoid supporting multiple representations merely because conversion is easy
- Keep compatibility branches small, documented with a verified caller, and removable
- Report invalid contracts through the project's existing diagnostic path when silent failure would hide a defect
- Do not retain both old and new protocols without a confirmed compatibility requirement

## Review Question

Ask: "What is the single supported way this UI should receive its required data?"

If the answer is unclear, inspect callers and editor assets before adding another protocol.
