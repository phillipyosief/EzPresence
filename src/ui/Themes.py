from dearpygui.core import *
from dearpygui.simple import *


class Themes:
    themes = ['Default', 'Discord']

    @staticmethod
    def default():
        set_theme_item(mvGuiCol_WindowBg, 11, 11, 11, 255)
        set_theme_item(mvGuiCol_PopupBg, 6, 6, 6, 240)
        set_theme_item(mvGuiCol_Border, 55, 55, 55, 128)
        set_theme_item(mvGuiCol_FrameBg, 30, 30, 30, 138)
        set_theme_item(mvGuiCol_FrameBgHovered, 63, 63, 63, 102)
        set_theme_item(mvGuiCol_FrameBgActive, 28, 28, 28, 171)
        set_theme_item(mvGuiCol_TitleBgActive, 21, 21, 21, 255)
        set_theme_item(mvGuiCol_MenuBarBg, 8, 8, 8, 255)
        set_theme_item(mvGuiCol_CheckMark, 125, 125, 125, 255)
        set_theme_item(mvGuiCol_SliderGrab, 125, 125, 125, 255)
        set_theme_item(mvGuiCol_SliderGrabActive, 97, 97, 97, 255)
        set_theme_item(mvGuiCol_Button, 42, 42, 42, 255)
        set_theme_item(mvGuiCol_ButtonHovered, 52, 52, 52, 255)
        set_theme_item(mvGuiCol_ButtonActive, 59, 59, 59, 255)
        set_theme_item(mvGuiCol_Header, 96, 96, 96, 255)
        set_theme_item(mvGuiCol_HeaderHovered, 101, 101, 101, 255)
        set_theme_item(mvGuiCol_HeaderActive, 104, 104, 104, 255)
        set_theme_item(mvGuiCol_SeparatorHovered, 72, 72, 72, 199)
        set_theme_item(mvGuiCol_ResizeGrip, 90, 90, 90, 64)
        set_theme_item(mvGuiCol_ResizeGripHovered, 138, 138, 138, 64)
        set_theme_item(mvGuiCol_ResizeGripActive, 156, 156, 156, 64)
        set_theme_item(mvGuiCol_Tab, 52, 52, 52, 220)
        set_theme_item(mvGuiCol_TabHovered, 65, 65, 65, 220)
        set_theme_item(mvGuiCol_TabActive, 86, 86, 86, 220)

    @staticmethod
    def discord():
        set_theme_item(mvGuiCol_Text, 255, 255, 255, 255)
        set_theme_item(mvGuiCol_TextDisabled, 128, 128, 128, 255)
        set_theme_item(mvGuiCol_WindowBg, 32, 34, 37, 255)
        set_theme_item(mvGuiCol_ChildBg, 0, 0, 0, 0)
        set_theme_item(mvGuiCol_PopupBg, 47, 49, 54, 255)
        set_theme_item(mvGuiCol_Border, 110, 110, 128, 128)
        set_theme_item(mvGuiCol_FrameBg, 40, 43, 48, 255)
        set_theme_item(mvGuiCol_FrameBgHovered, 41, 44, 48, 230)
        set_theme_item(mvGuiCol_FrameBgActive, 36, 39, 42, 0)
        set_theme_item(mvGuiCol_TitleBg, 10, 10, 10, 255)
        set_theme_item(mvGuiCol_TitleBgActive, 32, 34, 37, 255)
        set_theme_item(mvGuiCol_TitleBgCollapsed, 0, 0, 0, 130)
        set_theme_item(mvGuiCol_MenuBarBg, 36, 36, 36, 255)
        set_theme_item(mvGuiCol_ScrollbarBg, 46, 51, 56, 123)
        set_theme_item(mvGuiCol_ScrollbarGrab, 32, 34, 37, 255)
        set_theme_item(mvGuiCol_ScrollbarGrabHovered, 32, 34, 37, 255)
        set_theme_item(mvGuiCol_ScrollbarGrabActive, 34, 36, 39, 255)
        set_theme_item(mvGuiCol_CheckMark, 125, 148, 232, 223)
        set_theme_item(mvGuiCol_SliderGrab, 114, 137, 218, 223)
        set_theme_item(mvGuiCol_SliderGrabActive, 97, 116, 182, 255)
        set_theme_item(mvGuiCol_Button, 114, 137, 218, 223)
        set_theme_item(mvGuiCol_ButtonHovered, 97, 116, 182, 255)
        set_theme_item(mvGuiCol_ButtonActive, 97, 116, 182, 255)
        set_theme_item(mvGuiCol_Header, 66, 150, 250, 79)
        set_theme_item(mvGuiCol_HeaderHovered, 66, 150, 250, 204)
        set_theme_item(mvGuiCol_HeaderActive, 66, 150, 250, 255)
        set_theme_item(mvGuiCol_Separator, 110, 110, 128, 128)
        set_theme_item(mvGuiCol_SeparatorHovered, 26, 102, 191, 199)
        set_theme_item(mvGuiCol_SeparatorActive, 26, 102, 191, 255)
        set_theme_item(mvGuiCol_ResizeGrip, 58, 58, 58, 64)
        set_theme_item(mvGuiCol_ResizeGripHovered, 56, 56, 56, 171)
        set_theme_item(mvGuiCol_ResizeGripActive, 51, 51, 51, 242)
        set_theme_item(mvGuiCol_Tab, 47, 49, 54, 255)
        set_theme_item(mvGuiCol_TabHovered, 63, 65, 70, 255)
        set_theme_item(mvGuiCol_TabActive, 114, 137, 218, 204)
        set_theme_item(mvGuiCol_TabUnfocused, 17, 26, 38, 248)
        set_theme_item(mvGuiCol_TabUnfocusedActive, 35, 67, 108, 255)
        set_theme_item(mvGuiCol_DockingPreview, 66, 150, 250, 179)
        set_theme_item(mvGuiCol_PlotLines, 156, 156, 156, 255)
        set_theme_item(mvGuiCol_PlotLinesHovered, 255, 110, 89, 255)
        set_theme_item(mvGuiCol_TextSelectedBg, 114, 137, 218, 241)
        set_theme_item(mvGuiCol_NavHighlight, 66, 150, 250, 255)
        set_theme_item(mvGuiCol_ModalWindowDimBg, 204, 204, 204, 89)

    @staticmethod
    def style():
        set_style_window_padding(8.00, 8.00)
        set_style_frame_padding(3.00, 3.00)
        set_style_item_spacing(8.00, 4.00)
        set_style_item_inner_spacing(4.00, 4.00)
        set_style_touch_extra_padding(0.00, 0.00)
        set_style_indent_spacing(25.00)
        set_style_scrollbar_size(12.00)
        set_style_grab_min_size(10.00)
        set_style_window_border_size(0.00)
        set_style_child_border_size(1.00)
        set_style_popup_border_size(1.00)
        set_style_frame_border_size(0.00)
        set_style_tab_border_size(0.00)
        set_style_window_rounding(7.00)
        set_style_child_rounding(0.00)
        set_style_frame_rounding(2.00)
        set_style_popup_rounding(0.00)
        set_style_scrollbar_rounding(12.00)
        set_style_grab_rounding(2.00)
        set_style_tab_rounding(4.00)
        set_style_window_title_align(0.00, 0.51)
        set_style_window_menu_button_position(mvDir_Left)
        set_style_color_button_position(mvDir_Right)
        set_style_button_text_align(0.50, 0.50)
        set_style_selectable_text_align(0.00, 0.00)
        set_style_display_safe_area_padding(3.00, 3.00)
        set_style_global_alpha(1.00)
        set_style_antialiased_lines(True)
        set_style_antialiased_fill(True)
        set_style_curve_tessellation_tolerance(1.25)
        set_style_circle_segment_max_error(1.60)

    @staticmethod
    def get_current_theme():
        return 'Theme'

    @staticmethod
    def set_theme(theme):
        if theme == 'Discord':
            Themes.discord()
            Themes.style()
        elif theme == 'Default':
            Themes.default()
            Themes.style()
        else:
            set_theme(theme)
            Themes.style()