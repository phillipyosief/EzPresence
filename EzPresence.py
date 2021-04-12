from src.ui.Main import *
from src.backend.settings import *


class App:
    @staticmethod
    def startup():
        check_file()



if __name__ == '__main__':
    App.startup()
    Main.show()
    show_style_editor()
    start_dearpygui(primary_window='MainWindow')

    # print(GitHub.get_non_api('philliphqs', '/html/body/div[4]/main/div[2]/div/div[1]/div/div[4]/div[2]/div[3]/div/a[3]/span'))
