from Person import Person
class not_found(Exception):
    pass

class Trainer(Person):
    def __init__(self, id:str, phone:str, name:str , specialty:str):
        super().__init__(id, phone, name)
        fits = ["fitness", "cardio", "bodybuilding"]
        if specialty.lower() in fits:
            self.specialty = specialty.lower()
        else:
            raise not_found("your specialty not found in our programe , our programe includes ( fitness , cardio , bodybuilding ) only! ") 

    def get_role(self):
        return f"I am trainer"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "specialty": self.specialty
        }  

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["phone"],
            data["name"],
            data["specialty"]
        )
             