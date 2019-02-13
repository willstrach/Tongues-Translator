from tkinter import *
from gui.style_constants import *



class LanguageSelector(Button):
    ''' A button for usage as a language selector. Clicking launches a window which allows language to be changed

    Args:
        include_detect (bool): Setting this to true will include the DETECT option in the language selector
        language_dict dict: a list of dictionaries in the form language_name:language_code
    '''
    def __init__(self, master, include_detect=False, language_dict={}, *args, **kwargs):
        Button.__init__(self, master=master, *args, **kwargs)
        self.language = None
        self.config(
            relief=SUNKEN,
            borderwidth=0,
            highlightthickness=0,
            bg=HIGHLIGHT_COLOUR,
            width=20,
            height=2
        )
        
        self.include_detect = include_detect
        self.config(text='Select language')
        self.language_dict = language_dict
        if include_detect:
            self.language_dict['DETECT'] = None
            self.language=None
            self.config(text='DETECT')
        else:
            self.language='en'
            self.config(text='English')

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

        def key_press(event):
            character = event.char
            if character.isalpha():
                index = [idx for idx, s in enumerate(language_list) if character == s[0].lower()][0]
                ls_listbox.selection_clear(0,END)
                ls_listbox.selection_set(index)
                ls_listbox.activate(index)
                ls_listbox.yview(index)

        language_selector_window = Toplevel(self.winfo_toplevel())
        language_selector_window.wait_visibility()
        language_selector_window.grab_set()
        language_selector_window.geometry('300x300')
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
        ls_listbox.bind('<Double-Button-1>', ok_click)
        ls_listbox.bind('<Return>', ok_click)
        ok_button.bind('<Button-1>', ok_click)
        ls_listbox.bind('<Key>', key_press)

        ls_listbox.pack(fill=BOTH, expand=True)
        ok_button.pack(fill=BOTH)
        
