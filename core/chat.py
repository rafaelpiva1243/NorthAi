from cliente import chat
from context import configContex, configResp, configRespContext

message = None

res = chat.send_message_stream(message, config=configResp)

res = chat.send_message_stream(message, config=configRespContext )