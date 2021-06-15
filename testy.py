import unittest
from datetime import timedelta
from parkomat import *
from parkomat import Parkomat
from wyjatki import *


    class Tests(unittest.TestCase):

# po wrzuceniu 2zl
self.P.change_current_time('2022', '11', '7', 12, 0, 1)
self.P.add_coin(2, 1)
self.assertEqual(self.Parkomat().get_current_time() + timedelta(hours=1), self.Parkomat().get_departure_time)
# po wrzuceniu 4zl
self.P.add_coin(2, 2)
self.assertEqual(self.Parkomat().get_current_time() + timedelta(hours=2), self.Parkomat().get_departure_time)
# po wrzuceniu 5zl
self.P.add_coin(5, 1)
self.assertEqual(self.Parkomat().get_current_time() + timedelta(hours=3), self.Parkomat().get_departure_time)
# po wrzuceniu 5zl
self.P.add_coin(5, 1)
self.assertEqual(self.Parkomat().get_current_time() + timedelta(hours=4), self.Parkomat().get_departure_time)

//
