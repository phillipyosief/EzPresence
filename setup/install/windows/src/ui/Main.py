from dearpygui.simple import *
from dearpygui.core import *
from src.ui.UI import *
from src.backend.download import *
from src.backend.cancel import *
from languages.language import *


class Main:
    username = getpass.getuser()
    temp_path = f'C:/Users/{username}/AppData/Local/Temp/'

    @staticmethod
    def show():
        with window('MainWindow', no_resize=True, no_title_bar=True):
            set_main_window_size(Size.MainWidth, Size.MainHeight)
            add_additional_font(file='C:/Windows/Fonts/arial.ttf')
            set_global_font_scale(1)

            Download.save_to_temp(
                url='https://raw.githubusercontent.com/philliphqs/EzPresence/assets/setup_img.png',
                filename='setup_img.png'
            )

            add_child('ImageChild', border=False, width=210, autosize_y=True)
            add_image('SetupImage', value=Main.temp_path + 'setup_img.png',
                      width=500 - 290, height=1000 - 575)
            end()
            add_same_line()

            add_child('ContentChild', width=Size.MainWidth - 250, height=Size.MainHeight - 55, border=True)

            add_text(f'{get_phrase("first", "title")}')
            add_separator()
            add_spacing(count=3)
            add_text(get_phrase("first", "description"))

            add_child('SpaceHolder', autosize_x=True, height=330, border=False)
            end()
            add_separator()

            add_child('ButtonsChild', autosize_x=True, height=20, border=False)

            Buttons.create('ContinueButton', 'CUSTOM',
                           get_phrase("buttons", "continue"),
                           print('Continue'), 77)
            add_same_line()
            Buttons.create('CancelButton', 'CUSTOM',
                           get_phrase("buttons", "cancel"),
                           Cancel.close_installer, 77)

            end()

        start_dearpygui(primary_window='MainWindow')

