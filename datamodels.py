from flask_sqlalchemy import SQLAlchemy

from modelserializer import ModelSerializer

db = SQLAlchemy()


class NEO(db.Model, ModelSerializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    nasa_jpl_url = db.Column(db.String(4096), unique=True, nullable=False)
    is_potentially_hazardous_asteroid = db.Column(db.Boolean, nullable=False)
    close_approach_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<NEO {self.id} {self.name}>'

    def serialize(self):
        serialized = ModelSerializer.serialize(self)
        return serialized
