from tkinter import *
from gui.style_constants import *
from gui.shared_components.language_selector import LanguageSelector
from gui.instant_translate_components.translate_panel import TranslatePanel

from api_interfaces.translator_manager import TranslatorManager




class InstantTranslatePage(Frame):
    ''' A page for translating a single string, matches the look and feel of online solutions

    Args:
        translator (obj: TranslatorManager): The translator to be used to handle translations for the page
    '''
    def __init__(self, master, translator, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.config(
            bg=MAIN_COLOUR
        )
        self.translator = translator
        self.top_panel = TranslatePanel(self, 'from', language_dict=self.translator.get_supported_languages())
        self.bottom_panel = TranslatePanel(self, 'to', language_dict=self.translator.get_supported_languages())
        self.bottom_panel.top_bar.btn_translate.bind('<Button-1>', self.translate_click)

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

    def translate_click(self, event):
        ''' The action to take when the translate button is clicked '''
        html_tags = bool(self.top_panel.top_bar.html_bool.get())
        from_language = self.top_panel.top_bar.btn_language.language
        to_language = self.bottom_panel.top_bar.btn_language.language
        translate_string = self.top_panel.text_box.get('1.0', END)
        
        translated_string = self.translator.translate(translate_string, translate_from=from_language, translate_to=[to_language], html=html_tags)[to_language]

        self.bottom_panel.text_box.delete('1.0', END)
        self.bottom_panel.text_box.insert(END, translated_string)