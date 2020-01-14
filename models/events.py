from db import db


class EventsModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(80))
    description = db.Column(db.String(400))
    event_type = db.Column(db.String(80))
    date = db.Column(db.String(80))
    time = db.Column(db.String(80))
    min_age = db.Column(db.String(80))
    cost = db.Column(db.String(80))
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    url = db.Column(db.String(800))
    
    business = db.relationship('BusinessModel')

    def __init__(self, name, location, business_id, description, event_type, date, time, min_age, cost, url):
        self.name = name
        self.location = location
        self.business_id = business_id
        self.description = description
        self.event_type = event_type
        self.date = date
        self.time = time
        self.min_age = min_age
        self.cost = cost
        self.url = url

    def json(self):
        return {'name': self.name, 'location': self.location, 'business_id': self.business_id, 'description': self.description, 'event_type': self.event_type, 'date': self.date, 'time': self.time, 'min_age': self.min_age, 'cost': self.cost, 'url': self.url  }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, business_id):
        return cls.query.filter_by(business_id=business_id).all()  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
