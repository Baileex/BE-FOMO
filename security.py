from werkzeug.security import safe_str_cmp
from models.user1 import UserModel
from models.business import BusinessModel



def authenticate(username, password):
    user = UserModel.find_by_username(username)
    business = BusinessModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    if business and safe_str_cmp(business.password, password):
        return business

def identity(payload):
    user_id = payload['identity']
    business_id = payload['identity']
    if business_id:
        return UserModel.find_by_id(user_id)
    if user_id:
        return BusinessModel.find_by_id(business_id)

    
    
