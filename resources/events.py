from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.events import EventsModel


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
    parser.add_argument('business_id',
                        type=str,
                        required=True,
                        help="Every event needs a business_id."
                        )                    
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
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class EventList(Resource):
    def get(self):
        return {'events': list(map(lambda x: x.json(), EventsModel.query.all()))}

# class EventByID(Resource):
#     def get(self, business_id):
#         return {'events': list(map(lambda x: x.json(), EventsModel.query.find_by_id()))}

class EventPoster(Resource):
    def post(self):

        data = Event.parser.parse_args()

        event = EventsModel(**data)

        try:
            event.save_to_db()
        except:
            return {"message": "An error occurred inserting the event."}, 500

        return event.json(), 201