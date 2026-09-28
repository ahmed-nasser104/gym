from Person import Person
class Member(Person):
    def __init__(self, id:str, phone:str, name:str  , email:str):
        super().__init__(id, phone, name )
        self.email = email

    def get_role(self):
        return f"i am member"

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "phone":self.phone
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["phone"],
            data["name"],
            data["email"]
        )