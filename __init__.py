from flask import Flask, request
from datetime import datetime, date, timezone
import uuid

app = Flask(__name__)

in_memory_database = {
    "b6d0568f-0110-49d5-94f0-cca98a7fff9a": {
        "id": "b6d0568f-0110-49d5-94f0-cca98a7fff9a",
        "title": "Clean Room", 
        "created_date": datetime.now(timezone.utc),
        "due_date": date(2023, 6, 15),
        "is_complete": False 
    },
    "4b50e146-f277-48c3-b340-17ed81ddfcd7": { 
        "id": "4b50e146-f277-48c3-b340-17ed81ddfcd7",
        "title": "Pick up perscription", 
        "created_date": datetime.now(timezone.utc),
        "due_date": date(2023, 6, 15),
        "is_complete": False 
    },
    "dcaf8888-7a2f-400f-bf19-bad1132dc73f": {
        "id": "dcaf8888-7a2f-400f-bf19-bad1132dc73f",
        "title": "Return library books", 
        "created_date": datetime.now(timezone.utc),
        "due_date": date(2023, 6, 15),
        "is_complete": False 
    }
}

@app.route('/todos', methods=['GET', 'POST'])
def todos_route():
   if request.method == 'GET':
       return list_todos()
   elif request.method == "POST":
       return create_todo(request.get_json(force=True))
       
def create_todo(new_todo):
   new_todo_id = uuid.uuid4()
   new_todo["id"] = new_todo_id
   new_todo["due_date"] = datetime.fromisoformat(new_todo["due_date"])
   new_todo["created_date"] = datetime.now(timezone.utc)
   in_memory_database[new_todo_id] = new_todo
   return new_todo

def list_todos():
   return {"todos":list(in_memory_database.values())}

@app.route('/todos/<id>')
def get_todo(id):
   return in_memory_database[id]