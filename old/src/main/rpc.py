from pypresence import *
from dearpygui.core import *
from dearpygui.simple import *

client_id = '820758395673640961'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

EzPresence = 0

Buttons = get_value('ButtonsCodeInput')
State = get_value('StateInput')
Details = get_value('DetailsInput')
LargeImage = get_value('LargeImageInput')
SmallImage = get_value('SmallImageInput')
LargeText = get_value('LargeTextInput')
SmallText = get_value('SmallTextInput')

Client.authorize(client_id=client_id, scopes=['activities.write'])


