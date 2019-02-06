from tkinter import *
from tkinter import filedialog
from gui.style_constants import *
from gui.shared_components.styled_button import StyledButton
import os


class SaveOutput(Tk):
    ''' A dialogue for reviewing, and saving, the outcome of the text_file_translate page
    
    Args:
        save_string (str): The string to be saved to file
    '''
    def __init__(self, save_string, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('800x800')
        self.save_string = save_string
        self.text_box = Text(self)
        self.text_box.config(
            bg=HIGHLIGHT_COLOUR,
            padx=10,
            pady=10,
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=5,
            highlightbackground=DARK_HIGHLIGHT_COLOUR
        )

        self.save_button = StyledButton(self, text='Save')

        self.text_box.insert('0.0', self.save_string)

        self.text_box.pack(side=TOP, fill=BOTH, expand=True)
        self.save_button.pack(side=RIGHT)

        self.save_button.bind('<Button-1>', self.save_click)

    def save_click(self, event):
        ''' Launches a save dialogue and saves the text to the named file. The window is then destroyed.
        
        Args:
            event (tkinter.event): A tkinter event that triggered the function call
        '''
        cwd = os.getcwd()
        f = filedialog.asksaveasfile(initialdir = cwd,title = 'Save as')
        f.write(str(self.save_string))
        f.close()
        self.destroy()        
