import json


def get_var(var):
    """
    Returns with data from the settings file.

    :param var: data from the settings file.
    :return:
    """
    with open('settings.json', 'r') as settings:
        data = json.load(settings)

    if var == 'THEME':
        return data["theme"]
    elif var == 'LANGUAGE':
        return data["language"]
    else:
        error('ERROR', 'settings.py', 'get_var', f'Cant get {var} from settings')


def create_file():
    """
    Creating settings file.

    :return:
    """
    try:
        with open('settings.json', 'w') as c_f_settings:
            c_f_settings.write('{\n'
                               f'    "language": "{language.detect_language()}",\n'
                               f'    "theme": "Default"\n'
                               '}'
                               )
            c_f_settings.close()
    except Exception as e:
        error('ERROR', 'settings.py', 'create_file', f'Cant create file: {e}')


# noinspection PyBroadException
def check_file():
    """
    Check if a settings file exist if not a new settings file will be created.

    :return:
    """
    try:
        with open('settings.json', 'r') as cf_r_settings:
            cf_r_settings.close()
    except:
        create_file()
