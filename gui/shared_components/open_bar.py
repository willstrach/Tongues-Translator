from tkinter import *
from tkinter import filedialog
from gui.shared_components.styled_button import StyledButton
from gui.style_constants import *


class OpenBar(Frame):
    ''' A horizontal bar containing file open elements '''
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.config(
            bg=MAIN_COLOUR
        )

        self.open_button = StyledButton(self, text='Open', width=20)
        self.open_name = Label(self, text='Open a file...', bg=MAIN_COLOUR)

        self.open_button.pack(
            side=LEFT
        )
        self.open_name.pack(
            side=LEFT,
            padx=20
        )
        


        self.pack(
            side=TOP,
            fill=BOTH,
            padx=20,
            pady=10
        )