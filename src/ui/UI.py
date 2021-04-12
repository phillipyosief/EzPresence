from dearpygui.core import *
from dearpygui.simple import *

from resources.console.error import *


class Size:
    """
    Sizes for UI elements.
    """
    MainWidth = 440
    MainHeight = 761

    ButtonSizeSmall = 100
    ButtonSizeMedium = 200
    ButtonSizeLarge = 408

    InputSizeSmall = 100
    InputSizeMedium = 204
    InputSizeLarge = 408

    ComboboxSizeSmall = 100
    ComboboxSizeMedium = 200
    ComboboxSizeLarge = 408

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
                add_button(name, width=Size.ButtonSizeSmall, label=label, callback=callback)
            elif size == 'MEDIUM':
                add_button(name, width=Size.ButtonSizeMedium, label=label, callback=callback)
            elif size == 'LARGE':
                add_button(name, width=Size.ButtonSizeLarge, label=label, callback=callback)
            elif size == 'CUSTOM':
                add_button(name, width=custom_size, label=label, callback=callback)
            else:
                internal.error('WARNING', 'UI.py', 'create', f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                add_button(name, label=label, callback=callback,
                           tip='Choose a correct button size! [SMALL, MEDIUM, LARGE]')
        except Exception as e:
            internal.error('ERROR', 'UI.py', 'create', f'Cant create button: {e}')


class Editor:
    @staticmethod
    def create(name, size, label, hint=None, parent=None):
        """
        Create a bigger input field like in a editor

        :param name: Name of the input.
        :param size: Size of the input..
        :param label: Label for the input
        :param hint: Tip for the input field because multiline is True i cant use hint (Im just to lazy to change the name).
        :param parent: Parent for the editor.
        :return:
        """
        if parent and hint is None:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeSmallWidth, height=Size.EditorSizeSmallHeight, label='',
                                   multiline=True)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeMediumWidth, height=Size.EditorSizeMediumHeight, label='',
                                   multiline=True)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   multiline=True)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   hint='Choose a correct editor size! [SMALL, MEDIUM, LARGE]',
                                   tip='Choose a correct editor size! [SMALL, MEDIUM, LARGE]', multiline=True)
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create editor: {e}')
        elif parent is None:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeSmallWidth, height=Size.EditorSizeSmallHeight, label='',
                                   tip=hint, multiline=True)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeMediumWidth, height=Size.EditorSizeMediumHeight, label='',
                                   tip=hint, multiline=True)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   tip=hint, multiline=True)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   tip=hint + '\nChoose a correct editor size! [SMALL, MEDIUM, LARGE]', multiline=True)
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create editor: {e}')
        elif hint is None:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeSmallWidth, height=Size.EditorSizeSmallHeight, label='',
                                   parent=parent, multiline=True)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeMediumWidth, height=Size.EditorSizeMediumHeight, label='',
                                   parent=parent, multiline=True)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   parent=parent, multiline=True)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   tip=hint + '\nChoose a correct editor size! [SMALL, MEDIUM, LARGE]', parent=parent,
                                   multiline=True)
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create editor: {e}')
        else:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label, parent=parent)
                    add_input_text(name, width=Size.EditorSizeSmallWidth, height=Size.EditorSizeSmallHeight, label='',
                                   tip=hint, parent=parent, multiline=True)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label, parent=parent)
                    add_input_text(name, width=Size.EditorSizeMediumWidth, height=Size.EditorSizeMediumHeight, label='',
                                   tip=hint, parent=parent, multiline=True)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label, parent=parent)
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight, label='',
                                   tip=hint, parent=parent, multiline=True)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, width=Size.EditorSizeLargeWidth, height=Size.EditorSizeLargeHeight,
                                   multiline=True, label='',
                                   tip=hint + '\nChoose a correct editor size! [SMALL, MEDIUM, LARGE]', parent=parent)
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create editor: {e}')


