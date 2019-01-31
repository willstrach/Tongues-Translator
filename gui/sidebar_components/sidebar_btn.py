from tkinter import *
from gui.style_constants import *


class SidebarBtn(Button):
    ''' A button component for use in the application sidebar
    ''' 
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.config(
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=HIGHLIGHT_COLOUR
        )
    
    def bind_function(self, function):
        ''' Bind a function to the button

        Args:
            event_type (str): The tkinter event type
            function (function): A function object to bind to the button 
        '''
        self.bind('<Button-1>', function)