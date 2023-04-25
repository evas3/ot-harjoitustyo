import unittest
from recipes import Recipes


class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipes = Recipes()

    def test_welcome_input_m(self):
        self.assertEqual(self.recipes.welcome("m"), recipes.sweet())