import unittest
from recipes import Recipes


class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipes()

    def test_welcome_input_m(self):
        self.assertEqual(self.recipe.welcome("m"), recipe.sweet())

if __name__ == "__main__":
    unittest.main()