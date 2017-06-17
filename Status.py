from enum import Enum


class Status(Enum):
    DEBATER = 'DEBATER'
    JUDGE = 'JUDGE'
    JUDGE_OR_DEBATE = 'JUDGE_OR_DEBATE'
    SPECTATOR = 'SPECTATOR'
