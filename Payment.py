from datetime import date
from Member import Member
class Payment:
    def __init__(self , id:str , member:Member , amount:int , payment_date:tuple):
        self.__id = id
        self.member = member
        if amount > 0:
            self.amount = amount
        else:
            raise ValueError("amount can't be less than or equal 0")  
        self.date = date(payment_date[0] , payment_date[1] , payment_date[2])

    @property
    def id(self):
        return self.__id

    def to_dict(self):
        return {
            "id": self.id,
            "member": self.member.to_dict(),
            "amount": self.amount,
            "date": self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        member = Member.from_dict(data["member"])
        payment_date = date.fromisoformat(data["date"])
        return cls(
            data["id"],
            member,
            data["amount"],
            (payment_date.year, payment_date.month, payment_date.day)
        )
