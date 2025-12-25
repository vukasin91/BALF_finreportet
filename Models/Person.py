from EmploymentType import EmploymentType


class Person:
    firstName: str
    lastName: str
    employmentType: str
    def __init__(self, firstname, lastname, employmenttype: EmploymentType):
        self.firstName = firstname
        self.lastName = lastname
        self.employmentType = employmenttype.name

