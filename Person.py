from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self , id:str , phone:str , name:str ):
        self.__id = id
        self.phone = phone
        self.name = name

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def get_role(self):
        pass