from datetime import date
from Member import Member

class Attendance:
    def __init__(self , id:str , member:Member , attendance_date:tuple):
        self.__id = id
        self.member = member
        self.date = date(attendance_date[0] , attendance_date[1] , attendance_date[2])

    @property
    def id(self):
        return self.__id

    def to_dict(self):
        return {
            "id": self.id,
            "member": self.member.to_dict(),
            "date": self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        member = Member.from_dict(data["member"])
        attendance_date = date.fromisoformat(data["date"])
        return cls(
            data["id"],
            member,
            (
                attendance_date.year,
                attendance_date.month,
                attendance_date.day
            )
        )