from flask_restful import Resource, reqparse
from models.business import BusinessModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

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

class BusinessLogin(Resource):
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
    @classmethod   
    def post(cls):
        data = cls.parser.parse_args()

        business = BusinessModel.find_by_username(data['username'])

        if business and safe_str_cmp(business.password, data['password']):
            access_token = create_access_token(identity=business.id, fresh=True)
            refresh_token = create_refresh_token(business.id)
            return {
                'message': 'Business User logged in',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        
        return {'message': 'Invalid credentials'}, 401



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

        return {"message": "Password successfully updated."}, 201

class ChangeBusUsername(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        help="This field cannot be blank."
                        )

    def patch(self, business_name):
        data = ChangeBusUsername.parser.parse_args()

        business = BusinessModel.find_by_business_name(business_name)

        if business:
            business.username = data['username']

        business.save_to_db()
        return {"message": "Username successfully updated"}, 201

class ChangeBusDetails(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('business_name', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('address', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('description', type=str,
                        help="This field cannot be blank")

    def patch(self, business_name):
        data = ChangeBusDetails.parser.parse_args()

        business = BusinessModel.find_by_business_name(business_name)

        if business:
            business.email = data['email']
            business.business_name = data['business_name']
            business.address = data['address']
            business.description = data['description']

        business.save_to_db()
        return {"message": "Business details successfully updated"}, 201