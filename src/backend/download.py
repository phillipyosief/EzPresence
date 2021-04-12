import getpass
import urllib.request


class Download:
    @staticmethod
    def save_to_temp(url, filename):
        """
        Download any file and save it in temp folder

        @param url: Download URL to requested file
        @param filename: Filename for downloaded file
        @return:
        """
        username = getpass.getuser()
        urllib.request.urlretrieve(url, f'C:/Users/{username}/AppData/Local/Temp/'+filename)
