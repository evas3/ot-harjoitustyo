from recipe_view import RecipeView
from welcome_view import WelcomeView
from redo_view import RedoVieW


class UI:
    """Luokka graafista käyttöliittymää varten.
    """

    def __init__(self, root):
        """Alustaa näkymän.

        Args:
            root: ttk alustusta
        """

        self._root = root
        self._current_view = None

    def tklinter_welcome(self):
        """Kutsuu ensimmäistä näkymää.
        """

        return self._show_welcome_view()

    def _show_welcome_view(self):
        """Ensimmäinen näkymä
           tervehtii käyttäjää.

        Returns:
           Nappulavalinnan arvon.
        """

        self._hide_current_view()

        self._current_view = WelcomeView(self._root)
        self._current_view.pack()

        self._current_view.button_ok.wait_variable(self._current_view.choise)
        return self._current_view.choise.get()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän
        """

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def show_recipe_view(self, file):
        """Näyttää reseptinäkymän

        Args:
           file: luettava tiedosto
        """

        self._hide_current_view()

        self._current_view = RecipeView(self._root, file)
        self._current_view.pack()

        self._current_view.button_add.wait_variable(self._current_view.add)

    def show_redo_view(self, doable):
        """Näyttää 'yritetäänkö uudelleen' näkymän.

        Args:
           doable: kertoo jos reseptit ovat loppuneet

        Returns:
           Nappulavalinnan arvo.
        """

        self._hide_current_view()

        self._current_view = RedoVieW(self._root, doable)
        self._current_view.pack()

        self._current_view.button_ok2.wait_variable(self._current_view.choise2)
        return self._current_view.choise2.get()
