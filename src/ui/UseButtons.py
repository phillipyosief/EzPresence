from dearpygui.core import *
from dearpygui.simple import *

from src.ui.UI import *
from src.ui.Preview import *


class UseButtons:
    @staticmethod
    def show():
        UseButtonsValue = get_value('UseButtonsCheckbox')

        items = ['ButtonsCode', 'UseButtonsSep',
                 'ButtonsCodeTitle']

        if UseButtonsValue is True:
            Editor.create(name='ButtonsCode', size='LARGE', label='Buttons',
                          hint='button1_label=http://button1.link\n=button2_label=http://button1.link',
                          parent='ExtraFields')
            set_item_callback('ButtonsCode', Preview.refresh)
            add_separator(name='UseButtonsSep', parent='ExtraFields')
        else:
            for item in items:
                delete_item(item)
