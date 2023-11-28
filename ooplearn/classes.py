from datetime import datetime, UTC
from fnmatch import fnmatch
import os
from pathlib import Path
from pprint import pp


class Employee:
    def __init__(self, name, age, postion, salary):
        self.name = name
        self.age = age
        self.postion = postion
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old. Employee is a {self.postion} with the salary of ${self.salary:,.2f}"

    def __repr__(self) -> str:
        return f"Employee({repr(self.formatted_name)},{repr(self.age)},{repr(self.postion)},{repr(self.salary)})"

    @property
    def formatted_name(self) -> str:
        return self._fname

    @formatted_name.setter
    def formatted_name(self, value: str) -> str:
        self._fname = value.title() if value else None


def employee_calls(Employee):
    e = Employee(None, None, None, 0)  # call __new__ and __init__ to initialize
    e1 = Employee("Debabrata Patnaik", 34, "developer", 30000)
    e1.formatted_name = "debabrata patnaik"
    e.formatted_name = "simple dummy user"
    print(e, e.__dict__, repr(e), e.formatted_name)
    print(e1, e1.__dict__, repr(e1), e1.formatted_name)


def get_date(ts: str) -> str:
    return datetime.fromtimestamp(ts, UTC).strftime("%d %b %Y")


if __name__ == "__main__":
    # employee_calls(Employee)
    pp([f for f in os.listdir(".") if fnmatch(f, "*.py")])
    pp([str(n) for n in Path("./ooplearn").glob("*.py")])

    pp(
        [
            f"Modified {get_date(f.stat().st_mtime)} {f.name}"
            for f in os.scandir(".")
            if fnmatch(f, "*.py")
        ]
    )
