import unittest
from recipes import Recipes


class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipes()

    def test_setup_sweet(self):
        self.assertEqual(len(self.dessert), 3)

    def test_setup_salty(self):
        self.assertEqual(len(self.meal), 3)

    def test_welcome_input_1(self):
        self.assertEqual(self.recipe.welcome(1), self.recipe.sweet())

    def test_welcome_input_2(self):
        self.assertEqual(self.recipe.welcome(2), self.recipe.salty())

    def test_welcome_input_(self):
        self.assertEqual(self.recipe.welcome(0), self.recipe.sweet() or self.recipe.salty())

    def test_welcome_input_x(self):
        self.assertEqual(self.recipe.welcome("x"), self.recipe.sweet())


if __name__ == "__main__":
    unittest.main()