class Inputs:
    @staticmethod
    def create(name, size, label, hint='', parent=None):
        """
        Creating button in different sizes.s

        @param parent: If a parent is needed you can define an item.
        @param name: Name of the input.
        @param size: Size of the input.
        @param label: Label for the input.
        @param hint: Hint for the input.
        @return:
        """
        if parent is None:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.InputSizeSmall, label='', hint=hint)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.InputSizeMedium, label='', hint=hint)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.InputSizeLarge, label='', hint=hint)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, label=label,
                                   tip='Choose a correct input size! [SMALL, MEDIUM, LARGE]')
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create input: {e}')
        elif hint is None:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.InputSizeSmall, label='', parent=parent)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.InputSizeMedium, label='', parent=parent)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label)
                    add_input_text(name, width=Size.InputSizeLarge, label='', parent=parent)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, label=label,
                                   tip='Choose a correct input size! [SMALL, MEDIUM, LARGE]')
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create input: {e}')
        else:
            try:
                if size == 'SMALL':
                    add_text(f'{name}Title', default_value=label, parent=parent)
                    add_input_text(name, width=Size.ButtonSizeSmall, label='', parent=parent, hint=hint)
                elif size == 'MEDIUM':
                    add_text(f'{name}Title', default_value=label, parent=parent)
                    add_input_text(name, width=Size.ButtonSizeMedium, label='', parent=parent, hint=hint)
                elif size == 'LARGE':
                    add_text(f'{name}Title', default_value=label, parent=parent)
                    add_input_text(name, width=Size.ButtonSizeLarge, label='', parent=parent, hint=hint)
                else:
                    internal.error('WARNING', 'UI.py', 'create',
                                   f'Choose a correct button size! [SMALL, MEDIUM, LARGE]')
                    add_input_text(name, label=label,
                                   tip='Choose a correct input size! [SMALL, MEDIUM, LARGE]')
            except Exception as e:
                internal.error('ERROR', 'UI.py', 'create', f'Cant create input: {e}')


class Alignment:
    @staticmethod
    def center(name):
        main_width = get_item_width('MainWindow')
        main_height = get_item_height('MainWindow')
        widget_width = get_item_width(name)
        widget_height = get_item_height(name)
        set_window_pos(name,
                       int((main_width / 2 - widget_width / 2)),
                       int((main_height / 2 - widget_height / 2)))

    @staticmethod
    def center_window():
        main_width = GetSystemMetrics(0)
        main_height = GetSystemMetrics(1)
        login_width = get_item_width('MainWindow')
        login_height = get_item_height('MainWindow')
        set_window_pos('MainWindow', int((main_width / 2 - login_width / 2)), int((main_height / 2 - login_height / 2)))


class Checkbox:
    @staticmethod
    def create(name, default_value, label, callback, tip):
        if not tip:
            add_checkbox(name, default_value=default_value, callback=callback, label=label)
        else:
            add_checkbox(name, default_value=default_value, callback=callback, label=label, tip=tip)


class Combobox:
    @staticmethod
    def create(name, items: List, callback, size, default_value, label, custom_size=None):
        if size == 'CUSTOM':
            add_text(name + 'Title', default_value=label)
            add_combo(name, items=items, default_value=default_value, callback=callback, label='',
                      width=custom_size)
        else:
            if size == 'SMALL':
                add_text(name + 'Title', default_value=label)
                add_combo(name, items=items, default_value=default_value, callback=callback, label='',
                          width=Size.ComboboxSizeSmall)
            elif size == 'MEDIUM':
                add_text(name + 'Title', default_value=label)
                add_combo(name, items=items, default_value=default_value, callback=callback, label='',
                          width=Size.ComboboxSizeMedium)
            elif size == 'LARGE':
                add_text(name + 'Title', default_value=label)
                add_combo(name, items=items, default_value=default_value, callback=callback, label='',
                          width=Size.ComboboxSizeLarge)
            else:
                internal.error('WARNING', 'UI.py', 'create',
                               f'Choose a correct combobox size! [SMALL, MEDIUM, LARGE]')
