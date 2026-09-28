from datetime import date
from Member import Member
class not_found(Exception):
    pass

class invalid(Exception):
    pass

class Membership:
    def __init__(self , id:str , start_date:tuple , end_date:tuple , type:str , member:Member):
        self.__id = id
        self.member = member
        self.start_date = date( start_date[0] , start_date[1] , start_date[2] )
        self.end_date = date( end_date[0] , end_date[1] , end_date[2])
        types = ["monthly", "quarterly" , "yearly"]
        if type.lower() in types:
            self.type = type.lower()
        else:
            raise not_found("your type not found in our programe , our types includes ( monthly , quarterly , yearly ) only! ")      

    @property
    def id(self):
        return self.__id

    def membership_status(self):
        if self.start_date <= self.end_date:
            today = date.today()
            if today < self.end_date:
                return "active membership"
            else:    
                return "date expired"     
        else:
            raise invalid("date invalide")    

    def to_dict(self):
        return {
            "id": self.id,
            "member": self.member.to_dict(),
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):
        member = Member.from_dict(data["member"])
        start_date = date.fromisoformat(data["start_date"])
        end_date = date.fromisoformat(data["end_date"])
        return cls(
            data["id"],
            (start_date.year, start_date.month, start_date.day),
            (end_date.year, end_date.month, end_date.day),
            data["type"],
            member
        )