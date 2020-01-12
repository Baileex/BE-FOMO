from db import db
from passlib.hash import pbkdf2_sha256 as sha256



class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(80), unique = True)
    age = db.Column(db.Integer)
    location = db.Column(db.String(80))
    option_1 = db.Column(db.String(80))
    option_2 = db.Column(db.String(80))
    option_3 = db.Column(db.String(80))
    option_4 = db.Column(db.String(80))
    family = db.Column(db.Boolean)
    gender = db.Column(db.String(30))

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def __init__(self, username, password, email, age, location, option_1, option_2, option_3, option_4, family, gender):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.location = location
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.family = family
        self.gender = gender

    def json(self):
        return 
        {'username': self.username, "password": self.password, 'email': self.email, "age": self.age, "location": self.location, "option_1": self.option_1, "option_2": self.option_2, "option_3": self.option_3, "option_4": self.option_4, "family": self.family, "gender": self.gender}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
