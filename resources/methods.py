from flask_restful import Resource, reqparse

class Methods(Resource):
  def get(self):
    return {'methods': {
        "GET /users": {
                "description": "get list of all users"
            }
        },
        " POST /register": {
                "description": "post a user",
                "example send": {
                    "username": "Bob",
                    "password": "Food12",
                    "email": "bob@bob.com",
                    "age": 12,
                    "location": "Manchester",
                    "option_1": "Food",
                    "option_2": "Music",
                    "option_3": "Drinking",
                    "option_4": "Family"
                }
            },
        
        " GET /users/username": {
        "description": "Get User by username"
            },

        " PATCH /users/username": {
        "description": "Patch User by username -  can patch location and quiz options",
        "example send": {
            "location": "Manchester",
            "option_1": "Food",
            "option_2": "Music",
            "option_3": "Drinking",
            "option_4": "Family"
        }
    },

        " DELETE /users/username": {
        "description": "Delete User by username"
    }
    }
