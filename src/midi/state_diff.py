from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ByteDiff:
    offset: int
    before: int
    after: int
    xor_mask: int


def diff_bytes(before: Sequence[int], after: Sequence[int]) -> list[ByteDiff]:
    if len(before) != len(after):
        raise ValueError("state payloads must have equal length")
    out: list[ByteDiff] = []
    for index, (a, b) in enumerate(zip(before, after)):
        a_i = int(a) & 0xFF
        b_i = int(b) & 0xFF
        if a_i != b_i:
            out.append(ByteDiff(index, a_i, b_i, a_i ^ b_i))
    return out


def changed_bit_positions(diffs: Iterable[ByteDiff]) -> list[tuple[int, int]]:
    bits: list[tuple[int, int]] = []
    for item in diffs:
        for bit in range(8):
            if item.xor_mask & (1 << bit):
                bits.append((item.offset, bit))
    return bits
