from tkinter import ttk, constants
import tkinter as tk

class RedoVieW:
    """Luokka 'valitaanko uudelleen' näkymää varten
    """


    def __init__(self, root, doable):
        """Alustaa näkymän.

        Args:
           root: ttk alustusta
           doable: kertoo jos joitakin reseptejä ei ole
        """

        self._root = root
        self._frame = None
        self.yes_or_no = 0
        self.doable = doable

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
        """Kuvaa redo näkymän tekstit, napit ja rakenteen.
        """

        self._frame = ttk.Frame(master=self._root)
        self.choise2 = tk.IntVar()
        style = ttk.Style()

        style.configure("clicked_button.TButton", background="green")
        style.configure("not_clicked.TButton")

        if self.doable == "sweet":
            label1 = ttk.Label(master=self._frame, text="No sweet options available", font="Helvetica 16")
            label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        if self.doable == "salty":
            label1 = ttk.Label(master=self._frame, text="No salty options available", font="Helvetica 16")
            label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
            
        label = ttk.Label(master=self._frame, text="Shall we try again?", font="Helvetica 16")
        
        self.button_yes = ttk.Button(master=self._frame, text="Yes", style="not_clicked.TButton", command=lambda: self._button2_clicked(1))
        self.button_no = ttk.Button(master=self._frame, text="No", style="not_clicked.TButton", command=lambda: self._button2_clicked(0))
        self.button_ok2 = ttk.Button(master=self._frame, text="OK", command=lambda: self.choise2.set(self.yes_or_no))

        label.grid(row=1, columnspan=2, padx=10, pady=10)
        self.button_yes.grid(row=3, column=1, columnspan=1, sticky=(constants.E, constants.W), padx=10, pady=10)
        self.button_no.grid(row=3, column=0, columnspan=1, sticky=(constants.E, constants.W), padx=10, pady=10)
        self.button_ok2.grid(columnspan=2, row=4, sticky=(constants.E, constants.W), padx=10, pady=10)


    def _button2_clicked(self, answer):
        """Käsittelee napinpainalluksen.
        
        Args:
           answer: käyttäjän nappivalinta
        """
        style = ttk.Style()
        style.configure("clicked_button.TButton", background="green")
        style.configure("not_clicked.TButton")
        if answer == 0:
            self.button_no.configure(style="clicked_button.TButton")
            self.button_yes.configure(style="not_clicked.TButton")
            self.yes_or_no = 0

        if answer == 1:
            self.button_yes.configure(style="clicked_button.TButton")
            self.button_no.configure(style="not_clicked.TButton")
            self.yes_or_no = 1