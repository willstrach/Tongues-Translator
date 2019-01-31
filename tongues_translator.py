from api_interfaces.translator_manager import TranslatorManager
from tkinter import *
from gui.style_constants import *
from gui.sidebar import SideBar
from gui.instant_translate import InstantTranslatePage
from gui.test_page import TestPage



class TonguesTranslator(Tk):
    ''' Acts as the main window for the application, draws upon components in gui to build the interface
    '''
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Tongues Translator')
        self.geometry(DEFAULT_WINDOW_SIZE)

        self.call('wm', 'iconphoto', self._w, PhotoImage(file='media/icon.png'))
        self.sidebar = SideBar()
        self.pages = {}

        self.add_page('Instant Translate', InstantTranslatePage(self, translator=TranslatorManager()))
        self.mainloop()

    def add_page(self, name, page):
        ''' add a page to the application. If no pages currently exist, the page will also be shown.

        Args:
            name (str): The name of the page, used to identify the page
            page (obj): A tkinter object containing the page to be added
        '''
        self.pages[name] = page
        self.sidebar.add_button('btn_' + name, name, TOP)
        self.sidebar.buttons['btn_' + name].bind_function(lambda event: (self.show_page(name)))
        if len(self.pages) == 1:
            self.show_page(name)
        

    def show_page(self, name):
        ''' Shows a named page

        Args:
            name (str): the name of the page to be shown
        '''
        self.sidebar.focus_button('btn_' + name)
        self.hide_all_pages()
        self.pages[name].show()

    def hide_all_pages(self):
        ''' Hides all pages in TonguesTranslator window'''
        for key, page in self.pages.items():
            page.hide()

if __name__=='__main__':
    window = TonguesTranslator()