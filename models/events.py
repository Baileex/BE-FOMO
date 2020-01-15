from db import db


class EventsModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    name = db.Column(db.String(80))
    cityname = db.Column(db.String(80))
    longitude = db.Column(db.String(80))
    latitude = db.Column(db.String(80))
    postcode = db.Column(db.String(80))
    description = db.Column(db.String(400))
    event_type = db.Column(db.String(80))
    date = db.Column(db.String(80))
    doorsopen = db.Column(db.String(80))
    doorsclose = db.Column(db.String(80))
    minage = db.Column(db.String(80))
    entryprice = db.Column(db.String(80))
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    url = db.Column(db.String(800))
    
    business = db.relationship('BusinessModel')

    def __init__(self, event_name, name, business_id, description, address, cityname, postcode, event_type, date, doorsopen, doorsclose, minage, entryprice, url, longitude, latitude):
        self.name = name
        self.event_name = event_name
        self.business_id = business_id
        self.description = description
        self.event_type = event_type
        self.address = address
        self.cityname = cityname
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.doorsopen = doorsopen
        self.doorsclose = doorsclose
        self.date = date
        self.minage = minage
        self.entryprice = entryprice
        self.url = url

    def json(self):
        return {'id': self.id, 'event_name': self.event_name, 'venue': {'address': self.address, 'name': self.name, 'cityname': self.cityname, 'postcode': self.postcode, 'longitude': self.longitude, 'latitude': self.latitude},'business_id': self.business_id, 'description': self.description, 'event_type': self.event_type, 'date': self.date, 'openingtimes': {
            'doorsopen': self.doorsopen, 'doorsclose': self.doorsclose
        }, 'minage': self.minage, 'entryprice': self.entryprice, 'url': self.url  }

    @classmethod
    def find_by_name(cls, event_name):
        return cls.query.filter_by(event_name=event_name).first()

    @classmethod
    def find_by_id(cls, business_id):
        return cls.query.filter_by(business_id=business_id).all()  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
