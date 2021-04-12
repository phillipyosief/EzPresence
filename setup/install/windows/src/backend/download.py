import getpass
import urllib.request


class Download:
    @staticmethod
    def save_to_temp(url, filename):
        username = getpass.getuser()
        urllib.request.urlretrieve(url, f'C:/Users/{username}/AppData/Local/Temp/'+filename)
