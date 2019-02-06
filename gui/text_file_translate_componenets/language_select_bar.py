from tkinter import *
from gui.style_constants import *
from gui.shared_components.language_selector import LanguageSelector



class LanguageSelectBar(Frame):
    ''' '''
    def __init__(self, master, language_dict={}, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.language_dict = language_dict
        self.config(
            bg=MAIN_COLOUR
        )

        self.from_label = Label(self, text='From:', bg=MAIN_COLOUR)
        self.to_label = Label(self, text='To:  ', bg=MAIN_COLOUR)

        self.from_lang = LanguageSelector(self, True, self.language_dict)
        self.to_lang = LanguageSelector(self, False, self.language_dict)

        self.from_label.pack(
            padx=20,
            pady=10,
            side=LEFT
        )

        self.from_lang.pack(
            padx=20,
            pady=10,
            side=LEFT
        )

        self.to_lang.pack(
            padx=20,
            pady=10,
            side=RIGHT
        )

        self.to_label.pack(
            padx=20,
            pady=10,
            side=RIGHT
        )

        self.pack(
            side=TOP,
            fill=BOTH
        )