from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_json, find_index

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        try:
            iD = db[-1]['id'] + 1
        except:
            iD = 1
        
        card = {
            'id': iD,
            'heading': request.form['heading'],
            'task': request.form['task'],
            'done': False
        }

        db.append(card)
        save_json()
        return redirect(url_for('welcome'))
    elif request.method == "GET":
        inprogress = list(filter(lambda i : i['done'] == False,db))
        completed = list(filter(lambda i :  i['done'] == True,db))
        return render_template('index.html', inprogress = inprogress, completed= completed)        


@app.route('/done/<int:index>')
def mark_as_done(index):
    db[find_index(index)]['done'] = True
    save_json()
    return redirect(url_for('welcome')) 


@app.route('/delete/<int:index>')
def delete_tasks(index):
    db.pop(find_index(index))
    save_json()
    return redirect(url_for('welcome')) 