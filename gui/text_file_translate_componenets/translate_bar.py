from tkinter import *
from gui.style_constants import *
from gui.shared_components.styled_button import StyledButton


class TranslateBar(Frame):
    ''' A horizontal bar containing to and from language selectors '''
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR
        )
        self.html_bool = BooleanVar()
        self.translate_button = StyledButton(self, text='Translate', width=20)
        self.translate_button.pack(
            side=RIGHT,
            padx=30
        )

        self.cb_html = Checkbutton(self, variable=self.html_bool)
        self.cb_html.config(
            text='Contains HTML tags',
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=MAIN_COLOUR
        )
        self.cb_html.pack(
            side=LEFT,
            padx=30
        )

        self.pack(
            side=BOTTOM,
            fill=BOTH
        )