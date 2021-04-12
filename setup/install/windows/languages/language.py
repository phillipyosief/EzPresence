import locale
import json


def detect_language():
    return locale.getdefaultlocale()[0]


def get_phrase(one, two=None, three=None, four=None, five=None):
    """
    Get text phrase from language file.

    :param five: JSON Path to phrase.
    :param four: JSON Path to phrase.
    :param three: JSON Path to phrase.
    :param two: JSON Path to phrase.
    :param one: JSON Path to phrase.
    :return:
    """

    with open(f'languages/{detect_language()}.json') as g_p_settings:
        data = json.load(g_p_settings)

    if two is not None:
        return data[one][two]
    elif two and three is not None:
        return data[one][two][three]
    elif two and three and four is not None:
        return data[one][two][three][four]
    elif two and three and four and five is not None:
        return data[one][two][three][four][five]
