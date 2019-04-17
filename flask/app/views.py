from app import app
import json
from flask import render_template

@app.route('/')
@app.route('/radialtree1/')
def RadialTree_v1():
    with open("/Users/shuizhuyu/Desktop/GQP/radicaltree/flask/app/static/alldata.json") as load_file:
        data = json.load(load_file)
    return render_template("Tree_v3.html",variable=data)

@app.route('/radialtree2/')
def RadialTree_v2():
    with open("/Users/shuizhuyu/Desktop/GQP/radicaltree/flask/app/static/alldata_v2.json") as load_file:
        data = json.load(load_file)
    return render_template("Tree_v3.html",variable=data)
