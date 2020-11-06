import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Paris", "France", True)

    def test_city_has_name(self):
        self.assertEqual("Paris", self.city.name)