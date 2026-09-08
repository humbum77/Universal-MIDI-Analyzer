# Safety Model

Universal MIDI Analyzer must treat unknown devices conservatively.

## Modes

### SAFE
Allowed by default:
- Passive input monitoring
- Device/port discovery
- User-triggered known-safe messages
- Non-destructive logging/export

### MAPPER
Explicitly enabled by the user for a selected device profile:
- CC sweeps
- NRPN/RPN sweeps
- Program Change tests when the profile marks them safe
- State read / state diff experiments when a safe read request is known
- Configurable pacing, cancellation, and optional restore-to-baseline

### RESEARCH
Highest-risk mode. Requires explicit opt-in and an allow-list of exact messages or command templates.

Rules:
- Never brute-force unknown SysEx command spaces.
- Never send unknown write/store/erase/reset/boot/firmware commands.
- Dangerous or irreversible commands belong on a deny-list even if observed in captures.
- Profiles should distinguish read-only, reversible, state-changing, persistent-write, and dangerous operations.
- Log every outgoing active-research message with timestamp and profile context.

## Guardrails
- Emergency Stop must cancel scans immediately.
- Scan rate must be configurable.
- Dry-run should show the planned message sequence without sending it.
- Optional baseline capture and restore should exist where the device protocol safely supports it.
- Active scans should require a selected output port and device profile.
- Unknown SysEx from incoming traffic can be recorded and analyzed, but not automatically replayed.
