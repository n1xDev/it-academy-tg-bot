# Stock/PIP's libraries
import sys

# External libraries
sys.path.append("include")
from tools import _Tools
from bot import _Bot
from server import _Server

# Definition of external libraries
Bot = _Bot()
Server = _Server()
Tools = _Tools()

def Main():
	Bot.initBot()
	Server.initServer()


Main()