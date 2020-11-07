from flask import Flask, request, Response
import mariadb
import json

app = Flask(__name__)
Animals_List = ["Parrot","Dog","Chicken","Cow","Pig","Crow","Fish"]

@app.route('/', methods=["GET","POST","PATCH", "DELETE"])
def Animals():
    if request.method == 'GET':
        return Response(json.dumps(Animals_List, default=str), mimetype="application/json", status=200)
    elif request.method == 'POST':
        return Response("Added Snake to the list!", mimetype="text/html", status=200)
    elif request.method == 'PATCH':
        return Response("Changed Snake to Lizard!", mimetype="text/html", status=200)
    elif request.method == 'DELETE':
        return Response ("Deleted Chicken from the list!", mimetype="text/html", status=200)

 