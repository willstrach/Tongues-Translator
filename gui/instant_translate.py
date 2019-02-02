from tkinter import *
from gui.style_constants import *
from gui.shared_components.language_selector import LanguageSelector
from api_interfaces.translator_manager import TranslatorManager




class InstantTranslatePage(Frame):
    ''' A page for translating a single string, matches the look and feel of online solutions

    Args:
        translator (obj: TranslatorManager): The translator to be used to handle translations for the page
    '''
    def __init__(self, master, translator, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR,
            highlightthickness=10,
            highlightbackground=MAIN_COLOUR
        )
        self.translator = translator
        self.language_selector = LanguageSelector(self, True, self.translator.get_supported_languages())
        self.language_selector.pack()

    def show(self):
        ''' Show the page '''
        self.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True
        )
    
    def hide(self):
        ''' Hide the page '''
        self.pack_forget()