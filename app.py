import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user1 import UserRegister, GetUser, GetAllUsers, ChangePassword
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.methods import Methods

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jess'
api = Api(app)



jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Methods, '/')
api.add_resource(GetAllUsers, '/users')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(GetUser, '/users/<string:username>')
api.add_resource(ChangePassword, '/users/<string:username>/password')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
