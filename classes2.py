from cmu_graphics import *
from PIL import Image, ImageDraw
import math, random, time
import os, pathlib


class Purple: #normal monster
	purplesPosition = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = []
		self.lifePoint = 320
		self.currLifePoint = 320
		self.worth = 14
		self.speed = 9
		Purple.purplesPosition.append(self.position)

	def __repr__(self):
		return(f"Purple({self.x},{self.y})")

class Shark: #normal monster
	sharksPosition = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = []
		self.lifePoint = 320
		self.currLifePoint = 320
		self.worth = 14
		self.speed = 9
		Shark.sharksPosition.append(self.position)

	def __repr__(self):
		return(f"Shark({self.x},{self.y})")

class Bear: #normal monster
	bearsPosition = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = []
		self.lifePoint = 320
		self.currLifePoint = 320
		self.worth = 14
		self.speed = 9
		Bear.bearsPosition.append(self.position)

	def __repr__(self):
		return(f"Bear({self.x},{self.y})")

class Milk: #heavy blood monster
	milksPosition = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = []
		self.lifePoint = 640
		self.currLifePoint = 640
		self.worth = 21
		self.speed = 10
		Milk.milksPosition.append(self.position)

	def __repr__(self):
		return(f"Purple({self.x},{self.y})")

class Green: #fast-moving monster
	greensPosition = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = []
		self.lifePoint = 560
		self.currLifePoint = 560
		self.worth = 21
		self.speed = 16
		Green.greensPosition.append(self.position)

	def __repr__(self):
		return(f"Bear({self.x},{self.y})")

class Mummy: #fast and heavy blood monster
	mummysPosition = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = []
		self.lifePoint = 600
		self.currLifePoint = 600
		self.worth = 28
		self.speed = 14
		Mummy.mummysPosition.append(self.position)

	def __repr__(self):
		return(f"Mummy({self.x},{self.y})")	

class BottleCanoon:
	def __init__(self):
		self.lifeDamage = -3
		self.speedDamage = -3
		self.price = -260
class BottleCanoonBullet(BottleCanoon):
	count = 0
	def __init__(self, x, y):
		self.name = 'bottleCannon'
		self.x = x
		self.y = y
		BottleCanoonBullet.count += 1		

	def __repr__(self):
		return(f"Cannon({self.x},{self.y})")


class IceStar:
	def __init__(self):
		self.lifeDamage = -3
		self.speedDamage = -3
		self.price = -260

class IceStarBullet(IceStar):
	count = 0
	def __init__(self, x, y):
		self.name = 'iceStar'
		self.x = x
		self.y = y
		IceStarBullet.count += 1

	def __repr__(self):
		return f"IceStar({self.x},{self.y})"

class Rocket:
	def __init__(self):
		self.lifeDamage = -3
		self.speedDamage = -3
		self.price = -220

class RocketBullet(Rocket):
	count = 0
	def __init__(self, x, y):
		self.name = 'rocket'
		self.x = x
		self.y = y
		RocketBullet.count += 1

	def __repr__(self):
		return f"Rocket({self.x},{self.y})"



class Carrot:
	def __init__(self):
		self.name = 'carrot'
		self.lifePoint = 10
		self.currLifePoint = 10



class Maps:

	def __init__(self):
		self.a = [(95, 125),(95, 175),(95, 225),(95, 275),(145,275),(195,275),(245, 275),(245,225),
				  (295,225),(345, 225),(395,225),(445,225),(495,225),(545,225),(595,225),(595,175),
				  (595, 125)]
		self.b = [(95,125),(95,175),(145,175),(195,175),(245,175),(245,225),(245,275),(295,275),
				  (345,275),(395,275),(395,325),(445,325),(495,325),(495,275),(495,225),(495,175),
				  (545,175),(595,175),(595, 125)]
		self.c = [(95,125),(95,175),(95,225),(145,225),(195,225),(195,175),(195,125),(245,125),
				  (295,125),(345,125),(345,175),(345,225),(345,275),(395,275),(445,275),(495,275),
				  (495,325),(545,325),(595,325),(595,275),(595,225),(595,175),(595,125)]
	pass


#Cell index
ISMAP = -1
ISEMPTY = 0
ISCANOON = 1
ISICESTAR = 2
ISROCKET = 3

def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

def onAppStart(app):
	app.show = "showBackground"
	app.station = 1
	#app.music = loadSound("sound.mp3")
	#app.music.play(restart = True)

	#draw bluesky
	app.blueSky = Image.open("BlueSky.jpg")
	app.blueSky = app.blueSky.convert("RGB")
	app.blueSky = CMUImage(app.blueSky.resize((700, 400)))
	
	#draw instruction
	app.instruction = Image.open("Instruction.jpg")
	app.instruction = app.instruction.convert("RGB")
	app.instruction = CMUImage(app.instruction.resize((700, 400)))
	
	#draw weapon gallery
	app.weaponGallery = Image.open("WeaponGallery.jpg")
	app.weaponGallery = app.weaponGallery.convert("RGB")
	app.weaponGallery = CMUImage(app.weaponGallery.resize((700, 400)))

	#draw stations
	app.stationChoose = Image.open("Station.png")
	app.stationChoose = app.stationChoose.convert("RGB")
	app.stationChoose = CMUImage(app.stationChoose.resize((700, 400)))

	#new game
	newGame(app)

	#round
	newRound(app)
	

