from dearpygui.simple import *
from dearpygui.core import *

from PIL import Image, ImageDraw, ImageFont

from src.ui.UI import *

from resources.console.error import internal


# 250
# 320

class Preview:
    HidePreviewValue = get_value('HidePreviewCheckbox')

    @staticmethod
    def create_image(username, discriminator, details, state, appname, button1_label=False, button2_label=False):
        completeusername = username + '#' + discriminator

        bg = Image.open('resources/assets/preview_rpc_background.png')
        pb = Image.open('resources/assets/example_pb.png')

        btn = Image.open('resources/assets/button_background.png')

        font_med = ImageFont.truetype("resources/assets/font.ttf", 18)
        font_small = ImageFont.truetype("resources/assets/font.ttf", 13)
        font_bold = ImageFont.truetype("resources/assets/font_bold.ttf", 13)

        new_width = 92
        new_height = 92
        new_pb = pb.resize((new_width, new_height), Image.ANTIALIAS)

        # x y
        bg.paste(new_pb, (77, 13))

        W, H = (320, 250)

        draw = ImageDraw.Draw(bg)
        m_w, m_h = font_med.getsize(username)
        s_w, s_h = font_med.getsize(completeusername)
        draw.text(((W - m_w) / 2.8, 105), username, fill="white", font=font_med)
        draw.text(((W - s_w) / 2.5, 130), completeusername, fill="white", font=font_small)
        draw.text((5, 160), 'PLAYING A GAME', fill="white", font=font_bold)

        draw.text((100, 180), appname, fill="white", font=font_bold)
        draw.text((100, 198), details, fill="white", font=font_small)
        draw.text((100, 215), state, fill="white", font=font_small)

        if button1_label is not False and button2_label is False:
            btn_width = 213
            btn_height = 40
            new_btn = btn.resize((btn_width, btn_height), Image.ANTIALIAS)

            # x y
            bg.paste(new_btn, (17, 240))

            draw.text(((W - s_w) / 1.9, 252), button1_label, fill="white", font=font_small)
        elif button1_label is False:
            pass
        else:
            btn_width = 213
            btn_height = 40
            new_btn = btn.resize((btn_width, btn_height), Image.ANTIALIAS)

            # x y
            bg.paste(new_btn, (17, 240))

            draw.text(((W - s_w) / 1.9, 252), button1_label, fill="white", font=font_small)

            ###########

            btn2_width = 213
            btn2_height = 40
            new_btn2 = btn.resize((btn2_width, btn2_height), Image.ANTIALIAS)

            # x y
            bg.paste(new_btn2, (17, 275))

            draw.text(((W - s_w) / 1.9, 288), button2_label, fill="white", font=font_small)

        bg.save('temp/preview.png')

    @staticmethod
    def refresh():
        state = get_value('StateInput')
        details = get_value('DetailsInput')

        if get_value('UseButtonsCheckbox') and get_value('AdvancedCheckbox') is True:
            buttons = get_value('ButtonsCode').split('=')
            try:
                Preview.create_image('philliphqs', '5920', details, state, 'EzPresence',
                                     button1_label=buttons[0], button2_label=buttons[2])
            except:
                Preview.create_image('philliphqs', '5920', details, state, 'EzPresence',
                                     button1_label=buttons[0])
        elif get_value('AdvancedCheckbox') is True:
            Preview.create_image('philliphqs', '5920', details, state, 'app')
        elif get_value('UseButtonsCheckbox') is True:
            buttons = get_value('ButtonsCode').split('=')
            try:
                Preview.create_image('philliphqs', '5920', details, state, 'EzPresence',
                                     button1_label=buttons[0], button2_label=buttons[2])
            except:
                Preview.create_image('philliphqs', '5920', details, state, 'EzPresence',
                                     button1_label=buttons[0])

        else:
            Preview.create_image('philliphqs', '5920', details, state, 'EzPresence')

        # ToDo: Error wegkriegen
        add_image(f'PreviewImageBackground', 'temp/preview.png', width=250 - 90,
                  height=320 - 110, parent='PreviewImageChild')
        internal.clear()


    @staticmethod
    def popout():
        """
        Create a popup to view the Preview in bigger size

        @return:
        """

        def close():
            close_popup('PopupPreview')

        items = ['PreviewPopupImageBackground', 'PreviewPopupCloseButton', 'PopupPreview']

        for item in items:
            if does_item_exist(item):
                delete_item(item)
            else:
                pass

        with popup("PopupPreviewButton", "PopupPreview", modal=True, mousebutton=mvMouseButton_Left):

            try:
                add_image('PreviewPopupImageBackground', 'temp/preview.png', width=270,
                          height=340, parent='PopupPreview')
            except:
                add_image('PreviewPopupImageBackground', 'resources/assets/preview_example.png', width=270,
                          height=340, parent='PopupPreview')

            Buttons.create("PreviewPopupCloseButton", 'CUSTOM', 'Close popup', close,
                           custom_size=Size.ButtonSizeMedium + 70)

    @staticmethod
    def show():
        """
        Shows "Preview"

        @return:
        """
        add_child('PreviewImageChild', border=False, height=210, autosize_x=True, autosize_y=True,
                  no_scrollbar=True)
        try:
            add_image('PreviewImageBackground', 'temp/preview.png', width=250 - 90,
                      height=320 - 110, parent='PreviewImageChild')
        except:
            add_image('PreviewImageBackground', 'resources/assets/preview_example.png', width=250 - 90,
                      height=320 - 110, parent='PreviewImageChild')

        add_same_line()

        add_child('PreviewOptionsChild', height=210, border=False, width=240)
        add_text('PreviewOptions', parent='PreviewOptionsChild', default_value='Preview options')
        Buttons.create('PopupPreviewButton', 'CUSTOM', 'Popup', Preview.popout, 240)

        end()
