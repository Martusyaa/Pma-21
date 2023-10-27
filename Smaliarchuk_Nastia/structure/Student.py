from dataclasses import dataclass
import re

@dataclass
class Student:
    surname: str
    name: str
    dataOfBirth: str
    grades: list

    def __str__(self):
        grades = re.sub("\[(.*)\]",r"\1",str(self.grades))
        return f"\t{self.surname}\t{self.name}\t{self.dataOfBirth}\t{grades}"

