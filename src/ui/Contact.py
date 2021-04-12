from dearpygui.simple import *
from dearpygui.core import *

from src.backend.email import *

from src.ui.UI import *


class Contact:
    @staticmethod
    def send():
        """
        Send a E-Mail (view backend/mail.py)

        @return:
        """
        Mail.send(get_value('ContactSubjectInput'), get_value('ContactContentInput'))

    @staticmethod
    def close():
        """
        Just close the "Contact" Popup

        @return:
        """
        close_popup('Contact')

    @staticmethod
    def show():
        Inputs.create('ContactSubjectInput', 'MEDIUM', 'Subject')
        Editor.create('ContactContentInput', 'MEDIUM', 'Content', hint='')
        add_separator()
        Buttons.create('ContactSendButton', 'MEDIUM', 'Send', Contact.send)
        Buttons.create('ContactCloseButton', 'MEDIUM', 'Close', Contact.close)