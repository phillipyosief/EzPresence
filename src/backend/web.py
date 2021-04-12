import webbrowser

class URL:
    """
    List of variables to simply create urls
    """
    github = 'http://github.com/'
    github_user = 'philliphqs'
    github_repo_name = 'EzPresence'

    github_repo = github + github_user + '/' + github_repo_name
    github_profile = github + github_user

    github_issue = github+github_user+'/'+github_repo+'/issues/new'

    instagram = 'http://instagram.com/'
    instagram_user = 'phillip_hqs'

    instagram_profile = instagram + instagram_user

    twitter = 'http://twitter.com/'
    twitter_user = 'phillip_hqs'

    twitter_profile = twitter + twitter_user

    discord = 'http://discord.gg/'
    alphaclan = 'uFdVUMH'
    hqsartworks = 'BxxzJQrWEV'

    alphaclan_discord = discord + alphaclan
    hqsartworks_discord = discord + hqsartworks

    instagram_hqsartworks_profile = instagram+'hqsartworks'
    twitter_hqsartworks_profile = twitter+'hqsartworks'


class Web:
    """
    Functions to open a specific webpage (mainly social media profiles)
    """
    @staticmethod
    def github_repo():
        webbrowser.open(URL.github_repo)

    @staticmethod
    def github_profile():
        webbrowser.open(URL.github_profile)

    @staticmethod
    def instagram():
        webbrowser.open(URL.instagram_profile)

    @staticmethod
    def twitter():
        webbrowser.open(URL.twitter_profile)

    @staticmethod
    def alphaclan_discord():
        webbrowser.open(URL.alphaclan_discord)

    @staticmethod
    def hqsartworks_discord():
        webbrowser.open(URL.hqsartworks_discord)

    @staticmethod
    def instagram_hqsartworks():
        webbrowser.open(URL.instagram_hqsartworks_profile)

    @staticmethod
    def twitter_hqsartworks():
        webbrowser.open(URL.twitter_hqsartworks_profile)




