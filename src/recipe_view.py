from tkinter import ttk, constants


class RecipeView:
    """Luokka reseptien tulostamisnäkymää varten
    """


    def __init__(self, root, file):
        """Alustaa näkymän.

        Args:
           root: ttk alustusta
           file: luettava tiedosto
        """

        self._root = root
        self._frame = None
        self.recipe = file

        self._initialize()


    def pack(self):
        """Näyttää senhetkisen näkymän.
        """

        self._frame.pack(fill=constants.X)


    def destroy(self):
        """Tuhoaa senhetkisen näkymän.
        """

        self._frame.destroy()


    def _initialize(self):
        """Lukee tiedoston sisällön
        """

        self._frame = ttk.Frame(master=self._root)
        instructions = open(self.recipe)
        print(instructions.read())