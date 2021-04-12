from old.src.gui.base import *
from old.src.main.web import *
from old.src.main.rpc import *

# TODO: Fix show_buttons_code bugs

class App:

    def center(window):
        main_width = get_item_width('MainWindow')
        main_height = get_item_height('MainWindow')
        login_width = get_item_width(window)
        login_height = get_item_height(window)
        set_window_pos(window, int((main_width / 1.9 - login_width / 50)), int((main_height / 0.47 - login_height / 2)))

    def show_clientid_input(self):
        if does_item_exist('ClientIDInput'):
            delete_item('ClientIDSeperator')
            delete_item('ClientIDInput')
            delete_item('ClientIDTitle')
            delete_item('LargeImageTitle')
            delete_item('SmallImageTitle')
            delete_item('LargeImageInput')
            delete_item('SmallImageInput')
            delete_item('LargeTextTitle')
            delete_item('SmallTextTitle')
            delete_item('LargeTextInput')
            delete_item('SmallTextInput')
        else:
            add_spacing(count=1, parent='Inputs', name='ClientIDSpacing')
            add_separator(name='ClientIDSeperator', parent='Inputs')

            add_text('ClientIDTitle', default_value='ClientID', parent='Inputs')
            add_input_text('ClientIDInput', width=InputWidth, parent='Inputs')

            add_text('LargeImageTitle', default_value='Large Image', parent='Inputs')
            add_input_text('LargeImageInput', width=InputWidth, parent='Inputs')

            add_text('SmallImageTitle', default_value='Small Image', parent='Inputs')
            add_input_text('SmallImageInput', width=InputWidth, parent='Inputs')

            add_text('LargeTextTitle', default_value='Large Text (Tooltip for the large image)', parent='Inputs')
            add_input_text('LargeTextInput', width=InputWidth, parent='Inputs')

            add_text('SmallTextTitle', default_value='Small Text (Tooltip for the small image)', parent='Inputs')
            add_input_text('SmallTextInput', width=InputWidth, parent='Inputs')

    @staticmethod
    def hide_preview():
        if is_item_shown('PreviewWindow'):
            hide_item('PreviewWindow')
        else:
            show_item('PreviewWindow')

    @staticmethod
    def show_buttons_code():
        def write_new_button():
            set_value('ButtonsCodeInput',
                      value='{"label": "{' + get_value("Button1NameInput") + '}", "url": "' + get_value(
                          "Button1URLInput") + '"}'
                            + ', \n'
                            + '{"label": "{' + get_value("Button2NameInput") + '}", "url": "' + get_value(
                          "Button2URLInput") + '"}'
                      )

        def collapse_buttons_code():
            if does_item_exist('CollapseButtonsCodeButton'):
                set_item_height('ButtonsCodeInput', height=100)
                delete_item('CollapseButtonsCodeButton')
                show_item('ExpandButtonsCodeButton')
            else:
                set_item_height('ButtonsCodeInput', height=100)
                show_item('ExpandButtonsCodeButton')

        def reset_buttonscode():
            set_value('ButtonsCodeInput', value='')

        def expand_buttons_code(self):
            if does_item_exist('ButtonsCodeInput'):
                set_item_height('ButtonsCodeInput', height=300)
                hide_item('PreviewWindow')
                hide_item('ExpandButtonsCodeButton')
                add_same_line()
                add_button('CollapseButtonsCodeButton', label='Collapse', callback=collapse_buttons_code,
                           parent='Inputs')

        def close_popup_add_button():
            close_popup('Add Button')
            delete_item('AddButtonButtonsCodeButton')
            delete_item('AddButtonButtonsCodeButton', children_only=True)

        if does_item_exist('ButtonsCodeInput'):
            delete_item('ButtonsCodeSpacing')
            delete_item('ButtonsCodeSeperator')
            delete_item('ButtonsCodeInputTitle')
            delete_item('ButtonsCodeInput')
            delete_item('ResetButtonsCodeButton')
            delete_item('SameLineButtonsCode1')
            delete_item('ExpandButtonsCodeButton')
            delete_item('SameLineButtonsCode2')
            if does_item_exist('AddButtonButtonsCodeButton'):
                try:
                    delete_item('AddButtonButtonsCodeButton')
                    delete_item('AddButtonButtonsCodeButton', children_only=True)
                except:
                    pass
        else:
            add_spacing(count=1, parent='Inputs', name='ButtonsCodeSpacing')
            add_separator(name='ButtonsCodeSeperator', parent='Inputs')
            add_text('ButtonsCodeInputTitle', default_value='Buttons code', parent='Inputs')
            add_input_text('ButtonsCodeInput', tip='[{"label": "Button Name", \n"url": "https://example.com"}, ...]',
                           width=InputWidth, height=100, multiline=True, parent='Inputs')
            add_button('ResetButtonsCodeButton', label='Reset', parent='Inputs', callback=reset_buttonscode)
            add_same_line(name='SameLineButtonsCode1', parent='Inputs')
            add_button('ExpandButtonsCodeButton', label='Expand', parent='Inputs', callback=expand_buttons_code)
            add_same_line(name='SameLineButtonsCode2', parent='Inputs')
            add_button('AddButtonButtonsCodeButton', label='Add Button', parent='Inputs')

            with popup('AddButtonButtonsCodeButton', "Add Button", modal=True, mousebutton=mvMouseButton_Left):
                add_text('Button1NameTitle', default_value='Name', parent='Add Button')
                add_input_text('Button1NameInput', label='', width=PopupInputWidth, parent='Add Button')

                add_text('Button1URLTitle', default_value='URL', parent='Add Button')
                add_input_text('Button1URLInput', label='', width=PopupInputWidth, parent='Add Button')

                add_separator()

                add_text('Button2NameTitle', default_value='Name', parent='Add Button')
                add_input_text('Button2NameInput', label='', width=PopupInputWidth, parent='Add Button')

                add_text('Button2URLTitle', default_value='URL', parent='Add Button')
                add_input_text('Button2URLInput', label='', width=PopupInputWidth, parent='Add Button')

                add_separator()

                add_button('AddButtonPopupButton', label='Add Button', parent='Add Button',
                           callback=write_new_button)
                add_same_line()
                add_button('ClosePopupButton', label='Close', parent='Add Button',
                           callback=close_popup_add_button)

    with window('PreviewWindow',
                label='Preview',
                no_title_bar=False,
                autosize=True,
                no_resize=True,
                no_close=True,
                no_move=True,
                no_scrollbar=True,
                no_collapse=True,
                no_bring_to_front_on_focus=True):
        add_image('PreviewImage', value='assets/preview_rpc_background.png', width=200, height=270)

    with window("MainWindow", autosize=True):
        with menu_bar('menu bar'):
            with menu('menu 1'):
                add_menu_item('menu item')
            with menu('menu 2'):
                add_menu_item('menu item 2')

        add_child('Inputs', autosize_x=True, border=False, height=610)

        add_text('DetailsInputTitle', default_value='Title')
        add_input_text('StateInput', width=InputWidth)

        add_text('DescriptionInputTitle', default_value='Description')
        add_input_text('DetailsInput', width=InputWidth)
        end()

        add_separator()

        add_checkbox('ClientID',
                     label='Use ClientID',
                     default_value=False,
                     tip='Use custom application to set\ncustom images to your Rich Presence',
                     callback=show_clientid_input)
        add_same_line()
        add_checkbox('HidePreview',
                     label='Hide Preview',
                     default_value=False,
                     tip='Hide Preview',
                     callback=hide_preview)
        add_same_line()
        add_checkbox('UseButtonsPreview',
                     label='Use Buttons',
                     default_value=False,
                     tip='Use Custom Buttons',
                     callback=show_buttons_code)

        center('PreviewWindow')

        add_separator()

        add_button('StartButton', label='Start RPC', width=ButtonWidth)
        add_same_line()
        add_button('DisableButton', label='Disable RPC', width=ButtonWidth)

        add_button('CreateApplicationButton', label='Create application', width=ButtonMaxWidth, callback=create_application)

    set_main_window_size(WindowWidth, WindowHeight)
    start_dearpygui(primary_window="MainWindow")
