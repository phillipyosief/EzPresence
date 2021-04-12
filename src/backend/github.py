from urllib import error, request
import json
from lxml import html


class GitHub:
    @staticmethod
    def get(user, item):
        """
        Get an info about a GitHub user with the GitHub API

        @param user: username e.g. philliphqs
        @param item: item e.g. followers
        @return:
        """
        try:
            with request.urlopen('https://api.github.com/users/' + user) as url:
                data = json.loads(url.read().decode())
                return data[item]
        except error.HTTPError:
            return "403: maybe rate limit"

    @staticmethod
    def get_non_api(user, item):
        """
        Get an info about a GitHub user by scraping the html code of a GitHub profile

        @param user:
        @param item:
        @return:
        """
        try:
            page = requests.get('https://github.com/' + user)

            tree = html.fromstring(page.content)

            return tree.xpath(item + '/text()')
        except:
            return 'None'
