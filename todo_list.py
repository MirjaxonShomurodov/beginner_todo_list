import tinydb
from datetime import datetime
from tinydb.table import Document

class Todo:
    def __init__(self):
        self.db = tinydb.TinyDB("todo_list.json",indent=4, separators=(',',':'))
        self.table = self.db.table("Todo")

    def add(self,todo_add:dict):
        return self.table.insert(todo_add)
    
    def all(self):
        return self.table.all()
    
    def id(self,id:int):
        q = tinydb.Query()
        return self.table.search(q.id == id)

    def task(self,task:str):
        q = tinydb.Query()
        return self.table.search(q.task ==task)
    
    def description(self,description:str):
        q = tinydb.Query()
        return self.table.search(q.description == description)
    
    def completed(self,completed:bool):
        q = tinydb.Query()
        return self.table.search(q.completed == completed)
    
    def created_at(self):
        new = datetime.now()
        date = new.strftime("%Y:%d:%m %H:%M:%S")
        user = Document(date)
        return  self.table.insert(user)
    
   