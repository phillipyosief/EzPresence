import win32api

from resources.properties import *


class Mail:
    @staticmethod
    def send(subject, content):
        """
        Generate an mailto: link and execute it

        @param subject: Basic E-Mail subject
        @param content: Body of the E-Mail or content
        @return:
        """
        email = f'contact@{Product.Email}'
        edited_subject = subject.replace(" ", "%20")
        edited_content = content.replace(" ", "%20")
        win32api.ShellExecute(0, 'open', f'mailto:{email}?'
                                         f'subject={edited_subject}'
                                         f'&body={edited_content}', None, None, 0)
