from db import db
from passlib.hash import pbkdf2_sha256 as sha256


class BusinessModel(db.Model):
    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))
    business_name = db.Column(db.String(80))
    address = db.Column(db.String(400))
    description = db.Column(db.String(400))

    events = db.relationship('EventsModel', lazy='dynamic')

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
        
    def __init__(self, username, password, email, business_name, address, description):
        self.username = username
        self.password = password
        self.email = email
        self.business_name = business_name
        self.address = address
        self.description = description

    def json(self):
        return {'business_id': self.id,
                'business_name': self.business_name, 
                'username': self.username, 
                'password': self.password, 
                'email': self.email,
                'address': self.address,
                'description': self.description
        }

    @classmethod
    def find_by_business_name(cls, business_name):
        return cls.query.filter_by(business_name=business_name).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username= username).first()

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
