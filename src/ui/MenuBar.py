from dearpygui.simple import *
from dearpygui.core import *

from src.backend.close import *
from src.backend.download import *
from src.backend.web import *

from src.ui.Settings import *
from src.ui.Bugreport import *
from src.ui.Contact import *
from src.ui.About import *
from src.ui.UsedLibs import *
from src.ui.DevEmbed import *


class MenuBar:
    """
    MenuBar Categories are divided in functions
    """

    @staticmethod
    def file():
        with menu("FileMenu", label='File'):
            add_text('SettingsItem', default_value='Settings')
            add_separator()
            add_menu_item('ExitItem', label='Exit', callback=Close.full_exit)

        with popup('SettingsItem', 'Settings', modal=True, mousebutton=mvMouseButton_Left):
            Settings.show()

    @staticmethod
    def about():
        Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/Icon-1024.png?raw=true',
                              'ezpresence_icon.png')

        with menu("AboutMenu", label='About'):
            add_menu_item('GitHubRepositoryItem', label='GitHub Repository', callback=Web.github_repo)
            add_menu_item('GitHubProfileItem', label='GitHub Profile', callback=Web.github_profile)
            add_separator()
            add_text('AboutEzPresence', default_value='About EzPresence')

        with popup('AboutEzPresence', 'About', modal=True, mousebutton=mvMouseButton_Left, parent='HelpMenu'):
            About.show()

            with popup('UsedLibraries', 'Used libraries', modal=True, mousebutton=mvMouseButton_Left):
                UsedLibs.show()

    @staticmethod
    def help():
        with menu("HelpMenu", label='Help'):
            add_text('ContactItem', default_value='Contact')
            add_separator()
            add_text('BugreportItem', default_value='Report a Bug')

        with popup("BugreportItem", "Bugreport", modal=True, mousebutton=mvMouseButton_Left):
            Bugreport.show()

        with popup("ContactItem", "Contact", modal=True, mousebutton=mvMouseButton_Left):
            Contact.show()

    @staticmethod
    def developer():
        with menu("DeveloperMenu", label='Developer'):
            Download.save_to_temp('https://avatars.githubusercontent.com/u/63358485', 'ezpresence_profile_pic.png')
            Download.save_to_temp('https://avatars.githubusercontent.com/u/66477948', 'hqsartworks.png')

            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/stars.png?raw=true',
                                  'stars.png')
            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/follower.png?raw=true',
                                  'follower.png')

            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/twitter.png?raw=true',
                                  'twitter.png')
            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/discord.png?raw=true',
                                  'discord.png')
            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/alpha.png?raw=true',
                                  'alpha.png')
            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/instagram.png?raw=true',
                                  'instagram.png')
            Download.save_to_temp('https://github.com/philliphqs/EzPresence/blob/assets/donate.png?raw=true',
                                  'donate.png')

            DevEmbed.show()

    @staticmethod
    def show():
        """
        Show the MenuBar

        @return:
        """
        with menu_bar("MenuBar"):
            MenuBar.file()
            MenuBar.help()
            MenuBar.about()
            MenuBar.developer()
