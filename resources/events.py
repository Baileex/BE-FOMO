from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.events import EventsModel
from models.business import BusinessModel


class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="Every event needs a location."
                        )
    # parser.add_argument('business_id',
    #                     type=str,
    #                     required=True,
    #                     help="Every event needs a business_id."
    #                     )                    
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="Every event needs a description."
                        )
    parser.add_argument('event_type',
                        type=str,
                        required=True,
                        help="Every event needs an event_type."
                        )       
    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="Every event needs a date."
                        )
    parser.add_argument('time',
                        type=str,
                        required=True,
                        help="Every event needs a time."
                        ) 
    parser.add_argument('min_age',
                        type=str,
                        required=True,
                        help="Every event needs a min_age."
                        )                     
    parser.add_argument('cost',
                        type=str,
                        required=True,
                        help="Every event needs a cost (can be zero)."
                        ) 
    # @jwt_required()
    def get(self, name):
        event = EventsModel.find_by_name(name)
        if event:
            return event.json()
        return {'message': '`Event` not found'}, 404

    

    def delete(self, name):
        event = EventsModel.find_by_name(name)
        if event:
            event.delete_from_db()
            return {'message': 'Event deleted.'}
        return {'message': 'Event not found.'}, 404

    def patch(self, name):
        data = Event.parser.parse_args()

        event = EventsModel.find_by_name(name)

        if event:
            event.name = data['name']
            event.location = data['location']
            event.description = data['description']
            event.event_type = data['event_type']
            event.date = data['date']
            event.time = data['time']
            event.min_age = data['min_age']
            event.cost = data['cost']

        event.save_to_db()

        return event.json()


class EventList(Resource):
    def get(self):
        return {'events': list(map(lambda x: x.json(), EventsModel.query.all()))}

class EventByID(Resource):
    def get(self, business_id):

        events = EventsModel.find_by_id(business_id)

        return {'events': list(map(lambda x: x.json(), events))}

class EventPoster(Resource):
    def post(self, business_id):
    
      business = BusinessModel.find_by_id(business_id)
      
      if business:
        data = Event.parser.parse_args()

      return {'message': 'business does not exist'}, 404  
        
        if EventsModel.find_by_name(data['name']):
            return {'message': "An event with name '{}' already exists.".format(data['name'])}, 400
            
        event = EventsModel(data['name'], data['location'], business_id, data['description'], data['event_type'], data['date'], data['time'], data['min_age'], data['cost'])

        try:
            event.save_to_db()
        except:
            return {"message": "An error occurred inserting the event."}, 500

        return event.json(), 201