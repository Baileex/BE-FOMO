from db import db


class EventHistoryModel(db.Model):
    __tablename__ = 'event_history'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(40))
    sex = db.Column(db.String(40))
    event_type = db.Column(db.String(40))
    location = db.Column(db.String(200))
    time = db.Column(db.String(80))

    def __init__(self, age, sex, event_type, location, time):
        self.age = age
        self.sex = sex
        self.event_type = event_type
        self.location = location
        self.time = time

    def json(self):
        return {'age': self.age, 'sex': self.sex, 'event_type': self.event_type, 'location': self.location, 'time': self.time}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_event_type(cls, event_type):
        return cls.query.filter_by(event_type=event_type).all()  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
