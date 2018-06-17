# Stock/PIP's libraries
import json, os, logging, datetime
from flask import Flask, render_template, Response, request, redirect

# External libraries
from api_webserver import _ApiWebServer
from api_itacademy import _ApiItAcademy

# Definition of external libraries
ApiWebServer = _ApiWebServer()
ApiItAcademy = _ApiItAcademy()

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class _Server:
	app = host = port = useTunnel = None

	def loadSettings(self):
		settings = json.load(open("database/settings/settings.json"))
		self.host = settings["settings"]["server"]["host"]
		self.port = settings["settings"]["server"]["port"]
		self.useTunnel = settings["settings"]["server"]["useTunnel"]

	def initServer(self):
		self.loadSettings()
		print("[i] Initializing web-server for admin panel...")
		serverApp.run(self.host, self.port)

	def initTunnel(self):
		if self.useTunnel:
			print("[i] Initializing tunnel-server...")

serverApp = Flask(__name__, static_folder='web', static_url_path='', template_folder='web')

# Answer tools
def makeAnswer(data, login, password):
	if ApiWebServer.checkAuth(login, password):
		return str(data)
	else:
		return "err"

#####################
# Page routes
#####################
@serverApp.route("/")
def indexPage():
	return render_template("index.html")

#####################
# API routes
#####################

# API -> Auth
@serverApp.route("/api/checkAuth")
def apiCheckAuth():
	return makeAnswer(ApiWebServer.checkAuth(request.args.get("login"), request.args.get("password")), request.args.get("login"), request.args.get("password"))

# API -> Get info
@serverApp.route("/api/getBotStatus")
def apiGetBotStatus():
	return makeAnswer(ApiWebServer.getBotStatus(), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/getWebServerStatus")
def apiGetWebServerStatus():
	return makeAnswer(ApiWebServer.getWebServerStatus(), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/getTunnelStatus")
def apiGetTunnelStatus():
	return makeAnswer(ApiWebServer.getTunnelStatus(), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/getVersion")
def apiGetVersion():
	return makeAnswer(ApiWebServer.getVersion(), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/getConfirmedReviews")
def apiGetConfirmedReviews():
	return makeAnswer(ApiWebServer.getConfirmedReviews(), request.args.get("login"), request.args.get("password"))#.decode('string_escape').encode('utf8')

@serverApp.route("/api/getNotConfirmedReviews")
def apiGetNotConfirmedReviews():
	return makeAnswer(ApiWebServer.getNotConfirmedReviews(), request.args.get("login"), request.args.get("password"))#.decode('string_escape').encode('utf8')

@serverApp.route("/api/getInfoUpdateTime")
def apiGetInfoUpdateTime():
	return makeAnswer(ApiWebServer.getInfoUpdateTime(), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/getKidsFaq")
def apiGetKidsFaq():
	return makeAnswer(ApiWebServer.getKidsFaq(), request.args.get("login"), request.args.get("password"))#.decode('string_escape').encode('utf8')

@serverApp.route("/api/getAdultFaq")
def apiGetAdultFaq():
	return makeAnswer(ApiWebServer.getAdultFaq(), request.args.get("login"), request.args.get("password"))#.decode('string_escape').encode('utf8')

@serverApp.route("/api/getLastInfoUpdateTime")
def apiGetLastInfoUpdateTime():
	now = datetime.datetime.now()
	return makeAnswer(now.strftime("%Y-%m-%d %H:%M"), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/getBotStats")
def apiGetBotStats():
	statsData = ""
	try:
		f = open(os.getcwd() + "\database\\stats.txt", "r")
		statsData = f.read()
		f.close()
	except:
		statsData = ""
	return makeAnswer(statsData, request.args.get("login"), request.args.get("password"))

# API -> Set info
@serverApp.route("/api/setInfoUpdateTime")
def apiSetInfoUpdateTime():
	return makeAnswer(ApiWebServer.setInfoUpdateTime(request.args.get("newTime")), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/setNewKidsFaq")
def apiSetNewKidsFaq():
	return makeAnswer(ApiWebServer.setKidsFaq(request.args.get("question"), request.args.get("answer")), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/setNewAdultFaq")
def apiSetNewAdultFaq():
	return makeAnswer(ApiWebServer.setAdultFaq(request.args.get("question"), request.args.get("answer")), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/acceptReview")
def apiAcceptReview():
	return makeAnswer(ApiWebServer.acceptReview(request.args.get("name")), request.args.get("login"), request.args.get("password"))

@serverApp.route("/api/declineReview")
def apiDeclineReview():
	return makeAnswer(ApiWebServer.declineReview(request.args.get("name")), request.args.get("login"), request.args.get("password"))

# Debug routes
@serverApp.route("/api/shutdown")
def apiShutdownServer():
	exit()
	return "ok"

@serverApp.before_request
def debugRoute():
    #print(request)
    pass