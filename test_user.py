import unittest
import os
import json
import app
import db

class UsersTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app(config_name="testing")
        self.client = self.app.test_client
        self.bucketlist = {'name': 'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()