from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self.root = root
        self._entry_sweet = None
        self._entry_salty = None
        self._entry_skip = None
        self._entry_continue = None
        self._entry_end = None

    def tklinter_welcome(self):
        label = ttk.Label(master=self._root, text="tervettuliaisliibalaaba")
        
        button_sweet = ttk.Button(master=self._root, text="Makeaa", command=lambda: self._button_clicked("b"))
        button_salty = ttk.Button(master=self._root, text="Suolaista", command=lambda: self._button_clicked("c"))
        button_skip = ttk.Button(master=self._root, text="En tiedä", command=lambda: self._button_clicked(""))

        label.grid(row=0, column=0, columnspan=2)
        button_sweet.grid(row=1, column=0)
        button_salty.grid(row=1, column=1)
        button_skip.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W))

    def button_clicked(self, sweet_or_salty):
        value_sweet = self._entry_sweet.get()
        value_salty = self._entry_salty.get()
        value_skip = self._entry_skip.get()

    def tklinter_continue(self):
        pass

    def second_choice(self, yes_or_no):
        pass

    def end(self):
        pass