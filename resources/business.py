from flask_restful import Resource, reqparse
from models.business import BusinessModel

class BusinessRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('business_name', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('address', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('description', type=str,
                        help="This field cannot be blank")

    def post(self):
        data = BusinessRegister.parser.parse_args()

        if BusinessModel.find_by_business_name(data['business_name']):
            return {'message': "A business with name '{}' already exists.".format(data['business_name'])}, 400 #

        business = BusinessModel(data['username'], data['password'], data['email'], data['business_name'],
                         data['address'], data['description'])
        business.save_to_db()
            # except:
            #     return {"message": "An error occurred creating the store."}, 500

        return business.json(), 201

class Business(Resource):

        def get(self, business_name):
            business = BusinessModel.find_by_business_name(business_name)
            if business:
                return business.json()
            return {'message': 'business not found'}, 404

        def delete(self, business_name):
            business = BusinessModel.find_by_business_name(business_name)
            if business:
                business.delete_from_db()

            return {'message': 'business deleted'}


class GetAllBusinesses(Resource):
    def get(self):
        return {'businesses': list(map(lambda x: x.json(), BusinessModel.query.all()))}

class ChangeBusPassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        help="This field cannot be blank."
                        )
    
    def patch(self, business_name):
        data = ChangeBusPassword.parser.parse_args()

        business = BusinessModel.find_by_business_name(business_name)

        if business:
            business.password = data['password']

        business.save_to_db()

        return {"message": "Business successfully updated."}, 201