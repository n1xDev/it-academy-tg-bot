# Stock/PIP's libraries
import sys

# External libraries
import bot
sys.path.append("include")
from threads import _Threads

# Definition of external libraries
Threads = _Threads()

# Main function
def Main():
	Threads.startAllThreads()
	bot.BotStart()

Main()