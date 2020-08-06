from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask_cars'
app.config['FLASK_ENV'] = 'development'
app.config['FLASK_APP'] = 'app.py'

from car_crud import *

@app.route('/')
def home():
    return jsonify({'message' : 'Home Page'})

@app.route('/cars', methods=['GET', 'POST'])
def all_cars():
    if request.method == 'GET':
        return get_all_cars()
    if request.method == 'POST':
        create_car(request.form['name'], request.form['model'], request.form['make'], request.form['year'])
        return redirect('/cars')

@app.route('/car/<id>', methods=['GET', 'PUT', 'DELETE'])
def car_detail():
    if request.method == 'GET':
        return get_car(id)
    if request.method == 'PUT':
        return update_car(id)
    if request.method == 'DELETE':
        return destroy_car(id)
