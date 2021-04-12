from dearpygui.simple import *
from dearpygui.core import *

import webbrowser
import platform

from src.ui.UI import *

from resources.console.error import internal
from resources.properties import *


class Bugreport:
    @staticmethod
    def github_issue():
        title = '[Bug]%20' + get_value('BugTitleInput')
        body = f'%23%23%23%23%20Description%0A' \
               f'%23%23%23%23%23%23%20{get_value("BugDescriptionInput")}%0A' \
               f'%23%23%23%23%20Environment%0A' \
               f'%20*%20{Product.Name}%0A' \
               f'%20*%20Platform:%20{platform.system()}%0A' \
               f'%20*%20Arch:%20{platform.architecture()[0]}%0A' \
               f'%20*%20OS%20Version:%20{platform.version()}%0A' \
               f'%20*%20Python%20Version:%20{platform.python_version()}%0A' \
               f'%20*%20Proccesor:%20{platform.processor()}%0A' \
               f'%20*%20App%20Version:%20{Product.Version}'

        if get_value('BugTitleInput') == '':
            internal.error('ERROR', 'MenuBar.py', 'github_issue',
                           'Title or description are not allowed to be empty', 'GUI',
                           'ERROR')
        elif get_value('BugDescriptionInput') == '':
            internal.error('ERROR', 'MenuBar.py', 'github_issue',
                           'Title or description are not allowed to be empty', 'GUI',
                           'ERROR')
        else:
            webbrowser.open(f'http://github.com/philliphqs/EzPresence/issues/new?body={body}&title={title}')

    @staticmethod
    def close():
        close_popup('Bugreport')

    @staticmethod
    def show():
        add_text("BugreportTitle", default_value='Thank you for reporting a bug')
        add_separator()
        Inputs.create('BugTitleInput', 'MEDIUM', 'Title', 'Bugreport')
        Inputs.create('BugDescriptionInput', 'MEDIUM', 'Describe your Bug', 'Bugreport')
        add_separator()
        Buttons.create('SendBugreportButton', 'MEDIUM', 'Send', Bugreport.github_issue)
        Buttons.create('CloseBugreportButton', 'MEDIUM', 'Close', Bugreport.close)
