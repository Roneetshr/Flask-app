import json
from logging import root
from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        "id":1,
        "title":"Run"
    }
]
@app.route("/adddata",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        }, 400)

    contact = {
        "id": tasks[-1]["id"]+1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "done" : False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/getdata")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__ == "__main__"):
    app.run(debug = True)
    