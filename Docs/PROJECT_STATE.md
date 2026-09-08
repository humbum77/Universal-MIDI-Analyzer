# Project State

## Project
Universal MIDI Analyzer

## Current phase
Scaffold / architecture planning.

## Goal
Build a reusable analyzer for arbitrary MIDI devices that can capture traffic, map controllers, compare readable device states, and create device-specific protocol profiles without assuming one manufacturer's implementation.

## Initial priorities
1. Stable MIDI port layer.
2. Passive monitor and capture format.
3. SAFE mode and safety policy enforcement.
4. CC auto-scan engine with configurable pacing and cancellation.
5. State-diff mapper for devices with readable state dumps.
6. Device profile schema.
7. NRPN/RPN support.
8. Controlled SysEx research workflow.
9. GUI.

## Non-goals for the initial scaffold
- No blind SysEx brute force.
- No automatic store/write/reset operations.
- No firmware/bootloader probing.
- No assumption that every device exposes a state dump.

## Design principle
Protocol discovery must be reproducible: each experiment should record device profile, input stimulus, timestamps, raw MIDI traffic, baseline/current state where available, and derived findings.
