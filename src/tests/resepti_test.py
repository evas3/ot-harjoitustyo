import unittest
from reseptit import Reseptit


class TestReseptit(unittest, TestCase):
    def SetUp(self):
        self.recipe = Recipes()

    def test_welcome_input_m(self):
        self.assertEqual(self.recipe.welcome("m"), reseptit.sweet())
