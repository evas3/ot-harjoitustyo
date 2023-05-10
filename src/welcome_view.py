from tkinter import ttk, constants
import tkinter as tk


class WelcomeView:
    """Luokka graafisen käyttöliittymän aloitusnäkymälle.
    """

    def __init__(self, root):
        """Alustaa näkymän.

        Args:
           root: ttk alustusta
        """

        self._root = root
        self._frame = None
        self._final_choise = 0
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
        """Kuvaa aloitusnäkymän tekstit, napit ja rakenteen
        """

        self._frame = ttk.Frame(master=self._root)
        self.choise = tk.IntVar()
        style = ttk.Style()

        label = ttk.Label(
            master=self._frame, text="Don't know what to do? Would you like to bake or cook?",
            font="Helvetica 16")
        label_2 = ttk.Label(
            master=self._frame, text="Select one and press 'OK' or if not sure just press 'OK'",
            font="Helvetica 16")

        style.configure("clicked_button.TButton", background="green")
        style.configure("not_clicked.TButton")
        self.button_sweet = ttk.Button(
            master=self._frame, text="Bake", style="not_clicked.TButton",
            command=lambda: self._button_clicked("sweet"))
        self.button_salty = ttk.Button(
            master=self._frame, text="Cook", style="not_clicked.TButton",
            command=lambda: self._button_clicked("salty"))
        self.button_ok = ttk.Button(
            master=self._frame, text="OK", command=lambda: self.choise.set(self._final_choise))

        label.grid(columnspan=2, sticky=constants.W, padx=10, pady=10)
        label_2.grid(columnspan=2)
        self.button_sweet.grid(row=2, column=1, columnspan=1, sticky=(
            constants.E, constants.W), padx=10, pady=10)
        self.button_salty.grid(row=2, column=0, columnspan=1, sticky=(
            constants.E, constants.W), padx=10, pady=10)
        self.button_ok.grid(columnspan=2, row=3, sticky=(
            constants.E, constants.W), padx=10, pady=10)

    def _button_clicked(self, sweet_or_salty):
        """Käsittelee napinpainalluksen.

        Args:
           sweet_or_salty: käyttäjän nappivalinta
        """

        style = ttk.Style()
        style.configure("clicked_button.TButton", background="green")
        style.configure("not_clicked.TButton")

        if sweet_or_salty == "sweet":
            self.button_sweet.configure(style="clicked_button.TButton")
            self.button_salty.configure(style="not_clicked.TButton")
            self._final_choise = 1

        if sweet_or_salty == "salty":
            self.button_salty.configure(style="clicked_button.TButton")
            self.button_sweet.configure(style="not_clicked.TButton")
            self._final_choise = 2
            