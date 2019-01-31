from tkinter import *
from gui.style_constants import *
from api_interfaces.translator_manager import TranslatorManager




class InstantTranslatePage(Frame):
    def __init__(self, master, translator, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR,
            highlightthickness=10,
            highlightbackground=MAIN_COLOUR
        )

    def show(self):
        self.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True
        )
    
    def hide(self):
        self.pack_forget()