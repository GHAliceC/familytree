from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from member import Node
from treeOps import TreeOps

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def renderer():
    return render_template("index.html")

@app.route("/linfamily.txt")
def get_file():
    return send_from_directory('static', "linfamily.txt")

@app.route("/addMember", methods=['GET', 'POST'])
def addMember():
    method = request.method
    print("print0:", method)
    if method == 'POST':
        param = request.get_json()
        print("print1", request)
        print("print1.1", param)
        try:
            tOps = TreeOps()
            parNode = tOps.findparent(**param)
            print(parNode.name, parNode.spouse)
            res = tOps.addchild(parNode, **param)
            print("res:", res)
            if res:
                return "success"
            else:
                return "fail"
        except Exception as e:
            print(str(e))
            return str(e)
    return "fail"

@app.route("/editMember", methods=['GET', 'POST'])
def editMember():
    method = request.method
    if method == 'POST':
        param = request.get_json()
        try:
            tOps = TreeOps()
            parNode = tOps.findparent(**param)
            res = tOps.editchild(parNode, **param)
            if res:
                return "success"
            else:
                return "fail"
        except Exception as e:
            print(str(e))
            return str(e)
    return "fail"

@app.route("/delMember", methods=['GET', 'POST'])
def delMember():
    method = request.method
    if method == 'POST':
        param = request.get_json()
        try:
            tOps = TreeOps()
            parNode = tOps.findparent(**param)
            print("parNode: ", parNode.name)
            res = tOps.delnode(parNode, **param)
            if res:
                return "success"
            else:
                return "fail"
        except Exception as e:
            print(str(e))
            return str(e)
    return "fail"


if __name__ == "__main__":
    app.run(port=8000)