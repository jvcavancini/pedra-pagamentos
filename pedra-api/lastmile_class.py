from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class last_mile(db.Model):
    id_atendimento=db.Column(db.Integer(),primary_key=True)
    id_cliente=db.Column(db.Integer(),nullable=False)
    angel=db.Column(db.String(255),nullable=False)
    polo_cidade=db.Column(db.String(255),nullable=False)
    polo_uf=db.Column(db.String(2),nullable=False)
    data_limite=db.Column(db.DateTime(),nullable=False)
    data_atendimento=db.Column(db.DateTime(),nullable=True)

    def __repr__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id_atendimento(cls,id_atendimento):
        return cls.query.get_or_404(id_atendimento)

    @classmethod
    def get_by_id_cliente(cls,id):
        return cls.query.filter_by(id_cliente=id)

    @classmethod
    def get_by_angel(cls,id):
        return cls.query.filter(cls.angel.contains(id.upper()))

    @classmethod
    def get_by_uf(cls,id):
        return cls.query.filter_by(polo_uf=id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
