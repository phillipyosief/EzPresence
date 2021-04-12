from dearpygui.core import *
from dearpygui.simple import *

from src.ui.UI import *
from src.ui.Advanced import *
from src.ui.UseButtons import *

from src.backend.rpc import *


class Footer:
    @staticmethod
    def row_1():
        """
        GUI Widget for the first row

        @return:
        """
        Buttons.create('StartRichPresenceButton', 'LARGE', 'Start RichPresence', RPC.start)

    @staticmethod
    def row_2():
        """
        GUI Widget for the second row

        @return:
        """
        Buttons.create('RefreshPreviewButton', 'MEDIUM', 'Refresh preview', None)
        add_same_line()
        Buttons.create('CloseRichPresenceButton', 'MEDIUM', 'Close RichPresence', None)

    @staticmethod
    def show():
        """
        Show the footer

        @return:
        """
        add_separator()

        Checkbox.create('AdvancedCheckbox', False, 'Advanced', Advanced.show,
                        'Click advanced to use images in \nyour RichPresence (Application required)')

        add_same_line()

        Checkbox.create('UseButtonsCheckbox', False, 'Use buttons', UseButtons.show, False)

        add_separator()

        Footer.row_1()
        Footer.row_2()
        end()
