from models import Car, db
from flask import jsonify, redirect

def create_car(name, model, make, year):
    year = int(year)
    car = Car(name=name, make=make, model=model, year=year)
    db.session.add(car)
    db.session.commit()
    return car

def get_all_cars():
    all_cars = Car.query.all()
    if all_cars:
        all_cars = [car.as_dict() for car in all_cars]
        return jsonify(all_cars)
    else:
        return jsonify({'message' : 'No Cars in the database'})

def get_car():
    car = Car.query.get(id)
    if car: return jsonify(car.as_dict())
    else: return jsonify(['message' : f'No car found at id: {id}'])

def update_car(id, name, make, model, year):
    car = Car.query.get(id)
    if car:
        car.name = name or car.name
        car.make = make or car.make
        car.model = model or car.model
        car.year = year or car.year
        db.session.commit()
        return jsonify(car.as_dict())
    else: return jsonify({'message' : f'No car found at id {id}'})

def destroy_car(id):
    car = Car.query.get(id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return redirect('/cars')
    else: return jsonify({'message' : 'No car with id: {id} to delete'})