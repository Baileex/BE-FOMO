from flask_restful import Resource, reqparse

class Methods(Resource):
  def get(self):
    return {'methods': {
        "GET /users": {
                "description": "get list of all users"
            }
        },
        "POST /register": {
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
                    "option_4": "Dance"
                    "family":
                    "DEFAULT false"
                    "gender":
                    "male"
                }
            },
        
        "GET /users/username": {
        "description": "Get User by username"
            },

        "PATCH /users/:username/location": {
        "description": "Patch User by username": {
            "username": "Manchester",

        }
    },

        "DELETE /users/:username": {
        "description": "Delete User by username"
    },


        "POST /login": {
        "description": "check username and password and receive an access key"
    },

       "POST /logout": {
        "description": "check username and password and receive and blacklist access key REQUIRED" 
       },

       "PATCH /users/:username/username": {
        "description": "Patch User Quiz results by username": {
            "option_1": "test",
            "option_2": "test",
            "option_3": "test",
            "option_4": "test"
        }
    },
    
      "DELETE /users/:username": {
        "description": "Delete user"
      },

      "PATCH /users/:username/password": {
          "description": "Change user password"
      }


    }
