import ctypes
import os
from resources.console.colors import *
from platform import system


def error(type, file, func, message, mode='CONSOLE', title='ERROR'):
    """
    Error function for simplified error messages.

    :param func: Function that got an error.
    :param type: Type of error.
    :param file: File that got an error.
    :param message: Error message.
    :return:
    """

    if mode == 'CONSOLE':
        if type == 'ERROR':
            print(Colors.FAIL + f'[ERROR] [{file}] [{func}]{message}!')
        elif type == 'WARNING':
            print(Colors.WARNING + f'[WARNING] [{file}] [{func}] {message}!')
        elif type == 'INFO':
            print(Colors.OKGREEN + f'[INFO] [{file}] [{func}] {message}!')
    else:
        if system() == 'Windows':
            ctypes.windll.user32.MessageBoxW(0, message, title, 0)
        elif system() == 'Darwin':
            pass
        elif system() == 'Linux':
            pass


def clear():
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Darwin':
        os.system('clear')
    elif system() == 'Linux':
        os.system('clear')
