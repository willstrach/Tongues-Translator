from tkinter import *
from gui.style_constants import *

class SidebarBtnGroup(Frame):
    ''' A sidebar button group for adding small, side-by-side buttons to a sidebar 
    '''
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.config(
            bg=HIGHLIGHT_COLOUR,
        )

        self.buttons = {}
    
    def add_button(self, name, text):
        ''' Add a button to the button group

        Args:
            name (str): The name of the button, used for referencing it
            text (str): The text to be shown in the button
        '''
        self.buttons[name] = Button(self, text=text)
        self.buttons[name].config(
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=HIGHLIGHT_COLOUR
        )
        self.buttons[name].pack(
            side=LEFT
        )