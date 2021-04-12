from pypresence.pypresence import Client, Presence
import locale
import json
import ctypes
from platform import system
import os
import getpass
from urllib import request, error
import win32api
from lxml import html
import requests
import time
from dearpygui.core import *
from dearpygui.simple import *
import webbrowser
from PIL import Image, ImageDraw, ImageFont

from src.backend.close import *
from src.backend.download import *
from src.backend.email import *
from src.backend.github import *
from src.backend.rpc import *
from src.backend.settings import *
from src.backend.web import *

from src.ui.About import *
from src.ui.Advanced import *
from src.ui.Bugreport import *
from src.ui.Contact import *
from src.ui.DevEmbed import *
from src.ui.Donate import *
from src.ui.Footer import *
from src.ui.Main import *
from src.ui.MenuBar import *
from src.ui.Preview import *
from src.ui.Settings import *
from src.ui.testing import *
from src.ui.UI import *
from src.ui.UseButtons import *
from src.ui.UsedLibs import *
from src.ui.Variables import *

from resources.console.error.internal import *
from resources.properties import *