from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.events import EventsModel
from models.business import BusinessModel


class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('event_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="Every event needs a name."
                        )
    parser.add_argument('address',
                        type=str,
                        required=True,
                        help="Every event needs an address."
                        )
    parser.add_argument('cityname',
                        type=str,
                        required=True,
                        help="Every event needs a cityname."
                        )
    parser.add_argument('postcode',
                        type=str,
                        required=True,
                        help="Every event needs an address."
                        )
    parser.add_argument('latitude',
                        type=str,
                        help="Every event needs an address."
                        )
    parser.add_argument('longitude',
                        type=str,
                        help="Every event needs an address."
                        )
    parser.add_argument('doorsopen',
                        type=str,
                        help="Every event needs an address."
                        )
    parser.add_argument('doorsclose',
                        type=str,
                        help="Every event needs an address."
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
    parser.add_argument('minage',
                        type=str,
                        required=True,
                        help="Every event needs a min_age."
                        )                     
    parser.add_argument('entryprice',
                        type=str,
                        required=True,
                        help="Every event needs a cost (can be zero)."
                        )
    parser.add_argument('url', type=str,
                        default="https://blogmedia.evbstatic.com/wp-content/uploads/wpmulti/sites/3/2016/12/16131147/future-phone-mobile-live-events-technology-trends.png")
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
            event.event_name = data['event_name']
            event.name = data['name']
            event.address = data['address']
            event.cityname = data['cityname']
            event.postcode = data['address']
            event.description = data['description']
            event.event_type = data['event_type']
            event.date = data['date']
            event.doorsopen = data['doorsopen']
            event.doorsclose = data['doorsclose']
            event.minage = data['minage']
            event.entryprice = data['entryprice']
            event.url = data['url']

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
      else:
        return {'message': 'business does not exist'}, 404  
        
      if EventsModel.find_by_name(data['event_name']):
         return {'message': "An event with name '{}' already exists.".format(data['event_name'])}, 400
            
      event = EventsModel(data['event_name'], data['name'], business_id, data['description'], data['address'], data['cityname'], data['postcode'], data['event_type'], data['date'], data['doorsopen'], data['doorsclose'], data['minage'], data['entryprice'], data['url'], data['longitude'], data['latitude'])

      try:
        event.save_to_db()
      except:
        return {"message": "An error occurred inserting the event."}, 500

      return event.json(), 201