def newGame(app):
	#initial values
	app.count = 0
	app.onStepCount = 0
	app.gameStart = False 
	app.pause = False
	app.showGrid = False
	app.monsterKilled = 0
	
	#monster initals
	app.countMonster = 0	

	app.maps = Maps()
	app.map = None
	if app.station  == 1:
		app.map = app.maps.a
	elif app.station == 2:
		app.map = app.maps.b
	elif app.station == 3:
		app.map = app.maps.c

	app.gameover = False

	#keep track of the cells
	app.row = 6
	app.col = 11
	app.cells = []
	for i in range(app.row):
		cols = []
		for j in range(app.col):
			cols.append(ISEMPTY)
		app.cells.append(cols)
	
	#initial value
	app.currentRound = 1
	app.totalRound = 5
	app.money = 600
	app.moneySymbol = Image.open("MoneySymbol.jpg")#Image is a screenshot from CarrotFantasy2, and I edited it.
	app.moneySymbol = app.moneySymbol.convert("RGBA")
	app.moneySymbol = CMUImage(app.moneySymbol.resize((30, 30)))

	#draw background
	app.bgWidth, app.bgHeight = 700, 400 
	app.blueBG = Image.open("blueBG.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.blueBG = app.blueBG.convert("RGB")
	app.blueBG = CMUImage(app.blueBG.resize((app.bgWidth, app.bgHeight)))

	#start 
	app.start = Image.open("Start.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.start = app.start.convert("RGB")
	app.start = CMUImage(app.start.resize((51, 70)))

	#draw monster 
	app.monsters = [] #Make an empty monster list
	app.lastMonsterTime = time.time()	
	app.imageWidth, app.imageHeight = 35,48
	app.monsterMap = []
	for i in range(len(app.map)-1):
		(prevx, prevy) = app.map[i]
		(nextx, nexty) = app.map[i+1]
		dx = (nextx - prevx)//10
		dy = (nexty - prevy)//10
		i = 0
		while i < 10:
			app.monsterMap.append((prevx+dx*i, prevy+dy*i))
			i = i+1
	#purple
	app.purpleImage = Image.open("Purple.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.purpleImage = app.purpleImage.convert("RGBA")
	app.purpleImage = CMUImage(app.purpleImage.resize((35,48)))
	#shark
	app.sharkImage = Image.open("Shark.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.sharkImage = app.sharkImage.convert("RGBA")
	app.sharkImage = CMUImage(app.sharkImage.resize((48,48)))
	#bear
	app.bearImage = Image.open("Bear.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.bearImage = app.bearImage.convert("RGBA")
	app.bearImage = CMUImage(app.bearImage.resize((35,48)))
	#milk
	app.milkImage = Image.open("Milk.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.milkImage = app.milkImage.convert("RGBA")
	app.milkImage = CMUImage(app.milkImage.resize((28,48)))
	#green
	app.greenImage = Image.open("Green.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.greenImage = app.greenImage.convert("RGBA")
	app.greenImage = CMUImage(app.greenImage.resize((48,48)))
	#mummy
	app.mummyImage = Image.open("Mummy.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.mummyImage = app.mummyImage.convert("RGBA")
	app.mummyImage = CMUImage(app.mummyImage.resize((44,44)))
	

	#draw weapon choice
	app.weaponChoice = 2
	app.showWeaponChoice = False
	app.weaponChoiceX = 0
	app.weaponChoiceY = 0
	app.cellX = -100
	app.cellY = -100
	app.weaponChosen = False
	app.rocketPrice = Image.open("Rocket Price.png")#Image is a screenshot from CarrotFantasy2, and I edited it.
	app.rocketPrice = app.rocketPrice.convert("RGB")
	app.rocketPrice = CMUImage(app.rocketPrice.resize((app.imageWidth-5, app.imageWidth-5)))
	app.canoonPrice = Image.open("Canoon Price.jpg")#Image is a screenshot from CarrotFantasy2, and I edited it.
	app.canoonPrice = app.canoonPrice.convert("RGB")
	app.canoonPrice = CMUImage(app.canoonPrice.resize((app.imageWidth-5, app.imageWidth-5)))
	app.iceStarPrice = Image.open("IceStar Price.jpg")#Image is a screenshot from CarrotFantasy2, and I edited it.
	app.iceStarPrice = app.iceStarPrice.convert("RGB")
	app.iceStarPrice = CMUImage(app.iceStarPrice.resize((app.imageWidth-5, app.imageWidth-5)))

	#choose weapon
	app.placeWeapon = False
	app.placeX = -1
	app.placeY = -1

	#draw waepon and bullet
	app.rocket = Image.open("Rocket.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.rocket = app.rocket.convert("RGB")
	app.rocket = CMUImage(app.rocket.resize((45, 45)))
	app.rocketList = []
	app.canoon = Image.open("BottleCanoon.png")#Image is a screenshot from CarrotFantasy2, and I edited it.
	app.canoon = app.canoon.convert("RGB")
	app.canoon = CMUImage(app.canoon.resize((45, 45)))
	app.canoonList = []
	app.iceStar = Image.open("IceStar.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.iceStar = app.iceStar.convert("RGB")
	app.iceStar = CMUImage(app.iceStar.resize((45, 45)))
	app.iceStarList = []

	#rocket bullet
	app.rocketBulletList = []
	app.rocketBulletDic = {}
	app.rocketBulletDicCopy = {}
	app.showBullet = True
	app.rocketBullet = Image.open("RocketBullet.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.rocketBullet = app.rocketBullet.convert("RGBA")
	app.rocketBullet = CMUImage(app.rocketBullet.resize((25, 25)))
	#canoon bullet
	app.canoonBulletList = []
	app.canoonBulletDic = {}
	app.canoonBulletDicCopy = {}
	app.showBullet = True
	app.canoonBullet = Image.open("CanoonBullet.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.canoonBullet = app.canoonBullet.convert("RGBA")
	app.canoonBullet = CMUImage(app.canoonBullet.resize((20, 20)))
	#ice star bullet
	app.iceStarBulletList = []
	app.iceStarBulletDic = {}
	app.iceStarBulletDicCopy = {}
	app.showBullet = True
	app.iceStarBullet = Image.open("IceStarBullet.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.iceStarBullet = app.iceStarBullet.convert("RGBA")
	app.iceStarBullet = CMUImage(app.iceStarBullet.resize((25, 25)))


	#carrot initials
	app.carrotX = 595
	app.carrotY = 125
	app.carrotCurrLife = 10
	app.carrot1 = Image.open("Carrot1.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot1 = app.carrot1.convert("RGB")
	app.carrot1 = CMUImage(app.carrot1.resize((75,45)))

	app.carrot2 = Image.open("Carrot2.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot2 = app.carrot2.convert("RGB")
	app.carrot2 = CMUImage(app.carrot2.resize((75,45)))

	app.carrot3 = Image.open("Carrot3.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot3 = app.carrot3.convert("RGB")
	app.carrot3 = CMUImage(app.carrot3.resize((75,45)))
	
	app.carrot4 = Image.open("Carrot4.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot4 = app.carrot4.convert("RGB")
	app.carrot4 = CMUImage(app.carrot4.resize((75,45)))

	app.carrot5 = Image.open("Carrot5.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot5 = app.carrot5.convert("RGB")
	app.carrot5 = CMUImage(app.carrot5.resize((75,45)))

	app.carrot6 = Image.open("Carrot6.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot6 = app.carrot6.convert("RGB")
	app.carrot6 = CMUImage(app.carrot6.resize((75,45)))

	app.carrot7 = Image.open("Carrot7.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot7 = app.carrot7.convert("RGB")
	app.carrot7 = CMUImage(app.carrot7.resize((75,45)))

	app.carrot8 = Image.open("Carrot8.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot8 = app.carrot8.convert("RGB")
	app.carrot8 = CMUImage(app.carrot8.resize((75,45)))

	app.carrot9 = Image.open("Carrot9.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot9 = app.carrot9.convert("RGB")
	app.carrot9 = CMUImage(app.carrot9.resize((75,45)))

	app.carrot10 = Image.open("Carrot10.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot10 = app.carrot10.convert("RGB")
	app.carrot10 = CMUImage(app.carrot10.resize((75,45)))

	#randomly choose monster
	app.n = 0 #monster indext
	if app.currentRound == 1 or app.currentRound == 2 or app.currentRound ==4: #easy round
		app.n = random.randint(1,3)
	elif app.currentRound == 3: # harder round
		app.n = random.randint(4,5)
	elif app.currentRound == 5: #hardest round
		app.n = 6

	#win or loose
	app.win = Image.open("Win.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.win = app.win.convert("RGBA")
	app.win = CMUImage(app.win.resize((700,400)))

	app.loose = Image.open("Loose.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.loose = app.loose.convert("RGBA")
	app.loose = CMUImage(app.loose.resize((700,400)))

	#score bar
	app.frame = Image.open("Frame.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.frame = app.frame.convert("RGBA")
	app.frame = CMUImage(app.frame.resize((230,27)))

	app.coin = Image.open("Coin.png")
	app.coin = app.coin.convert("RGBA")
	app.coin = CMUImage(app.coin.resize((25,25)))


	app.perstep = 5


	
	

def newRound(app):
	#initial values
	app.count = 0
	app.onStepCount = 0
	app.gameStart = False 
	app.pause = False
	app.showGrid = False
	
	#monster initals
	app.countMonster = 0	

	app.maps = Maps()
	app.map = None
	if app.station  == 1:
		app.map = app.maps.a
	elif app.station == 2:
		app.map = app.maps.b
	elif app.station == 3:
		app.map = app.maps.c
	app.gameover = False

	#keep track of the cells
	app.row = 6
	app.col = 11
	app.cells = []
	for i in range(app.row):
		cols = []
		for j in range(app.col):
			cols.append(ISEMPTY)
		app.cells.append(cols)
	
	#initial value
	#app.currentRound = 1
	app.totalRound = 5
	#app.money = 500
	app.moneySymbol = Image.open("MoneySymbol.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.moneySymbol = app.moneySymbol.convert("RGBA")
	app.moneySymbol = CMUImage(app.moneySymbol.resize((30, 30)))

	#draw background
	app.bgWidth, app.bgHeight = 700, 400 
	app.blueBG = Image.open("blueBG.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.blueBG = app.blueBG.convert("RGB")
	app.blueBG = CMUImage(app.blueBG.resize((app.bgWidth, app.bgHeight)))

	#start 
	app.start = Image.open("Start.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.start = app.start.convert("RGB")
	app.start = CMUImage(app.start.resize((51, 70)))

	#draw monster 
	app.monsters = [] #Make an empty monster list
	app.lastMonsterTime = time.time()	
	app.imageWidth, app.imageHeight = 35,48
	app.monsterMap = []
	for i in range(len(app.map)-1):
		(prevx, prevy) = app.map[i]
		(nextx, nexty) = app.map[i+1]
		dx = (nextx - prevx)//10
		dy = (nexty - prevy)//10
		i = 0
		while i < 10:
			app.monsterMap.append((prevx+dx*i, prevy+dy*i))
			i = i+1
	#purple
	app.purpleImage = Image.open("Purple.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.purpleImage = app.purpleImage.convert("RGBA")
	app.purpleImage = CMUImage(app.purpleImage.resize((35,48)))
	#shark
	app.sharkImage = Image.open("Shark.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.sharkImage = app.sharkImage.convert("RGBA")
	app.sharkImage = CMUImage(app.sharkImage.resize((48,48)))
	#bear
	app.bearImage = Image.open("Bear.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.bearImage = app.bearImage.convert("RGBA")
	app.bearImage = CMUImage(app.bearImage.resize((35,48)))
	#milk
	app.milkImage = Image.open("Milk.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.milkImage = app.milkImage.convert("RGBA")
	app.milkImage = CMUImage(app.milkImage.resize((28,48)))
	#green
	app.greenImage = Image.open("Green.png")#Image is a screenshot from CarrotFantasy2, and I edited it.
	app.greenImage = app.greenImage.convert("RGBA")
	app.greenImage = CMUImage(app.greenImage.resize((48,48)))
	#mummy
	app.mummyImage = Image.open("Mummy.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.mummyImage = app.mummyImage.convert("RGBA")
	app.mummyImage = CMUImage(app.mummyImage.resize((44,44)))
	

	#draw weapon choice
	app.weaponChoice = 2
	app.showWeaponChoice = False
	app.weaponChoiceX = 0
	app.weaponChoiceY = 0
	app.cellX = -100
	app.cellY = -100
	app.weaponChosen = False
	app.rocketPrice = Image.open("Rocket Price.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.rocketPrice = app.rocketPrice.convert("RGB")
	app.rocketPrice = CMUImage(app.rocketPrice.resize((app.imageWidth-5, app.imageWidth-5)))
	app.canoonPrice = Image.open("Canoon Price.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.canoonPrice = app.canoonPrice.convert("RGB")
	app.canoonPrice = CMUImage(app.canoonPrice.resize((app.imageWidth-5, app.imageWidth-5)))
	app.iceStarPrice = Image.open("IceStar Price.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.iceStarPrice = app.iceStarPrice.convert("RGB")
	app.iceStarPrice = CMUImage(app.iceStarPrice.resize((app.imageWidth-5, app.imageWidth-5)))

	#choose weapon
	app.placeWeapon = False
	app.placeX = -1
	app.placeY = -1

	#draw waepon and bullet
	app.rocket = Image.open("Rocket.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.rocket = app.rocket.convert("RGB")
	app.rocket = CMUImage(app.rocket.resize((45, 45)))
	#app.rocketList = []
	app.canoon = Image.open("BottleCanoon.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.canoon = app.canoon.convert("RGB")
	app.canoon = CMUImage(app.canoon.resize((45, 45)))
	#app.canoonList = []
	app.iceStar = Image.open("IceStar.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.iceStar = app.iceStar.convert("RGB")
	app.iceStar = CMUImage(app.iceStar.resize((45, 45)))
	#app.iceStarList = []

	#rocket bullet
	#app.rocketBulletList = []
	#app.rocketBulletDic = {}
	#app.rocketBulletDicCopy = {}
	app.showBullet = True
	app.rocketBullet = Image.open("RocketBullet.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.rocketBullet = app.rocketBullet.convert("RGBA")
	app.rocketBullet = CMUImage(app.rocketBullet.resize((25, 25)))
	#canoon bullet
	#app.canoonBulletList = []
	#app.canoonBulletDic = {}
	#app.canoonBulletDicCopy = {}
	app.showBullet = True
	app.canoonBullet = Image.open("CanoonBullet.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.canoonBullet = app.canoonBullet.convert("RGBA")
	app.canoonBullet = CMUImage(app.canoonBullet.resize((20, 20)))
	#ice star bullet
	#app.iceStarBulletList = []
	#app.iceStarBulletDic = {}
	#app.iceStarBulletDicCopy = {}
	app.showBullet = True
	app.iceStarBullet = Image.open("IceStarBullet.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.iceStarBullet = app.iceStarBullet.convert("RGBA")
	app.iceStarBullet = CMUImage(app.iceStarBullet.resize((25, 25)))

	#carrot initials
	app.carrotX = 595
	app.carrotY = 125
	#app.carrotCurrLife = 10
	app.carrot1 = Image.open("Carrot1.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot1 = app.carrot1.convert("RGB")
	app.carrot1 = CMUImage(app.carrot1.resize((75,45)))

	app.carrot2 = Image.open("Carrot2.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot2 = app.carrot2.convert("RGB")
	app.carrot2 = CMUImage(app.carrot2.resize((75,45)))

	app.carrot3 = Image.open("Carrot3.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot3 = app.carrot3.convert("RGB")
	app.carrot3 = CMUImage(app.carrot3.resize((75,45)))
	
	app.carrot4 = Image.open("Carrot4.jpg") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot4 = app.carrot4.convert("RGB")
	app.carrot4 = CMUImage(app.carrot4.resize((75,45)))

	app.carrot5 = Image.open("Carrot5.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot5 = app.carrot5.convert("RGB")
	app.carrot5 = CMUImage(app.carrot5.resize((75,45)))

	app.carrot6 = Image.open("Carrot6.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot6 = app.carrot6.convert("RGB")
	app.carrot6 = CMUImage(app.carrot6.resize((75,45)))

	app.carrot7 = Image.open("Carrot7.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot7 = app.carrot7.convert("RGB")
	app.carrot7 = CMUImage(app.carrot7.resize((75,45)))

	app.carrot8 = Image.open("Carrot8.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot8 = app.carrot8.convert("RGB")
	app.carrot8 = CMUImage(app.carrot8.resize((75,45)))

	app.carrot9 = Image.open("Carrot9.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot9 = app.carrot9.convert("RGB")
	app.carrot9 = CMUImage(app.carrot9.resize((75,45)))

	app.carrot10 = Image.open("Carrot10.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.carrot10 = app.carrot10.convert("RGB")
	app.carrot10 = CMUImage(app.carrot10.resize((75,45)))

	#randomly choose monster
	app.n = 0 #monster indext
	if app.currentRound == 1 or app.currentRound == 2 or app.currentRound ==4: #easy round
		app.n = random.randint(1,3)
	elif app.currentRound == 3: # harder round
		app.n = random.randint(4,5)
	elif app.currentRound == 5: #hardest round
		app.n = 6

	#win or loose
	app.win = Image.open("Win.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.win = app.win.convert("RGBA")
	app.win = CMUImage(app.win.resize((700,400)))

	app.loose = Image.open("Loose.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.loose = app.loose.convert("RGBA")
	app.loose = CMUImage(app.loose.resize((700,400)))

	#score bar
	app.frame = Image.open("Frame.png") #Image is a screenshot from CarrotFantasy2, and I edited it.
	app.frame = app.frame.convert("RGBA")
	app.frame = CMUImage(app.frame.resize((230,27)))

	app.coin = Image.open("Coin.png")
	app.coin = app.coin.convert("RGBA")
	app.coin = CMUImage(app.coin.resize((25,25)))

	app.perstep = 5



def redrawAll(app):
	#draw background
	if app.show == "showBackground":
		drawImage(app.blueSky, 0, 0)
	elif app.show == "showInstruction":
		drawImage(app.instruction, 0, 0)
	elif app.show == "showWeaponGallery":
		drawImage(app.weaponGallery, 0, 0)
	elif app.show == "showStation":
		drawImage(app.stationChoose, 0, 0)
	elif app.show == "play game":
		#draw background
		drawImage(app.blueBG, 350, 225, align = "center")

		#draw panel bar
		drawRect(0, 0, 700, 50, fill = rgb(195, 130, 90))

		#draw restart button
		drawCircle(50 ,25, 23, fill = rgb(238, 208, 158))
		drawLabel(chr(0x2b6f), 50, 25, size=40, rotateAngle = 265, bold = True, font ='Segoe UI Symbol', fill = rgb(195, 130, 90))

		#draw stop button
		drawCircle(120 ,25, 23, fill = rgb(238, 208, 158))
		drawLine(112,13,112, 37, lineWidth = 8, fill = rgb(195, 130, 90))
		drawLine(127,13,127, 37, lineWidth = 8, fill = rgb(195, 130, 90))

		#draw round  panel
		drawRect(270, 5, 150, 40, fill = rgb(146, 89, 36), border = rgb(248, 240, 157), borderWidth = 3)
		drawLabel(app.currentRound, 290, 25, fill = "white", size = 23, bold = True, font = "Comfortaa")
		drawLabel("/", 306.5, 25, fill = "white", size = 23, bold = True, font = "Comfortaa")
		drawLabel(app.totalRound, 325, 25, fill = "white", size = 23, bold = True, font = "Comfortaa")
		drawLabel("Round", 380, 25, fill = "white", bold = True, size = 23, font = "Comfortaa")

		#draw money symbol
		drawImage(app.moneySymbol, 575, 25, align = "center")
		drawLabel(app.money, 620, 25, fill = "white", size = 23, bold = True, font = "Comfortaa")

		#draw map
		for (x,y) in app.map[:-1]:
			drawRect(x, y, 50, 50, align = "center", fill = rgb(193,216,250), border=rgb(99,120,151))
			i = (y-75)//50
			j = (x-95)//50
			changeCellIndex(app, i, j, ISMAP)

		#draw start 
		drawImage(app.start,94, 110, align = "center")

		#draw grid
		if app.showGrid == True:
			for x in range(70, 621,50):
				drawLine(x, 50, x, 350, dashes=(10, 5), fill = "white")
			for y in range(50, 351, 50):
				drawLine(70, y, 620, y, dashes=(10, 5), fill = "white")

		
		#draw carrots
		if app.carrotCurrLife == 1:
			drawImage(app.carrot1, 575,100)
		elif app.carrotCurrLife == 2:
			drawImage(app.carrot2, 575,100)
		elif app.carrotCurrLife == 3:
			drawImage(app.carrot3, 575,100)
		elif app.carrotCurrLife == 4:
			drawImage(app.carrot4, 575,100)
		elif app.carrotCurrLife == 5:
			drawImage(app.carrot5, 575,100)
		elif app.carrotCurrLife == 6:
			drawImage(app.carrot6, 575,100)
		elif app.carrotCurrLife == 7:
			drawImage(app.carrot7, 575,100)
		elif app.carrotCurrLife == 8:
			drawImage(app.carrot8, 575,100)
		elif app.carrotCurrLife == 9:
			drawImage(app.carrot9, 575,100)
		elif app.carrotCurrLife == 10:
			drawImage(app.carrot10, 575,100)


		#draw weapon
		#rocket	
		for (x, y) in app.rocketList:		
			drawImage(app.rocket, x, y, align = "center")
			i = (y-75)//50
			j = (x-95)//50
			changeCellIndex(app, i, j, ISROCKET)
			app.rocketBulletList.append((x,y))
		#canoon	
		for (x, y) in app.canoonList:		
			drawImage(app.canoon, x, y, align = "center")
			i = (y-75)//50
			j = (x-95)//50
			changeCellIndex(app, i, j, ISCANOON)
			app.canoonBulletList.append((x,y))
		#ice start
		for (x, y) in app.iceStarList:
			drawImage(app.iceStar, x, y, align = "center")	
			i = (y-75)//50
			j = (x-95)//50
			changeCellIndex(app, i, j, ISICESTAR)	
			app.iceStarBulletList.append((x,y))
		
		

		#draw monsters
		for monster in app.monsters:
			if app.monsterMap[len(app.monsterMap)-1] not in monster.position:
				if type(monster) == Purple:
					image = app.purpleImage
				elif type(monster) == Shark:
					image = app.sharkImage
				elif type(monster) == Bear:
					image = app.bearImage
				elif type(monster) == Milk:
					image = app.milkImage
				elif type(monster) == Green:
					image = app.greenImage
				elif type(monster) == Mummy:
					image = app.mummyImage
				drawImage(image, monster.x, monster.y, align= "center")
				monster.position.append((monster.x, monster.y))
				
				#draw monster life bar
				barUnit = 40/monster.lifePoint
				barLength = monster.currLifePoint*barUnit
				if barLength > 0:
					drawRect(monster.x-20, monster.y-40, barLength, 10, fill = "lightgreen")
				drawRect(monster.x, monster.y-35, 40, 10, fill = None, border = "white", align = "center")
		
		#draw bullet
		if app.monsters != []:
			if app.station == 1:
				#canoon bullet
				for key in app.canoonBulletDic:
					x,y = app.canoonBulletDic[key]
					drawImage(app.canoonBullet, x, y, align = "center")
				#ice star bullet
				for key in app.iceStarBulletDic:
					x,y = app.iceStarBulletDic[key]
					drawImage(app.iceStarBullet, x, y, align = "center")

			elif app.station == 2:
				#rocket bullet
				for key in app.rocketBulletDic:
					x,y = app.rocketBulletDic[key]
					drawImage(app.rocketBullet, x, y, align = "center")
				#canoon bullet
				for key in app.canoonBulletDic:
					x,y = app.canoonBulletDic[key]
					drawImage(app.canoonBullet, x, y, align = "center")

			elif app.station == 3:
				#rocket bullet
				for key in app.rocketBulletDic:
					x,y = app.rocketBulletDic[key]
					drawImage(app.rocketBullet, x, y, align = "center")
				#ice star bullet
				for key in app.iceStarBulletDic:
					x,y = app.iceStarBulletDic[key]
					drawImage(app.iceStarBullet, x, y, align = "center")
		

		#draw weapon choice
		if app.showWeaponChoice == True:
			if (app.cellX,app.cellY) not in app.map:
				#check if valid
				i = (app.cellY-75)//50
				j = (app.cellX-95)//50
				if checkIfValid(app, i, j, ISEMPTY):
					drawRect(app.cellX, app.cellY, 45, 45, fill = None, border = "white", align = "center")
					drawLine(app.cellX-15, app.cellY, app.cellX+15, app.cellY, fill = "white")
					drawLine(app.cellX, app.cellY-15, app.cellX, app.cellY+15, fill = "white")
					if app.station == 1:
						drawImage(app.canoonPrice, app.cellX-25, app.cellY-50, align = "center")
						drawImage(app.iceStarPrice, app.cellX+25, app.cellY-50, align = "center")				
					elif app.station == 2:
						drawImage(app.rocketPrice, app.cellX-25, app.cellY-50, align = "center")
						drawImage(app.canoonPrice, app.cellX+25, app.cellY-50, align = "center")
					elif app.station == 3:
						drawImage(app.iceStarPrice, app.cellX-25, app.cellY-50, align = "center")
						drawImage(app.rocketPrice, app.cellX+25, app.cellY-50, align = "center")

		

		#game over
		if app.gameover == "Loose":
			drawRect(0, 0, 700, 400, fill = "gray", opacity = 50)
			#draw summary pannel
			drawImage(app.loose, 0, 0)
			drawLabel(app.monsterKilled, 390, 252)
			
		elif app.gameover == "Win":
			drawRect(0, 0, 700, 400, fill = "gray", opacity = 50)
			#draw summary pannel
			drawImage(app.win, 0, 0)
			drawLabel(app.monsterKilled, 387, 250, bold = True, fill = rgb(229, 181, 55))
			score = 10*app.carrotCurrLife
			drawLabel(score, 430, 222, bold = True, size = 30, fill = rgb(229, 181, 55))
			length = 230//10*app.carrotCurrLife
			drawRect(231, 276, length, 21, fill = rgb(241, 122, 0))
			drawImage(app.frame, 345, 290, align = "center")
			drawImage(app.coin, 217+length, 290, align = "center")

	


def changeCellIndex(app, row, col, index):
	app.cells[row][col] = index
	#print(app.cells)

def checkIfValid(app, row, col, intendIndex):
	return app.cells[row][col] == intendIndex

			



def getWeaponChoiceCell(cx, cy):
	rx = 0
	ry = 0
	for x in range(95, 596,50):
		for y in range(75, 326, 50):
			if distance(cx, cy, x, y) > 25:
				continue
			else:
				rx = x
				ry = y
	return rx,ry

def onMouseDrag(app, mouseX, mouseY):
	pass




def takeStep(app):
	
	pass

def onMousePress(app, mouseX, mouseY):
	if app.show == "showBackground":
		print("111")
		if (mouseX > 550 and mouseX < 660 and 
			mouseY > 40 and mouseY < 105):
			print("222")
			app.show = "showInstruction"
		elif distance(mouseX, mouseY, 100, 290) <= 40:
			app.show = "showWeaponGallery"
		elif distance(mouseX, mouseY, 600, 300) <= 50:
			app.show = "showStation"

	elif app.show == "showInstruction":
		if distance(mouseX, mouseY, 40, 40) <= 30:
			app.show = "showBackground"

	elif app.show == "showWeaponGallery":
		if distance(mouseX, mouseY, 40, 40) <= 30:
			app.show = "showBackground"

	elif app.show == "showStation":
		if distance(mouseX, mouseY, 40, 40) <= 30:
			app.show = "showBackground"
		elif distance(mouseX, mouseY, 150, 200) <= 50:
			app.show = "play game"
			app.station = 1
			app.map = app.maps.a
			print(app.map)
			newGame(app)
			
		elif distance(mouseX, mouseY, 350, 200) <= 50:
			app.show = "play game"
			app.station = 2
			app.map = app.maps.b
			print(app.map)
			newGame(app)
			
		elif distance(mouseX, mouseY, 550, 200) <= 50:
			app.show = "play game"
			app.station = 3
			app.map = app.maps.c
			print(app.map)
			newGame(app)
			

	elif app.show == "play game": #when start playing
		if app.gameover == False:
			#pause the game and show grid
			if mouseY < 50:
				if distance(mouseX, mouseY, 120, 25) <= 23:
					app.pause = not app.pause
				if distance(mouseX, mouseY, 70, 25) <= 23:
					app.show = "showStation"
				if app.pause == True:
					app.showGrid = True
				elif app.pause == False:
					app.showGrid = False

			elif mouseY >= 50 and mouseY <= 350 and mouseX >=70 and mouseX <= 620:
				#show the weapon choice
				if app.placeWeapon == False:
					for (x,y) in app.map:
						if distance(mouseX, mouseY, x, y) <= 23:
							continue
						else:
							app.showWeaponChoice = True
							print("111")
							app.weaponChoiceX = mouseX
							app.weaponChoiceY = mouseY
							app.cellX, app.cellY = getWeaponChoiceCell(app.weaponChoiceX, app.weaponChoiceY)
							app.placeWeapon = True
							break

				#choice the weapon
				elif app.placeWeapon == True:
					print("here")
					if app.weaponChoice == 2:
						if (mouseX > (app.cellX - 41) and mouseY > (app.cellY - 72.5) and
							mouseX < (app.cellX + 41)and mouseY < (app.cellY + 72.5)):
							app.showWeaponChoice = False
							app.placeWeapon = False					
							app.placeX = mouseX
							app.placeY = mouseY
							#choose weapon
							if app.station == 1:
								#canoon		
								if distance(app.cellX-25, app.cellY-50, app.placeX, app.placeY) <= 16:
									if app.money >= 100: #if have money
										#check if valid
										i = (app.cellY-75)//50
										j = (app.cellX-95)//50
										if checkIfValid(app, i, j, ISEMPTY):
											app.canoonList.append((app.cellX, app.cellY))
											app.money -= 100
										#generate bullet
										bullet = BottleCanoonBullet(app.cellX, app.cellY)
										app.canoonBulletDicCopy[bullet.count] = (bullet.x, bullet.y)
										app.canoonBulletDic[bullet.count] = (bullet.x, bullet.y)
								#ice star
								elif distance(app.cellX+25, app.cellY-50, app.placeX, app.placeY) <= 16:
									if app.money >= 220: #if have money
										#check if valid
										i = (app.cellY-75)//50
										j = (app.cellX-95)//50
										if checkIfValid(app, i, j, ISEMPTY):
											app.iceStarList.append((app.cellX, app.cellY))
											app.money -= 220
										#generate bullet
										bullet = IceStarBullet(app.cellX, app.cellY)
										app.iceStarBulletDicCopy[bullet.count] = (bullet.x, bullet.y)
										app.iceStarBulletDic[bullet.count] = (bullet.x, bullet.y)
							elif app.station == 2:
								#rocket		
								if distance(app.cellX-25, app.cellY-50, app.placeX, app.placeY) <= 16:
									if app.money >= 220: #if have money
										#check if valid
										i = (app.cellY-75)//50
										j = (app.cellX-95)//50
										if checkIfValid(app, i, j, ISEMPTY):
											app.rocketList.append((app.cellX, app.cellY))
											app.money -= 220
										#generate bullet
										bullet = RocketBullet(app.cellX, app.cellY)
										app.rocketBulletDicCopy[bullet.count] = (bullet.x, bullet.y)
										app.rocketBulletDic[bullet.count] = (bullet.x, bullet.y)
								#canoon		
								elif distance(app.cellX+25, app.cellY-50, app.placeX, app.placeY) <= 16:
									if app.money >= 100: #if have money
										#check if valid
										i = (app.cellY-75)//50
										j = (app.cellX-95)//50
										if checkIfValid(app, i, j, ISEMPTY):
											app.canoonList.append((app.cellX, app.cellY))
											app.money -= 100
										#generate bullet
										bullet = BottleCanoonBullet(app.cellX, app.cellY)
										app.canoonBulletDicCopy[bullet.count] = (bullet.x, bullet.y)
										app.canoonBulletDic[bullet.count] = (bullet.x, bullet.y)
							elif app.station == 3:
								#ice star
								if distance(app.cellX-25, app.cellY-50, app.placeX, app.placeY) <= 16:
									if app.money >= 220: #if have money
										#check if valid
										i = (app.cellY-75)//50
										j = (app.cellX-95)//50
										if checkIfValid(app, i, j, ISEMPTY):
											app.iceStarList.append((app.cellX, app.cellY))
											app.money -= 220
										#generate bullet
										bullet = IceStarBullet(app.cellX, app.cellY)
										app.iceStarBulletDicCopy[bullet.count] = (bullet.x, bullet.y)
										app.iceStarBulletDic[bullet.count] = (bullet.x, bullet.y)
								#rocket		
								elif distance(app.cellX+25, app.cellY-50, app.placeX, app.placeY) <= 16:
									if app.money >= 220: #if have money
										#check if valid
										i = (app.cellY-75)//50
										j = (app.cellX-95)//50
										if checkIfValid(app, i, j, ISEMPTY):
											app.rocketList.append((app.cellX, app.cellY))
											app.money -= 220
										#generate bullet
										bullet = RocketBullet(app.cellX, app.cellY)
										app.rocketBulletDicCopy[bullet.count] = (bullet.x, bullet.y)
										app.rocketBulletDic[bullet.count] = (bullet.x, bullet.y)
						#click outside and do nothing
						else:
							app.placeWeapon = False				

		else:
			if mouseX > 230 and mouseX < 330 and mouseY > 320 and mouseY < 370:
				app.show = "showStation"
			elif mouseX > 360 and mouseX < 452 and mouseY > 320 and mouseY < 370:
				newGame(app)
		

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def onStep(app):
	
	#when start playing
	if app.show == "play game":
		app.count += 1
		app.onStepCount += 1
		app.stepsPerSeond = 1
		

		#updatw monster
		if app.pause == False:
			if app.countMonster < 10:
				if (time.time() - app.lastMonsterTime > 1):
					print(app.monsters)
					x,y = app.map[0]
					if app.n == 1:
						Purple(x,y)
						app.monsters.append(Purple(x,y))
						app.countMonster += 1
						app.lastMonsterTime = time.time()
					elif app.n == 2:
						Shark(x,y)
						app.monsters.append(Shark(x,y))
						app.countMonster += 1
						app.lastMonsterTime = time.time()
					elif app.n == 3:
						Bear(x,y)
						app.monsters.append(Bear(x,y))
						app.countMonster += 1
						app.lastMonsterTime = time.time()
					elif app.n == 4:
						Milk(x,y)
						app.monsters.append(Milk(x,y))
						app.countMonster += 1
						app.lastMonsterTime = time.time()
					elif app.n == 5:
						Green(x,y)
						app.monsters.append(Green(x,y))
						app.countMonster += 1
						app.lastMonsterTime = time.time()
					elif app.n == 6:
						Mummy(x,y)
						app.monsters.append(Mummy(x,y))
						app.countMonster += 1
						app.lastMonsterTime = time.time()
					

		#update monsters move
		if app.pause == False:	
			for monster in app.monsters:
				if type(monster) == Bear or type(monster) == Shark or type(monster) == Purple or type(monster) == Milk:
					app.perstep = 5
				elif type(monster) == Green or type(monster) == Mummy:
					app.perstep = 3
				L = app.monsterMap + [(app.carrotX, app.carrotY)]
				if (monster.x, monster.y) != app.monsterMap[-1]:
					prevx, prevy = monster.x, monster.y
					n = app.monsterMap.index((monster.x, monster.y))
					nextx, nexty = app.monsterMap[n+1]
					dx = nextx-prevx
					dy = nexty-prevy
					if app.onStepCount % app.perstep == 0:
						monster.x += dx
						monster.y += dy
			#eat carrot
			if app.monsters != []:
				if (app.monsters[0].x, app.monsters[0].y) == app.monsterMap[-1]:
					app.carrotCurrLife -= 1
					app.monsters.pop(0)
			
			if app.countMonster == 10:
				app.gameStart = True

			#bullet move	
			if app.monsters != []:
				if app.station == 1:
					#canoon bullet
					for key in app.canoonBulletDic:
						bulletx, bullety = app.canoonBulletDic[key]
						position = app.monsters[0].position + []
						if position != []:
							x, y = position[-1]
							canoonMonsterX = bulletx - x
							canoonMonsterY = bullety - y
							dx = canoonMonsterX//10
							dy = canoonMonsterY//10
							dis = distance(bulletx, bullety, x, y)
							if dis >= 20 and bulletx > 0 and bullety > 0:
								if app.onStepCount % 1 == 0:
									bulletx -= dx 
									bullety -= dy
									app.canoonBulletDic[key] = (bulletx, bullety)
							else:
								app.canoonBulletDic[key] = app.canoonBulletDicCopy[key]			
					#ice star bullet		
					for key in app.iceStarBulletDic:
						bulletx, bullety = app.iceStarBulletDic[key]
						position = app.monsters[0].position + []
						if position != []:
							x, y = position[-1]
							iceStarMonsterX = bulletx - x
							iceStarMonsterY = bullety - y
							dx = iceStarMonsterX//10
							dy = iceStarMonsterY//10
							dis = distance(bulletx, bullety, x, y)
							if dis >= 20 and bulletx > 0 and bullety > 0:
								if app.onStepCount % 1 == 0:
									bulletx -= dx 
									bullety -= dy
									app.iceStarBulletDic[key] = (bulletx, bullety)
							else:
								app.iceStarBulletDic[key] = app.iceStarBulletDicCopy[key]
				elif app.station == 2:
					#rocket
					for key in app.rocketBulletDic:
						bulletx, bullety = app.rocketBulletDic[key]
						position = app.monsters[0].position + []
						if position != []:
							x, y = position[-1]
							rocketMonsterX = bulletx - x
							rocketMonsterY = bullety - y
							dx = rocketMonsterX//10
							dy = rocketMonsterY//10
							dis = distance(bulletx, bullety, x, y)
							if dis >= 20 and bulletx > 0 and bullety > 0:
								if app.onStepCount % 1 == 0:
									bulletx -= dx 
									bullety -= dy
									app.rocketBulletDic[key] = (bulletx, bullety)
							else:
								app.rocketBulletDic[key] = app.rocketBulletDicCopy[key]
					#bottle canoon
					for key in app.canoonBulletDic:
						bulletx, bullety = app.canoonBulletDic[key]
						position = app.monsters[0].position + []
						if position != []:
							x, y = position[-1]
							canoonMonsterX = bulletx - x
							canoonMonsterY = bullety - y
							dx = canoonMonsterX//10
							dy = canoonMonsterY//10
							dis = distance(bulletx, bullety, x, y)
							if dis >= 20 and bulletx > 0 and bullety > 0:
								if app.onStepCount % 1 == 0:
									bulletx -= dx 
									bullety -= dy
									app.canoonBulletDic[key] = (bulletx, bullety)
							else:
								app.canoonBulletDic[key] = app.canoonBulletDicCopy[key]		
				
				elif app.station == 3:	
					#ice star bullet		
					for key in app.iceStarBulletDic:
						bulletx, bullety = app.iceStarBulletDic[key]
						position = app.monsters[0].position + []
						if position != []:
							x, y = position[-1]
							iceStarMonsterX = bulletx - x
							iceStarMonsterY = bullety - y
							dx = iceStarMonsterX//10
							dy = iceStarMonsterY//10
							dis = distance(bulletx, bullety, x, y)
							if dis >= 20 and bulletx > 0 and bullety > 0:
								if app.onStepCount % 1 == 0:
									bulletx -= dx 
									bullety -= dy
									app.iceStarBulletDic[key] = (bulletx, bullety)
							else:
								app.iceStarBulletDic[key] = app.iceStarBulletDicCopy[key]
					#rocket
					for key in app.rocketBulletDic:
						bulletx, bullety = app.rocketBulletDic[key]
						position = app.monsters[0].position + []
						if position != []:
							x, y = position[-1]
							rocketMonsterX = bulletx - x
							rocketMonsterY = bullety - y
							dx = rocketMonsterX//10
							dy = rocketMonsterY//10
							dis = distance(bulletx, bullety, x, y)
							if dis >= 20 and bulletx > 0 and bullety > 0:
								if app.onStepCount % 1 == 0:
									bulletx -= dx 
									bullety -= dy
									app.rocketBulletDic[key] = (bulletx, bullety)
							else:
								app.rocketBulletDic[key] = app.rocketBulletDicCopy[key]	
					
		#make life damage
		if app.monsters != []:
			monster = app.monsters[0]
			if monster.position != []:
				if app.station == 1:
					for key in app.canoonBulletDic:
						(x, y) = app.canoonBulletDic[key]
						(bx, by) = monster.position[-1]
						if distance(x, y, bx, by) <= 20:
							monster.currLifePoint -= 10

					for key in app.iceStarBulletDic:
						(x, y) = app.iceStarBulletDic[key]
						(bx, by) = monster.position[-1]
						if distance(x, y, bx, by) <= 20:
							monster.currLifePoint -= 20
							app.perstep = 6

				elif app.station == 2:
					for key in app.rocketBulletDic:
						(x, y) = app.rocketBulletDic[key]
						(bx, by) = monster.position[-1]
						if distance(x, y, bx, by) <= 20:
							monster.currLifePoint -= 40
					
					for key in app.canoonBulletDic:
						(x, y) = app.canoonBulletDic[key]
						(bx, by) = monster.position[-1]
						if distance(x, y, bx, by) <= 20:
							monster.currLifePoint -= 10

				elif app.station == 3:
					for key in app.rocketBulletDic:
						(x, y) = app.rocketBulletDic[key]
						(bx, by) = monster.position[-1]
						if distance(x, y, bx, by) <= 20:
							monster.currLifePoint -= 40
						
					for key in app.iceStarBulletDic:
						(x, y) = app.iceStarBulletDic[key]
						(bx, by) = monster.position[-1]
						if distance(x, y, bx, by) <= 20:
							monster.currLifePoint -= 20
							app.perstep = 6

			#earn money		
			if monster.currLifePoint <= 0:
				app.monsters.pop(0)
				app.money += 14  ############################33333333
				app.monsterKilled += 1
		
		#game over
		if app.gameStart == True:
			#carrot dies and game over, loose
			if app.carrotCurrLife == 0:
				app.gameover = "Loose"
				app.pause = True
			#last round and all monsters dies, win
			elif app.currentRound == 5 and app.monsters == []:
				app.gameover = "Win"
				app.pause = True
			#all monster killed and start a new round
			elif app.monsters == [] and app.currentRound <= 4:
				app.currentRound += 1
				newRound(app)
	



def main():
	runApp(width = 700, height = 400)

main()