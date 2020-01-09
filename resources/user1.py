from flask_restful import Resource, reqparse
from security import UserModel


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
    parser.add_argument('email', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('age', type=int, required=True,
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

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'], data['email'], data['age'],
                         data['location'], data['option_1'], data['option_2'], data['option_3'], data['option_4'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class GetAllUsers(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}


class GetUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location', type=str, required=True,
                        help="This field cannot be blank")
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
            user.location = data['location']
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
