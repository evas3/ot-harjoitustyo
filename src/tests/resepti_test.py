import unittest
from recipes import Recipes


class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipes()

    def test_welcome_input_b(self):
        self.assertEqual(self.recipe.welcome("b"), recipe.sweet())

    def test_welcome_input_c(self):
        self.assertEqual(self.recipe.welcome("c"), recipe.salty())

    def test_welcome_input_(self):
        self.assertEqual(self.recipe.welcome(""), recipe.sweet())

    def test_welcome_input_x(self):
        self.assertEqual(self.recipe.welcome("x"), recipe.sweet())


if __name__ == "__main__":
    unittest.main()
