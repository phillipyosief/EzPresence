from src.backend.settings import *
import locale
import json


def detect_language():
    return locale.getdefaultlocale()[0]


# noinspection PyBroadException
def set_language(lang):
    """
    Setting language in settings file.

    :param lang: Specified language.
    :return:
    """
    try:
        with open('settings.json', 'w') as s_l_settings:
            s_l_settings.write('{\n'
                               f'    "language": "{lang}",\n'
                               f'    "theme": "{get_var("THEME")}"\n'
                               '}')
            s_l_settings.close()
    except Exception as e:
        error('ERROR', 'language.py', 'set_language', f'Cant set language to "{lang}": {e}')


def get_phrase(path):
    """
    Get text phrase from language file.

    :param path: JSON Path to phrase.
    :return:
    """
    try:
        with open('settings.json') as g_p_settings:
            data = json.load(g_p_settings)
        return data + path
    except Exception as e:
        error('ERROR', 'language.py', 'get_phrase', f'Cant get phrase from {path}: {e}')
