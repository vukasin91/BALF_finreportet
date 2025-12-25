from enum import Enum, auto


class EmploymentType(str, Enum):
    MANAGER = "manager"
    DELEGATE = "delegate"
    REFEREE = "referee"
