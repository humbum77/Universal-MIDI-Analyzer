from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Sequence


@dataclass(frozen=True)
class MidiEvent:
    timestamp: str
    direction: str
    kind: str
    data: tuple[int, ...]
    source: str | None = None

    @classmethod
    def now(
        cls,
        *,
        direction: str,
        kind: str,
        data: Sequence[int],
        source: str | None = None,
    ) -> "MidiEvent":
        return cls(
            timestamp=datetime.now(timezone.utc).isoformat(),
            direction=direction,
            kind=kind,
            data=tuple(int(x) & 0xFF for x in data),
            source=source,
        )
