from tkinter import *
from gui.style_constants import *
from gui.shared_components.language_selector import LanguageSelector 


class PanelTopBar(Frame):
    ''' The top bar of a translate panel

    Args:
        to_from (str): A string with a value of 'to' or 'from' to define the type of translate panel
    '''  
    def __init__(self, master, to_from, language_dict, *args, **kwargs):
        Frame.__init__(self, master=master, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR
        )
        self.pack(
            side=TOP,
            fill=BOTH
        )


        self.lbl_language = Label(self)
        self.lbl_language.config(
            text='To:  ' if to_from == 'to' else 'From:',
            bg=MAIN_COLOUR
        )
        self.lbl_language.pack(
            side=LEFT,
            padx=30
        )

        self.btn_language = LanguageSelector(self, include_detect=True if to_from == 'from' else False, language_dict=language_dict)
        self.btn_language.pack(
            side=LEFT,
            padx=30
        )

        if to_from == 'to':
            self.btn_translate = Button(self)
            self.btn_translate.config(
                text='Translate',
                width=20,
                height=2,
                relief=SUNKEN,
                borderwidth=0,
                highlightthickness=0,
                bg=HIGHLIGHT_COLOUR
            )
            self.btn_translate.pack(
                side=RIGHT,
                padx=30
            )
        
        if to_from == 'from':
            self.html_bool = IntVar()
            self.cb_html = Checkbutton(self, variable=self.html_bool)
            self.cb_html.config(
                text='Contains HTML tags',
                relief=SUNKEN,
                borderwidth=0,
                highlightthickness=0,
                bg=MAIN_COLOUR
            )
            self.cb_html.pack(
                side=RIGHT,
                padx=30
            )

class TranslatePanel(Frame):
    ''' A panel to act as the top and bottom of the instant translate page
    
    Args:
        to_from (str): A string with a value of 'to' or 'from' to define the type of translate panel
    '''

    def __init__(self, master, to_from, language_dict, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR
        )

        self.pack(
            side=TOP,
            fill=BOTH,
            expand=True
        )

        self.top_bar = PanelTopBar(self, to_from=to_from, language_dict=language_dict)

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
        self.text_box.pack(
            side=TOP,
            fill=BOTH,
            expand=True,
            padx=20,
            pady=10
        )
        self.text_box.bind('<Control-a>', self.callback)
    
    def callback(self, event):
        self.after(50, self.select_all, event.widget)

    def select_all(self, widget):
        widget.tag_add(SEL, "1.0", END)
        widget.mark_set(INSERT, "1.0")
        widget.see(INSERT)
        return 'break'