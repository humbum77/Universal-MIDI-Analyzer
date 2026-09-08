from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class SafetyMode(str, Enum):
    SAFE = "SAFE"
    MAPPER = "MAPPER"
    RESEARCH = "RESEARCH"


class CommandClass(str, Enum):
    READ_ONLY = "READ_ONLY"
    REVERSIBLE = "REVERSIBLE"
    STATE_CHANGE = "STATE_CHANGE"
    PERSISTENT_WRITE = "PERSISTENT_WRITE"
    DANGEROUS = "DANGEROUS"


@dataclass(frozen=True)
class OutgoingCommand:
    kind: str
    payload: tuple[int, ...]
    classification: CommandClass
    description: str = ""


_ALLOWED_BY_MODE = {
    SafetyMode.SAFE: {CommandClass.READ_ONLY},
    SafetyMode.MAPPER: {
        CommandClass.READ_ONLY,
        CommandClass.REVERSIBLE,
        CommandClass.STATE_CHANGE,
    },
    SafetyMode.RESEARCH: {
        CommandClass.READ_ONLY,
        CommandClass.REVERSIBLE,
        CommandClass.STATE_CHANGE,
    },
}


def can_send(mode: SafetyMode, command: OutgoingCommand) -> bool:
    """Return whether a command is permitted by the global safety policy.

    Persistent writes and dangerous commands are never implicitly allowed.
    Device-profile allow-lists must add an additional check on top of this one.
    """
    return command.classification in _ALLOWED_BY_MODE[mode]


def filter_allowed(mode: SafetyMode, commands: Iterable[OutgoingCommand]) -> list[OutgoingCommand]:
    return [command for command in commands if can_send(mode, command)]
