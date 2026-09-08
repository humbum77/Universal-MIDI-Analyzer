from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator

from .safety import CommandClass, OutgoingCommand, SafetyMode, can_send


@dataclass(frozen=True)
class CCScanPlan:
    channel: int = 1
    controllers: tuple[int, ...] = tuple(range(128))
    values: tuple[int, ...] = tuple(range(128))
    delay_ms: int = 20

    def validate(self) -> None:
        if not 1 <= self.channel <= 16:
            raise ValueError("channel must be 1..16")
        if self.delay_ms < 0:
            raise ValueError("delay_ms must be >= 0")
        if any(not 0 <= cc <= 127 for cc in self.controllers):
            raise ValueError("controllers must be 0..127")
        if any(not 0 <= value <= 127 for value in self.values):
            raise ValueError("values must be 0..127")


def iter_cc_commands(plan: CCScanPlan, *, mode: SafetyMode = SafetyMode.MAPPER) -> Iterator[OutgoingCommand]:
    """Generate CC messages for a controlled scan without sending them.

    Transport and timing are intentionally separate from planning so the UI can
    show a dry-run and the runtime can provide cancellation/emergency stop.
    """
    plan.validate()
    status = 0xB0 | ((plan.channel - 1) & 0x0F)
    for cc in plan.controllers:
        for value in plan.values:
            command = OutgoingCommand(
                kind="cc",
                payload=(status, cc, value),
                classification=CommandClass.STATE_CHANGE,
                description=f"CC {cc} = {value}",
            )
            if not can_send(mode, command):
                raise PermissionError(f"CC scan not allowed in {mode.value} mode")
            yield command


def planned_message_count(plan: CCScanPlan) -> int:
    plan.validate()
    return len(plan.controllers) * len(plan.values)
