from api import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {
            "id" = self.id,
            "name" = self.name,
            "make" = self.make,
            "model" = self.model,
            "year" = self.year
        }
    
    def __repr__(self):
        return f'🚘 Car(id={self.id}, name="{self.name}", make="{self.make}", model="{self.model}", year="{self.year}")'