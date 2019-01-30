from api_interfaces.translator_manager import TranslatorManager
from tkinter import *
from gui.style_constants import *




class TonguesTranslator(Tk):
    ''' Acts as the main window for the application, draws upon components in gui to build the interface
    '''
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Tongues Translator')
        self.geometry(DEFAULT_WINDOW_SIZE)

        self.call('wm', 'iconphoto', self._w, PhotoImage(file='media/icon.png'))

        self.mainloop()

if __name__=='__main__':
    window = TonguesTranslator()