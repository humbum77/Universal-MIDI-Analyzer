# Protocol Research Notes

This document will accumulate protocol-discovery findings that are not yet mature enough to become confirmed device-profile entries.

## Research workflow
1. Record the exact hardware/firmware identity where possible.
2. Capture passive MIDI traffic first.
3. Identify known message families: CC, PC, Pitch Bend, Aftertouch, NRPN/RPN, SysEx.
4. Prefer observing official software/device interaction before active probing.
5. For controlled scans, record baseline, stimulus, response, timing and raw bytes.
6. Derive diffs and candidate mappings.
7. Mark conclusions as confirmed, probable, inferred, or unknown.
8. Move only confirmed safe commands into device profiles.

## Planned research artifacts
- raw capture logs
- JSON experiment metadata
- CSV controller maps
- state-diff summaries
- SysEx request/response pairs
- byte/bit ownership maps
- validation reports

## Important limitation
Not every MIDI device exposes a readable complete state. The analyzer should support discovery workflows that rely only on observable MIDI traffic and user actions when state-dump analysis is unavailable.
