from enum import Enum


class MatchStatus(str, Enum):
    PLAYED = "odigrana"
    DEFAULT_RESULT = "zavedena 3:0"