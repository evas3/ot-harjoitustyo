import unittest
from recipes import Recipes
from tkinter import Tk
from graafinen_kayttoliittyma import UI


class TestRecipes(unittest.TestCase):
    def setUp(self):
        recipe = Recipes()
        window = Tk()
        ui = UI(window)

    def test_setup_sweet(self):
        recipe = Recipes()
        self.assertEqual(len(recipe.dessert), 3)

    def test_setup_salty(self):
        recipe = Recipes()
        self.assertEqual(len(recipe.meal), 3)

    def test_setup_test_indicator(self):
        recipe = Recipes()
        self.assertEqual(recipe.test_indicator, 0)

    def test_welcome_input_1(self):
        recipe = Recipes()
        recipe.welcome(1)
        self.assertEqual(recipe.test_indicator, 1)

    def test_welcome_input_2(self):
        recipe = Recipes()
        recipe.welcome(2)
        self.assertEqual(recipe.test_indicator, 2)

    def test_welcome_input_(self):
        recipe = Recipes()
        recipe.welcome(0)
        self.assertEqual(recipe.test_indicator, 0)

    def test_sweet_empty(self):
        recipe = Recipes()
        recipe.dessert = []
        recipe.sweet()
        self.assertEqual(recipe.test_indicator, 3.2)

    def test_sweet(self):
        window = Tk()
        ui = UI(window)
        recipe = Recipes()
        recipe.sweet()
        self.assertEqual(recipe.test_indicator, 3.1)


    def test_salty_empty(self):
        recipe = Recipes()
        recipe.meal = []
        recipe.salty()
        self.assertEqual(recipe.test_indicator, 3.4)

    def test_salty(self):
        window = Tk()
        ui = UI(window)
        recipe = Recipes()
        recipe.salty()
        self.assertEqual(recipe.test_indicator, 3.3)

    def test_redo_0(self):
        window = Tk()
        ui = UI(window)
        recipe = Recipes()
        self.assertEqual(recipe.redo(0), "quit")

    def test_redo(self):
        recipe = Recipes()
        self.assertEqual(recipe.redo("x", recipe.welcome(1)) or recipe.welcome(2) or recipe.welcome(0))


if __name__ == "__main__":
    recipe = Recipes()
    window = Tk()
    ui = UI(window)
    unittest.main()