import unittest
from recipes import Recipes
from tkinter import Tk
from graafinen_kayttoliittyma import UI


class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipes()

    def test_setup_sweet(self):
        self.assertEqual(len(self.recipe.dessert), 3)

    def test_setup_salty(self):
        self.assertEqual(len(self.recipe.meal), 3)

    def test_setup_test_indicator(self):
        self.assertEqual(self.recipe.test_indicator, 0)

    def test_welcome_input_1(self):
        self.recipe.welcome(1)
        self.assertEqual(self.recipe.test_indicator, 1)

    def test_welcome_input_2(self):
        self.recipe.welcome(2)
        self.assertEqual(self.recipe.test_indicator, 2)

    def test_welcome_input_(self):
        self.recipe.welcome(0)
        self.assertEqual(self.recipe.test_indicator, 0)

    def test_sweet_empty(self):
        self.recipe.dessert = []
        self.recipe.sweet()
        self.assertEqual(self.recipe.test_indicator, 3.2)

    def test_sweet(self):
        self.recipe.sweet()
        self.assertEqual(self.recipe.test_indicator, 3.1)

    def test_salty_empty(self):
        self.recipe.meal = []
        self.recipe.salty()
        self.assertEqual(self.recipe.test_indicator, 3.4)

    def test_salty(self):
        self.recipe.salty()
        self.assertEqual(self.recipe.test_indicator, 3.3)

    def test_redo_0(self):
        self.assertEqual(self.recipe.redo(0), "quit")

    def test_redo(self):
        self.assertEqual(self.recipe.redo("x", self.recipe.welcome(
            1)) or self.recipe.welcome(2) or self.recipe.welcome(0))


if __name__ == "__main__":
    unittest.main()
