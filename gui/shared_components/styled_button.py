from tkinter import *
from gui.style_constants import *



class StyledButton(Button):
    ''' A button to be used to ensure consistency accross app '''
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.config(
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=HIGHLIGHT_COLOUR,
            height=2
        )