# Universal MIDI Analyzer

Universal MIDI Analyzer is a future-focused toolkit for safely analyzing MIDI devices, discovering control mappings, capturing protocol traffic, and building reusable device profiles.

## Planned scope

- MIDI port discovery and connection management
- Passive MIDI monitor for CC, Program Change, Pitch Bend, Aftertouch, NRPN/RPN and SysEx
- Safe CC auto-scan with configurable ranges, pacing and rollback
- State-diff mapping for devices that expose readable state dumps
- Device profiles and protocol knowledge base
- Export of captures and discovered mappings to JSON/CSV
- Optional GUI for live monitoring, scanning and protocol inspection

## Safety model

The analyzer is intentionally split into three modes:

1. **SAFE** — passive monitoring plus low-risk MIDI discovery.
2. **MAPPER** — controlled CC/NRPN/RPN sweeps and state-diff experiments.
3. **RESEARCH** — active SysEx probing only from an explicit allow-list.

Unknown SysEx commands are never brute-forced automatically. Vendor SysEx may contain write, erase, reset, store, bootloader or firmware commands, so active probing must be opt-in and device-profile-aware.

## Initial architecture

```text
src/
  midi/
    ports.py
    monitor.py
    messages.py
    cc_scanner.py
    nrpn_scanner.py
    sysex_monitor.py
    state_diff.py
    safety.py
  profiles/
  ui/
Docs/
  PROJECT_STATE.md
  SAFETY_MODEL.md
  DEVICE_PROFILE_SPEC.md
  PROTOCOL_RESEARCH.md
captures/
tests/
```

## Status

Project scaffold only. Core implementation will be developed later.
