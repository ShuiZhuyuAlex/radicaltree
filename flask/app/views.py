from app import app
import json
from flask import render_template

@app.route('/')
@app.route('/radicaltree/')
def RadicalTree():
    with open("/home/zsun/radicaltree/flask/app/static/alldata.json") as load_file:
        data = json.load(load_file)
    return render_template("Tree_v3.html",variable=data)
