import unittest
from app.models import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'jerry')
    