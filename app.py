from flask import Flask,request
from todo_list import Todo
from datetime import datetime
from pprint import pprint
app = Flask(__name__)
todo = Todo()

@app.route("/Todo")
def all_todo():

    return todo.all()


@app.route("/Todo/add", methods= ["POST"])
def main():
        data = request.get_json(force=True)
        new = datetime.now()
        date = new.strftime("%Y:%d:%m %H:%M:%S")
        forc = {
                "id": data['id'],
                "task":data['task'],
                "description":data['description'],
                "completed":data['completed'],
                "created_at":date,
                "updated_at":date
            }       
        todo.add(forc)
        return {}
@app.route("/Todo/id/<int:id>")
def all_id(id):
     return todo.id(id)


@app.route("/Todo/task/<task>",methods=["POST"])
def task(task):
     return todo.task(task)

@app.route("/Todo/description/<description>",methods=["POST"])
def description(description):
     return todo.description(description)

@app.route("/Todo/completed/<completed>",methods = ["POST"])
def completed(completed):
     return todo.completed(completed)

@app.route("/Todo/created/<created>",methods=["POST"])
def created(created):
     return todo.created_at(created)

@app.route("/Todo/updated/<updated>",methods=["POST"])
def updated(updated):
     return todo.updated_at(updated)


if __name__=="__main__":
    app.run(debug=True,port=3000)

# pprint(updated("%Y:%d:%m %H:%M:%S"))


