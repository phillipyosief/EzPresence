from dearpygui.core import *
from dearpygui.simple import *

from src.ui.UI import *
from src.ui.MenuBar import *
from src.ui.Preview import *
from src.ui.Footer import *


class Main:
    @staticmethod
    def show():
        """
        Main function to sort all gui functions here

        @return:
        """
        with window('MainWindow',
                    no_resize=True,
                    no_title_bar=True):
            set_main_window_size(width=Size.MainWidth, height=Size.MainHeight)
            MenuBar.show()

            Inputs.create('DetailsInput', size='LARGE', label='Details')
            Inputs.create('StateInput', size='LARGE', label='State')

            set_item_callback('StateInput', Preview.refresh)
            set_item_callback('DetailsInput', Preview.refresh)

            add_separator()

            add_child('ExtraFields', height=307, autosize_x=True, border=False)
            end()

            Preview.show()

            Footer.show()
            try:
                add_additional_font('C:/Windows/Fonts/arial.ttf')
            except:
                pass