from tkinter import ttk, constants, Text
import tkinter as tk


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
        self.add = tk.IntVar()

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

        label0 = ttk.Label(master=self._frame, text="(Scroll down to see the whole recipe)", font="Helvetica 10")
        label = ttk.Label(master=self._frame, text="When done add a note to this recipe", font="Helvetica 16")
        label_2 = ttk.Label(master=self._frame, text="Write the note below and press 'OK' or just press 'OK'", font="Helvetica 16")
        self.note = ttk.Entry(master=self._frame)
        self.button_add = ttk.Button(master=self._frame, text="OK", command=lambda: self._button_clicked())

        text = Text(self._frame)
        with open(self.recipe, 'r') as file:
            text.insert("end", chars=file.read())

        text.grid(padx=10, pady=10)
        label0.grid(padx=10, pady=10)
        label.grid(padx=10, pady=10)
        label_2.grid(padx=10, pady=10)
        self.note.grid(sticky=(constants.E, constants.W), padx=10, pady=10)
        self.button_add.grid(sticky=(constants.E, constants.W), padx=10, pady=10)


    def _button_clicked(self):
        """Käsittelee napin painamisen ja kirjoittaa huomion.
        """

        self.add.set(1)
        note_value = self.note.get()
        if note_value != "":
            file = open(self.file, 'a+')
            file.write('\n' + "NOTE: " + note_value)
            file.close()