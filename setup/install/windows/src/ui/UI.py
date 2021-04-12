from dearpygui.core import *
from dearpygui.simple import *
from resources.console.error import internal


class Size:
    """
    Sizes for UI elements.
    """
    MainWidth = 820
    MainHeight = 480

    ButtonSizeSmall = 100
    ButtonSizeMedium = 200
    ButtonSizeLarge = 408

    InputSizeSmall = 100
    InputSizeMedium = 204
    InputSizeLarge = 408

    EditorSizeSmallWidth = 100
    EditorSizeMediumWidth = 204
    EditorSizeLargeWidth = 408

    EditorSizeSmallHeight = 20
    EditorSizeMediumHeight = 50
    EditorSizeLargeHeight = 80


class Buttons:
    """
    Button creator to keep all elements in one style.
    """

    @staticmethod
    def create(name, size, label, callback, custom_size=None):
        """
        Creating button in different sizes.

        :param custom_size: Custom width size only activated when size='CUSTOM'.
        :param name: Name for the button.
        :param size: Size for button .
        :param label: Label for the button.
        :param callback: Onclick function for the created button.
        :return:
        """
        try:
            if size == 'SMALL':
                add_button(name, width=Size.ButtonSizeSmall, label=label, callback=callback, small=False)
            elif size == 'MEDIUM':
                add_button(name, width=Size.ButtonSizeMedium, label=label, callback=callback, small=False)
            elif size == 'LARGE':
                add_button(name, width=Size.ButtonSizeLarge, label=label, callback=callback, small=False)
            elif size == 'CUSTOM':
                add_button(name, width=custom_size, label=label, callback=callback, small=False)

            else:
                internal.error('WARNING', 'UI.py', 'create', f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                add_button(name, label=label, callback=callback,
                           tip='Choose a correct button size! [SMALL, MEDIUM, LARGE]', small=False)
        except Exception as e:
            internal.error('ERROR', 'UI.py', 'create', f'Cant create button: {e}')