from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class SysExPacket:
    data: tuple[int, ...]

    @classmethod
    def from_bytes(cls, data: Sequence[int]) -> "SysExPacket":
        payload = tuple(int(x) & 0xFF for x in data)
        if not payload or payload[0] != 0xF0 or payload[-1] != 0xF7:
            raise ValueError("SysEx packet must start with F0 and end with F7")
        return cls(payload)

    @property
    def manufacturer_id(self) -> tuple[int, ...]:
        if len(self.data) < 3:
            return ()
        if self.data[1] == 0x00 and len(self.data) >= 5:
            return self.data[1:4]
        return (self.data[1],)


def passive_only_message() -> str:
    return (
        "Unknown SysEx is capture-only by default. "
        "Active replay/probing requires an explicit device-profile allow-list."
    )
