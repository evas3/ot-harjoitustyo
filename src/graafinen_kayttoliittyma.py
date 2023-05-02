from tkinter import Tk, ttk, constants

class UI:
    """Luokka graafista käyttöliittymää varten.
    """

    def __init__(self, root):
        """Alustaa nappulat
        
        Args:
            root: ttk alustusta
        """

        self._root = root
        self._entry_sweet = None
        self._entry_salty = None
        self._entry_skip = None
        self._entry_continue = None
        self._entry_end = None

    def tklinter_welcome(self):
        """Tervehtii käyttäjää
            ensimmäinen näkymä
        """

        label = ttk.Label(master=self._root, text="Can't make good decisions? I can! (ei vielä tee mitään)")
        label_2 = ttk.Label(master=self._root, text="Would you like to bake or cook?")
        
        button_sweet = ttk.Button(master=self._root, text="Makeaa", command=lambda: self._button_clicked(1))
        button_salty = ttk.Button(master=self._root, text="Suolaista", command=lambda: self._button_clicked(2))
        button_skip = ttk.Button(master=self._root, text="En tiedä", command=lambda: self._button_clicked(""))

        label.grid(row=0, column=0, columnspan=2)
        label_2.grid(row=1, column=0, columnspan=2)
        button_sweet.grid(row=2, column=0)
        button_salty.grid(row=2, column=1)
        button_skip.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W))

    def _button_clicked(self, sweet_or_salty):
        """Käsittelee napinpainalluksen.
        
        Args:
           sweet_or_salty: käyttäjän nappivalinta
        """

        pass

    def tklinter_continue(self):
        """Kysytään käyttäjältä haluaako jatkaa.
        """
        pass

    def second_choice(self):
        """Jos käyttäjä jatkaa.
        """

        pass

    def end(self):
        """Jos käyttäjä ei jatka.
        """

        pass