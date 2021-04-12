from dearpygui.core import *
from dearpygui.simple import *

from src.ui.UI import *
from src.ui.Themes import *


class Settings:
    @staticmethod
    def close():
        close_popup('Settings')

    @staticmethod
    def choose_profilepic():
        pass

    @staticmethod
    def settings_set_theme():
        set_theme(get_value('SettingsThemeCombo'))

    @staticmethod
    def show():
        add_text('Design')
        add_separator()
        Combobox.create('SettingsThemeCombo', Themes.themes, Settings.settings_set_theme, 'MEDIUM', 'Theme', 'Theme')

        add_spacing(count=3)
        add_text('PreviewSettings', default_value='Preview settings')

        add_separator()

        Inputs.create('SettingsUsername', 'MEDIUM', 'Username', 'e.g. Wumpus#0001')
        Inputs.create('SettingsProfilepictureInput', 'SMALL', 'Profilepicture')
        add_same_line()
        Buttons.create('SettingsChooseProfilepicture', 'CUSTOM', 'Open file', Settings.choose_profilepic, Size.ButtonSizeSmall-15)

        add_separator()
        Buttons.create('SettingsClose', 'MEDIUM', 'Close', Settings.close)
