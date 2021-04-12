from dearpygui.core import *
from dearpygui.simple import *

from src.ui.UI import *
from src.ui.Preview import *


class Advanced:
    @staticmethod
    def show():
        """
        Shows the "Advanced" options

        @return:
        """
        AdvancedValue = get_value('AdvancedCheckbox')

        items = ['ClientIDInput', 'LargeImageInput', 'SmallImageInput', 'LargeImageTextInput', 'SmallImageTextInput',
                 'AdvancedSep',
                 'ClientIDInputTitle', 'LargeImageInputTitle', 'SmallImageInputTitle', 'LargeImageTextInputTitle',
                 'SmallImageTextInputTitle']

        if AdvancedValue is True:
            Inputs.create('ClientIDInput', 'LARGE', 'ClientID', parent='ExtraFields')

            Inputs.create('LargeImageInput', 'LARGE', 'Large image', parent='ExtraFields')
            Inputs.create('SmallImageInput', 'LARGE', 'Small image', parent='ExtraFields')

            Inputs.create('LargeImageTextInput', 'LARGE', 'Large image text', parent='ExtraFields')
            Inputs.create('SmallImageTextInput', 'LARGE', 'Small image text', parent='ExtraFields')

            set_item_callback('ClientIDInput', Preview.refresh)
            set_item_callback('LargeImageInput', Preview.refresh)
            set_item_callback('SmallImageInput', Preview.refresh)
            set_item_callback('LargeImageTextInput', Preview.refresh)
            set_item_callback('SmallImageTextInput', Preview.refresh)

            add_separator(name='AdvancedSep', parent='ExtraFields')
        else:
            for item in items:
                delete_item(item)
