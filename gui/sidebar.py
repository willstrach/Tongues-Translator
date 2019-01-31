from tkinter import *
from gui.style_constants import *
from gui.sidebar_components.sidebar_btn import SidebarBtn
from gui.sidebar_components.sidebar_btn_group import SidebarBtnGroup 


class SideBar(Frame):
    ''' The side bar for the application. This will be used for switching between pages
    '''
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.config(
            bg=HIGHLIGHT_COLOUR,
            width=18
        )

        self.buttons = {}
        self.button_groups = {}

        self.pack(
            side=LEFT,
            fill=BOTH,
            expand=False
        )
    


    def add_button(self, name, text, top_bottom=TOP):
        self.buttons[name] = SidebarBtn(self)
        self.buttons[name].config(
            text=text,
            height=2,
            width=18
        )

        self.buttons[name].pack(
            side=top_bottom
        )


    def focus_button(self, focus_name):
        for name, button in self.buttons.items():
            if name == focus_name:
                button.config(
                    bg=MAIN_COLOUR
                )
            else:
                button.config(
                    bg=HIGHLIGHT_COLOUR
                )


    def remove_button(self, name):
        self.buttons[name].destroy()
        self.buttons.pop(name)


    def add_button_group(self, name, top_bottom=TOP):
        self.button_groups[name] = SidebarBtnGroup(self)
        self.button_groups[name].pack(
            side=top_bottom
        )