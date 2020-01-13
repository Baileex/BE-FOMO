from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.event_history import EventHistoryModel


class EventHist(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('sex',
                        type=str,
                        required=True,
                        help="Every event needs a gender."
                        )  
    parser.add_argument('event_type',
                        type=str,
                        required=True,
                        help="Every event needs an event_type."
                        )   
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="Every event needs a location."
                        )
    parser.add_argument('time',
                        type=str,
                        required=True,
                        help="Every event needs a time."
                        ) 
    # @jwt_required()
    # def get(self, id):
    #     event = EventHistoryModel.find_by_id(id)
    #     if event:
    #         return event.json()
    #     return {'message': '`Event` not found'}, 404

    def post(self):
        data = EventHist.parser.parse_args()       

        event = EventHistoryModel(data['age'], data['sex'], data['event_type'], data['location'], data['time'])
        event.save_to_db()

        return {"message": "Event History stored successfully."}, 201

    def get(self):
        return {'event_history': list(map(lambda x: x.json(), EventHistoryModel.query.all()))}

    # def patch(self, name):
    #     data = Event.parser.parse_args()

    #     event = EventsModel.find_by_name(name)

    #     if event:
    #         event.name = data['name']
    #         event.location = data['location']
    #         event.description = data['description']
    #         event.event_type = data['event_type']
    #         event.date = data['date']
    #         event.time = data['time']
    #         event.min_age = data['min_age']
    #         event.cost = data['cost']

    #     event.save_to_db()

    #     return event.json()


class EventHistDelete(Resource):
    def delete(self, id):
        event = EventHistoryModel.find_by_id(id)
        if event:
            event.delete_from_db()
            return {'message': 'Event deleted.'}
        return {'message': 'Event not found.'}, 404
    

class EventHistByType(Resource):
    def get(self, event_type):
        events = EventHistoryModel.find_by_event_type(event_type)
        return {'event_history': list(map(lambda x: x.json(), events))}

class EventHistByLocation(Resource):
    def get(self, location):
        events = EventHistoryModel.find_by_location(location)
        return {'event_history': list(map(lambda x: x.json(), events))}

# class EventHistoryPoster(Resource):
#     def post(self, business_id):
    
#       business = BusinessModel.find_by_id(business_id)
      
#       if business:
#         data = Event.parser.parse_args()
#       else:
#         return {'message': 'business does not exist'}, 404  
        
#       if EventsModel.find_by_name(data['name']):
#          return {'message': "An event with name '{}' already exists.".format(data['name'])}, 400
            
#       event = EventsModel(data['name'], data['location'], business_id, data['description'], data['event_type'], data['date'], data['time'], data['min_age'], data['cost'])

#       try:
#         event.save_to_db()
#       except:
#         return {"message": "An error occurred inserting the event."}, 500

#       return event.json(), 201