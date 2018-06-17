# Stock/PIP's libraries
import threading

# External libraries
from server import _Server

# Definition of external libraries
Server = _Server()

class _Threads:
	botThread = serverThread = tunnelThread = None

	def startServerThread(self):
		self.serverThread = threading.Thread(target = Server.initServer, name = "myServerThread")
		self.serverThread.start()

	def startTunnelThread(self):
		Server.loadSettings()
		self.tunnelThread = threading.Thread(target = Server.initTunnel, name = "myTunnelThread")
		self.tunnelThread.start()

	def startAllThreads(self):
		self.startServerThread()
		self.startTunnelThread()