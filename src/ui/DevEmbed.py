from dearpygui.core import *
from dearpygui.simple import *

import getpass

from src.backend.github import *
from src.backend.web import *

from src.ui.Donate import *


class DevEmbed:
    path = f'C:/Users/{getpass.getuser()}/AppData/Local/Temp/'

    @staticmethod
    def show():
        """
        Shows the "DevEmbed" with all GUI content

        @return:
        """

        add_child('DeveloperChild', width=84, height=84, border=False)
        add_image('DevItemPic', value=DevEmbed.path + 'ezpresence_profile_pic.png',
                  width=84, height=84)

        end()
        add_same_line()

        add_child('DevContent', width=200, height=85, border=False)
        add_text('DevName', default_value='philliphqs')

        add_text('DevDescription', default_value='Just a bad python dev', color=[166, 166, 166])

        add_image('DevFollowerIcon', value=DevEmbed.path + 'follower.png', width=20, height=20)
        add_same_line()
        add_text('FollowerCount', default_value=str(GitHub.get('philliphqs', 'followers')))
        add_same_line()
        add_image('DevStarsIcon', value=DevEmbed.path + 'stars.png', width=19, height=19)
        add_same_line()
        add_text('DevStarsCount', default_value='18')

        add_image_button('DevInstagramIcon', value=DevEmbed.path + 'instagram.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.instagram)
        add_same_line()
        add_image_button('DevTwitterIcon', value=DevEmbed.path + 'twitter.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.twitter)
        add_same_line()
        add_image_button('DevDiscordIcon', value=DevEmbed.path + 'discord.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.hqsartworks_discord)
        add_same_line()
        add_image_button('DevAlphaIcon', value=DevEmbed.path + 'alpha.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.alphaclan_discord)
        add_same_line()
        add_image_button('DevDonateIcon', value=DevEmbed.path + 'donate.png', width=20, height=20,
                         background_color=[0, 0, 0, 0])
        end()
        add_separator()

        add_child('DeveloperHQSChild', width=84, height=84, border=False)
        add_image('DevHQSItemPic', value=DevEmbed.path + 'hqsartworks.png',
                  width=84, height=84)

        end()
        add_same_line()

        add_child('DevHQSContent', width=200, height=75, border=False)
        add_text('DevHQSName', default_value='hqsartworks')
        add_text('DevHQSDescription', default_value='My website for some projects \nstill not finished...',
                 color=[166, 166, 166])

        add_image_button('DevHQSInstagramIcon', value=DevEmbed.path + 'instagram.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.instagram_hqsartworks)
        add_same_line()
        add_image_button('DevHQSTwitterIcon', value=DevEmbed.path + 'twitter.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.twitter_hqsartworks)
        add_same_line()
        add_image_button('DevHQSDiscordIcon', value=DevEmbed.path + 'discord.png', width=20, height=20,
                         background_color=[0, 0, 0, 0], callback=Web.hqsartworks_discord)
        add_same_line()
        add_image_button('DevHQSDonateIcon', value=DevEmbed.path + 'donate.png', width=20, height=20,
                         background_color=[0, 0, 0, 0])

        with popup('DevDonateIcon', 'Donate philliphqs', modal=True, mousebutton=mvMouseButton_Left):
            Donate.show()

        with popup('DevHQSDonateIcon', 'Donate hqsartworks', modal=True, mousebutton=mvMouseButton_Left):
            Donate.show_hqs()

        end()