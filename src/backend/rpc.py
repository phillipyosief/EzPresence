from dearpygui.simple import *
from dearpygui.core import *

from pypresence.pypresence import Presence, Client

from resources.console.error import internal

RichPresence = False

CLIENT_ID = '820758395673640961'


class RPC:
    @staticmethod
    def start():
        state = get_value('StateInput')
        details = get_value('DetailsInput')

        usebuttons = get_value('UseButtonsCheckbox')
        advanced = get_value('AdvancedCheckbox')

        try:
            if advanced is True and usebuttons:
                clientid = get_value('ClientIDInput')
                buttons = get_value('ButtonsCode').split('=')

                li = get_value('LargeImageInput')
                lit = get_value('LargeImageTextInput')

                si = get_value('SmallImageInput')
                sit = get_value('SmallImageTextInput')

                RPC = Presence(clientid)  # Initialize the client class
                RPC.connect()  # Start the handshake loop

                try:
                    print(RPC.update(
                        state=state,
                        details=details,
                        small_text=sit,
                        small_image=si,
                        large_text=lit,
                        large_image=li,
                        buttons=[
                            {"label": buttons[0], "url": buttons[1]},
                            {"label": buttons[2], "url": buttons[3]}
                        ]
                    )
                    )
                except:
                    print(RPC.update(
                        state=state,
                        details=details,
                        buttons=[
                            {"label": buttons[0], "url": buttons[1]}
                        ]
                    )
                    )

                RichPresence = True

                while RichPresence:
                    if RichPresence is False:
                        break
                    else:
                        time.sleep(15)
            elif advanced is True:
                clientid = get_value('ClientIDInput')

                li = get_value('LargeImageInput')
                lit = get_value('LargeImageTextInput')

                si = get_value('SmallImageInput')
                sit = get_value('SmallImageTextInput')

                RPC = Presence(clientid)
                RPC.connect()

                print(RPC.update(
                    state=state,
                    details=details,
                    small_text=sit,
                    small_image=si,
                    large_text=lit,
                    large_image=li
                )
                )

                RichPresence = True

                while RichPresence:
                    if RichPresence is False:
                        break
                    else:
                        time.sleep(15)
            elif usebuttons is True:
                buttons = get_value('ButtonsCode').split('=')

                client_id = '820758395673640961'
                RPC = Presence(client_id)
                RPC.connect()
                print(buttons)

                try:
                    print(RPC.update(
                        state=state,
                        details=details,
                        buttons=[
                            {"label": buttons[0], "url": buttons[1]},
                            {"label": buttons[2], "url": buttons[3]}
                        ]
                    )
                    )
                except:
                    print(RPC.update(
                        state=state,
                        details=details,
                        buttons=[
                            {"label": buttons[0], "url": buttons[1]}
                        ]
                    )
                    )

                RichPresence = True

                while RichPresence:
                    if RichPresence is False:
                        break
                    else:
                        time.sleep(15)
            else:
                client_id = '820758395673640961'  # Fake ID, put your real one here
                RPC = Presence(client_id)  # Initialize the client class
                RPC.connect()  # Start the handshake loop

                print(RPC.update(state=state,
                                 details=details))

                RichPresence = True

                while RichPresence:
                    if RichPresence is False:
                        break
                    else:
                        time.sleep(15)
        except Exception as e:
            if not state and details == '':
                internal.error('ERROR', 'rpc.py', 'start', 'State and Details are not allowed to be empty', 'GUI', 'ERROR')
            elif not state or details == '':
                internal.error('ERROR', 'rpc.py', 'start', 'State or Details are not allowed to be empty', 'GUI',
                               'ERROR')


