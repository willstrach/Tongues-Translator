from tkinter import *
from gui.style_constants import *
from gui.shared_components.styled_button import StyledButton
from gui.shared_components.open_bar import OpenBar
from gui.text_file_translate_componenets.language_select_bar import LanguageSelectBar
from gui.text_file_translate_componenets.translate_bar import TranslateBar 
from gui.text_file_translate_componenets.save_output import SaveOutput
from tkinter import filedialog
from api_interfaces.translator_manager import TranslatorManager
import os


class TextFileTranslate(Frame):
    ''' A page to be used for translating plain text files e.g. HTML, TXT, etc.

    Args:
        master (obj: tkinter.Widget): A tkinter widget object specifying the parent of the page
        translator (obj:TranslatorManager): A translator to handle all translations
    '''
    def __init__(self, master, translator, *args, **kwargs):
        Frame.__init__(self, master=master, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR
        )
        self.translator = translator
        self.open_bar = OpenBar(self)
        self.open_bar.open_button.bind('<Button-1>', self.open_file)
        self.language_select_bar = LanguageSelectBar(self, self.translator.get_supported_languages())

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
        self.translate_bar = TranslateBar(self)
        self.translate_bar.translate_button.bind('<Button-1>', self.translate_click)


    def callback(self, event):
        ''' A method to be called when ctrl-a is hit 
        
        Args:
            event (tkinter.event): A tkinter event that triggered the function call
        '''
        self.after(50, self.select_all, event.widget)

    def select_all(self, widget):
        ''' A method to select all content in a text box

        Args:
            widget (tkinter.Text): The tkinter textbox containg the text to be selected
        '''
        widget.tag_add(SEL, "1.0", END)
        widget.mark_set(INSERT, "1.0")
        widget.see(INSERT)
        return 'break'

    def show(self):
        ''' Show the page '''
        self.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True
        )
    
    def hide(self):
        ''' Hide the page '''
        self.pack_forget()

    def open_file(self, event):
        ''' A method to launch an open file dialogue 
        Args:
            event (tkinter.event): A tkinter event that triggered the function call
        '''
        cwd = os.getcwd()
        filename = filedialog.askopenfilename(initialdir =cwd,title = 'Select file')
        with open(filename, 'r') as f:
            self.text_box.delete('1.0', END)
            self.text_box.insert(END, f.read())
        self.open_bar.open_name.config(text=filename)

    def translate_click(self, event):
        ''' Translate the text in the text box, and launch a save window 
        Args:
            event (tkinter.event): A tkinter event that triggered the function call
        '''
        translate_string = "\r\n".join(self.text_box.get('1.0', END).split("\n"))
        from_language = self.language_select_bar.from_lang.language
        to_language = self.language_select_bar.to_lang.language
        html_tags = bool(self.translate_bar.html_bool.get())
        translated_string = self.translator.translate(translate_string, translate_from=from_language, translate_to=[to_language], html=True)[to_language]

        save_window = SaveOutput(translated_string)