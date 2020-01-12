from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_raw_jwt
from models.user1 import UserModel
from blacklist import BLACKLIST



class UserRegister(Resource):
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
    parser.add_argument('email', type=str,     required=True,
                        help="This field cannot be blank")
    parser.add_argument('age', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('location', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('option_1', type=str,
                        help="This field cannot be blank")
    parser.add_argument('option_2', type=str,
                        help="This field cannot be blank")
    parser.add_argument('option_3', type=str,
                        help="This field cannot be blank")
    parser.add_argument('option_4', type=str,
                        help="This field cannot be blank")
    parser.add_argument('family', type=bool,
                        default=False)
    parser.add_argument('gender', type=str,
                        help="This field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], UserModel.generate_hash(data['password']), data['email'], data['age'], data['location'], data['option_1'], data['option_2'], data['option_3'], data['option_4'], data['family'], data['gender'])

        user.save_to_db()

        return user.json(), 201

class UserLogin(Resource):
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

        user = UserModel.find_by_username(data['username'])

        if user and UserModel.verify_hash( data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'message': 'User logged in',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        
        return {'message': 'Invalid credentials'}, 401

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200

class GetAllUsers(Resource):
    # @jwt_required
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}


class GetUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('option_1', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('option_2', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('option_3', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('option_4', type=str, required=True,
                        help="This field cannot be blank")

    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def patch(self, username):
        data = GetUser.parser.parse_args()

        user = UserModel.find_by_username(username)

        if user:
            user.option_1 = data['option_1']
            user.option_2 = data['option_2']
            user.option_3 = data['option_3']
            user.option_4 = data['option_4']

        user.save_to_db()

        return {"message": "User successfully updated."}, 201

    def delete(self, username):
        user = UserModel.find_by_username(username)

        if user:
            user.delete_from_db()
            return {'message': "User deleted."}
        return {'message': 'User not found.'}, 404

class ChangePassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        help="This field cannot be blank."
                        )
    
    def patch(self, username):
        data = ChangePassword.parser.parse_args()

        user = UserModel.find_by_username(username)

        if user:
            user.password = data['password']

        user.save_to_db()

        return {"message": "User successfully updated."}, 201

class ChangeUsername(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        help="This field cannot be blank."
                        )

    def patch(self, username):
        data = ChangeUsername.parser.parse_args()

        user = UserModel.find_by_username(username)

        if user:
            user.username = data['username']

        user.save_to_db()
        return {"message": "User successfully updated"}, 201

class ChangeLocation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location',
                        type=str,
                        help="This field cannot be blank."
                        )

    def patch(self, username):
        data = ChangeLocation.parser.parse_args()

        user = UserModel.find_by_username(username)

        if user:
            user.location = data['location']

        user.save_to_db()
        return {"message": "User successfully updated"}, 201
