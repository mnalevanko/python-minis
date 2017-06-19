import unittest
from city_functions import city_country

class TestCityNames(unittest.TestCase):
    '''Tests for city_functions.py.'''

    def test_city_country(self):
        '''Do "Santiago" and "Chile" work?'''
        formatted_result = city_country('santiago', 'chile')
        self.assertEqual(formatted_result, "Santiago, Chile")

    def test_city_country_case_insentive(self):
        '''How about "medzIbROD" and "slovaKIA"'''
        formatted_result = city_country('medzIbROD', 'slovaKIA')
        self.assertEqual(formatted_result, "Medzibrod, Slovakia")

    def test_city_country_population(self):
        '''This time, we include a population parameter.'''
        result = city_country('santiago', 'chile', 5000000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000')

unittest.main()
