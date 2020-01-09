from flask_restful import Resource, reqparse
from models.user import UserModel


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
    parser.add_argument('email', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('age', type=int, required=True, help="This field cannot be blank")
    parser.add_argument('location', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('option_1', type=str, help="This field cannot be blank")
    parser.add_argument('option_2', type=str, help="This field cannot be blank")
    parser.add_argument('option_3', type=str, help="This field cannot be blank")
    parser.add_argument('option_4', type=str, help="This field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['email'], data['age'], data['password'], data['location'], data['option_1'], data['option_2'],data['option_3'],data['option_4'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
