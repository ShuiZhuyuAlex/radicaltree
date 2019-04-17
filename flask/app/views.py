from app import app
import json
from flask import render_template

@app.route('/')
<<<<<<< HEAD
@app.route('/radicaltree1/')
def RadicalTree_v1():
    with open("/Users/shuizhuyu/Desktop/GQP/radicaltree/flask/app/static/alldata.json") as load_file:
        data = json.load(load_file)
    return render_template("Tree_v3.html",variable=data)

@app.route('/radicaltree2/')
def RadicalTree_v2():
    with open("/Users/shuizhuyu/Desktop/GQP/radicaltree/flask/app/static/alldata_v2.json") as load_file:
=======
@app.route('/radicaltree/')
def RadicalTree():
    with open("/home/zsun/radicaltree/flask/app/static/alldata.json") as load_file:
>>>>>>> e18326b874a9aa3ac1641b56310f8e1fed0b7541
        data = json.load(load_file)
    return render_template("Tree_v3.html",variable=data)
