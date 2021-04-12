from dearpygui.core import *
from dearpygui.simple import *

import getpass

from resources.properties import *

from src.ui.UI import *


class About:
    @staticmethod
    def close():
        """
        Just close the "About" Popup

        @return:
        """
        close_popup('About')

    @staticmethod
    def show():
        """
        Shows the "About" popup with all GUI content

        @return:
        """
        add_image('AboutIcon', value=f'C:/Users/{getpass.getuser()}/AppData/Local/Temp/ezpresence_icon.png',
                  width=128, height=128)

        add_text(f'          {Product.Name}')
        add_text(f'               v{Product.Version}')
        add_text(f'            {Product.Author}')
        add_text(f'       {Product.Website}')

        add_spacing(count=3)

        add_text('UsedLibraries', default_value='         Used libraries', tip='Click to see the used libraries')

        add_separator()
        Buttons.create('CloseAboutButton', 'CUSTOM', 'Close', callback=About.close, custom_size=Size.ButtonSizeSmall + 30)