import json

class FileManager:
    def __init__(self , file_path:str):
        self.file_path = file_path

    def load(self):
        with open(self.file_path , "r") as file:
            return json.load(file)

    def save(self , content:dict):
        with open(self.file_path , "w") as file:
            json.dump(content, file)

    