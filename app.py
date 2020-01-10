import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user1 import UserRegister, GetUser, GetAllUsers, ChangePassword, ChangeUsername, ChangeLocation, UserLogin
from resources.business import BusinessRegister, ChangeBusDetails, ChangeBusUsername, Business, GetAllBusinesses, ChangeBusPassword, BusinessLogin
# from resources.item import Item, ItemList
from resources.methods import Methods

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jess'
api = Api(app)



jwt = JWTManager(app)  # /auth

api.add_resource(Methods, '/')
api.add_resource(GetAllUsers, '/users')
api.add_resource(GetAllBusinesses, '/businesses')
api.add_resource(BusinessRegister, '/businesses/register')
api.add_resource(BusinessLogin, '/businesses/login')
api.add_resource(Business, '/businesses/<string:business_name>')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(GetUser, '/users/<string:username>')
api.add_resource(ChangePassword, '/users/<string:username>/password')
api.add_resource(ChangeBusPassword, '/businesses/<string:business_name>/password')
api.add_resource(ChangeBusDetails, '/businesses/<string:business_name>/details')
api.add_resource(ChangeBusUsername, '/businesses/<string:business_name>/username')
api.add_resource(ChangeUsername, '/users/<string:username>/username')
api.add_resource(ChangeLocation, '/users/<string:username>/location')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
