from enum import Enum
Month=Enum('Month',('J','F'))

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


class WeekDay(Enum):
    Sun=0
    Mon=1
    Tue=2


day1=WeekDay.Mon
print(day1)

day1=WeekDay.Mon.value
print(day1)