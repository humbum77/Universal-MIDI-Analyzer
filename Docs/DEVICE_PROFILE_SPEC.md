# Device Profile Specification

Device profiles describe what the analyzer knows about a particular MIDI device and, critically, what it is allowed to send.

## Proposed fields

```yaml
id: vendor-model
manufacturer: Example
model: Device
transport:
  midi_channels: [1]
  preferred_input_name: null
  preferred_output_name: null
capabilities:
  cc: true
  nrpn: false
  rpn: false
  program_change: true
  sysex: true
safety:
  program_change_safe: true
  cc_scan_safe: true
  nrpn_scan_safe: false
sysex:
  manufacturer_id: []
  safe_requests: []
  dangerous_patterns: []
state_read:
  supported: false
  request: null
  response_match: null
scan_defaults:
  delay_ms: 20
  value_range: [0, 127]
notes: []
```

## Command classification
Every known active command should have one classification:
- `READ_ONLY`
- `REVERSIBLE`
- `STATE_CHANGE`
- `PERSISTENT_WRITE`
- `DANGEROUS`

Only explicitly allowed command classes may be sent in each safety mode.

## Discovery provenance
Mapped parameters should store provenance where possible:
- manual test
- captured official editor traffic
- automated sweep
- documentation
- inferred / unconfirmed

Inferences must never be silently promoted to confirmed protocol facts.
