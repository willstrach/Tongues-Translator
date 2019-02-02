from tkinter import *
from gui.style_constants import *


class LanguageSelector(Button):
    ''' A button for usage as a language selector. Clicking launches a window which allows language to be changed

    Args:
        include_detect (bool): Setting this to true will include the DETECT option in the language selector
        language_dict dict: a list of dictionaries in the form language_name:language_code
    '''
    def __init__(self, master, include_detect=False, language_dict={}, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.language = None
        self.config(
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=HIGHLIGHT_COLOUR
        )
        self.include_detect = include_detect
        self.config(text='Select language')
        self.language_dict = language_dict
        if include_detect:
            self.language_dict['DETECT'] = None

        self.bind('<Button-1>',self._button_click)

    def _button_click(self, event):
        ''' Launches the language selector window

        Args:
            event (str): The tkinter event type
        '''
        def ok_click(event):
            language_selection = ls_listbox.get(ls_listbox.curselection())
            self.config(text=language_selection)
            self.language = self.language_dict[language_selection]
            language_selector_window.destroy()

        language_selector_window = Tk()
        ls_listbox = Listbox(language_selector_window)
        language_list = sorted(list(self.language_dict.keys()))

        if self.include_detect:
            ls_listbox.insert(END, 'DETECT')
        for language in language_list:
            if language != 'DETECT':
                ls_listbox.insert(END, language)
                
        ok_button = Button(language_selector_window)
        ok_button.config(
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=HIGHLIGHT_COLOUR,
            text='Select'
        )

        ok_button.bind('<Button-1>', ok_click)

        ls_listbox.pack()
        ok_button.pack()

        language_selector_window.mainloop()
