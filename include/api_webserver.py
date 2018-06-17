# Stock/PIP's libraries
import json, sys, os, shutil

# External libraries
import threads

# Definition of external libraries
sys.path.append("..")
#import bot

class _ApiWebServer:
	def checkAuth(self, login, password):
		adminAccounts = json.load(open("database/accounts/admins.json"))
		for item in adminAccounts["admins"]:
			if item[0] == login:
				if item[1] == password:
					return True
		return False

	def getVersion(self):
		settings = json.load(open("database/settings/settings.json"))
		return settings["settings"]["app"]["version"]

	def getBotStatus(self):
		return "ok"

	def getWebServerStatus(self):
		return "ok"

	def getTunnelStatus(self):
		return "ok"

	# Main API
	# Get queries
	def getNotConfirmedReviews(self):
		reviews = []
		allFiles = os.listdir(os.getcwd() + "\database\\reviews\unconfirmed")
		del allFiles[-1]
		for item in allFiles:
			file = open(os.getcwd() + "\database\\reviews\unconfirmed\\" + item, "r")
			content = file.read().encode('utf-8')
			content = content.split("\r\n")
			content.append(item)
			content[1] = content[1][0:-16]
			reviews.append(content)
		return json.dumps(reviews)

	def getConfirmedReviews(self):
		reviews = []
		allFiles = os.listdir(os.getcwd() + "\database\\reviews\confirmed")
		if len(allFiles) > 0:
			for item in allFiles:
				file = open(os.getcwd() + "\database\\reviews\confirmed\\" + item, "r")
				content = file.read().encode('utf-8')
				content = content.split("\r\n")
				content.append(item)
				reviews.append(content)
		return json.dumps(reviews)

	def getInfoUpdateTime(self):
		file = open(os.getcwd() + "\database\\settings\settings.json", "r")
		settings = json.loads(file.read())
		updateTime = settings["settings"]["bot"]["infoUpdateTime"]
		file.close()
		return updateTime

	def getKidsFaq(self):
		file = open(os.getcwd() + "\database\\faq\kids.json", "r")
		return file.read().encode('utf8')

	def getAdultFaq(self):
		file = open(os.getcwd() + "\database\\faq\\adult.json", "r")
		return file.read().encode('utf8')

	#Set queries
	def setKidsFaq(self, question, answer):
		file = open(os.getcwd() + "\database\\faq\kids.json", "r")
		kidsFaq = json.loads(file.read().encode('utf8'))
		kidsFaq["kids"].append([question, answer])
		file.close()
		file = open(os.getcwd() + "\database\\faq\kids.json", "w")
		file.write(json.dumps(kidsFaq).encode('utf8'))
		file.close()
		return "ok"

	def setAdultFaq(self, question, answer):
		file = open(os.getcwd() + "\database\\faq\\adult.json", "r")
		adultFaq = json.loads(file.read().encode('utf8'))
		adultFaq["adult"].append([question, answer])
		file.close()
		file = open(os.getcwd() + "\database\\faq\\adult.json", "w")
		file.write(json.dumps(adultFaq).encode('utf8'))
		file.close()
		return "ok"

	def acceptReview(self, acceptName):
		file = open('database/reviews/confirmed/index.txt', 'r')
		index = int(file.read())
		file.close()
		index += 1
		file = open('database/reviews/confirmed/index.txt', 'w')
		file.write(str(index))
		file.close()
		shutil.move(os.getcwd() + "\database\\reviews\unconfirmed\\" + acceptName, os.getcwd() + "\database\\reviews\confirmed\\" + str(index) + '.txt')
		return "ok"

	def declineReview(self, declineName):
		shutil.move(os.getcwd() + "\database\\reviews\unconfirmed\\" + declineName, os.getcwd() + "\database\\reviews\spam\\" + declineName)
		return "ok"

	def setInfoUpdateTime(self, newTime):
		file = open(os.getcwd() + "\database\\settings\settings.json", "r")
		settings = json.loads(file.read().encode('utf8'))
		settings["settings"]["bot"]["infoUpdateTime"] = int(newTime)
		file.close()
		file = open(os.getcwd() + "\database\\settings\\settings.json", "w")
		file.write(json.dumps(settings).encode('utf8'))
		file.close()
		return "ok"