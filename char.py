import json
import random
from decimal import Decimal
# Character Name
# pronouns
# Eye Color
# Skin Color
# Hair Color
# Hair Type
# Hair Thickness
# Personality
# 	Lax <-> Serious
# 	Somber <-> Lively
# 	Humble <-> Haughty
# 	Cursed <-> Lucky
# 	Selfish <-> Selfless
# Skills
# 	Singing
# 	Cooking
# 	Animal Handling
# 	Studying
#   Faith <-> Battle (stronger affinity begets more points for magic <-> weapons)
# 	Weapons
# 		Sword
# 		Axe
# 		Lance
# 		Bow
# 		Fists
# 	Magic
# 		Destructive
# 		Healing
class Person(object):
	def __init__(self, name, appearance, personality, skills):
		with open('data/firstNames.json') as firstNamesJson:
			self.firstNames = json.load(firstNamesJson)['firstNames']
		with open('data/lastNames.json') as lastNamesJson:
			self.lastNames = json.load(lastNamesJson)['lastNames']
		# with open('data/pronouns.json') as pronounsJson:
		#     self.pronouns = json.load(pronounsJson)
		if name:
			self.firstName = name[0]
			self.lastName = name[1]
		else:
			self.firstName = random.choice(self.firstNames)
			self.lastName = random.choice(self.lastNames)
		# self.pronoun = random.choice(self.pronouns)
		self.appearance = appearance
		self.personality = personality
		self.skills = skills
		self.level = 1
		self.job = 'Squire'
	
	
	def levelUp(self, levelsGained):
		self.skills.levelUp(levelsGained) # assign skill points
		self.level += levelsGained # numerical level
	
	def characterSheet(self):
		print('{} {}\t\t Lv{} {}'.format(self.firstName, self.lastName, self.level, self.job))
		print()
		print('Camp skills:')
		print('\t{}: {}\t\t{}: {}'.format('Singing', self.skills.singing, 'Studying', self.skills.studying))
		print('\t{}: {}\t\t{}: {}'.format('Cooking', self.skills.cooking, 'Apothecary', self.skills.apothecary))
		print('\t{}: {}'.format('Animal Handling', self.skills.animals))
		print('\nBattle skills:')
		print('\t{}: {}\t\t{}: {}'.format('Sword', self.skills.sword, 'Fist', self.skills.fists))
		print('\t{}: {}\t\t\t{}: {}'.format('Axe', self.skills.axe, 'White Magic', self.skills.blackMagic))
		print('\t{}: {}\t\t{}: {}'.format('Lance', self.skills.lance, 'Black Magic', self.skills.whiteMagic))
		print('\t{}: {}'.format('Bow', self.skills.bow))
		print('--------------------')
		#print('\nYour skill total is {}'.format((self.singing + self.cooking + self.animals + self.studying + self.apothecary + self.sword + self.axe + self.lance + self.bow + self.fists + self.blackMagic + self.whiteMagic)))

class Personality(object):
	def __init__(self, serious, lively, haught, luck, selfless):
		pass

class Appearance(object):
	def __init__(self):
		self.eyeColors = ['green', 'hazel', 'brown', 'blue', 'gray', 'amber', 'red']
		self.skinColors = ['light','medium-light','medium','medium-dark','dark']
		self.hairColors = {'brown' :('light-brown', 'brown', 'dark-brown'),'blonde': ('toe-head','blonde','dirty blonde'),'black': ('white','grey','black'), 'red':('pink','red', 'crimson'),'orange': ('light-orange', 'orange', 'umber'),'green':('mint', 'green', 'forest green'),'blue': ('periwinkle', 'blue', 'navy blue')}
		self.hairTypes = ['straight', 'wavy', 'curly', 'coily']
		self.hairThickness = ['fine', 'medium', 'thick']

class Skills(object):
	def __init__(self, singing=2, cooking=2, animals=2, studying=2, apothecary=2, sword=2, axe=2, lance=2, bow=2, fists=2, blackMagic=2, whiteMagic=2):
		singingWeight = self._genSkillWeight()
		cookingWeight = self._genSkillWeight()
		animalsWeight = self._genSkillWeight()
		studyingWeight = self._genSkillWeight()
		apothecaryWeight = self._genSkillWeight()
		#self.faithWeight = self._genSkillWeight()
		swordWeight = self._genSkillWeight()
		axeWeight = self._genSkillWeight()
		lanceWeight = self._genSkillWeight()
		bowWeight = self._genSkillWeight()
		fistsWeight = self._genSkillWeight()
		blackMagicWeight = self._genSkillWeight()
		whiteMagicWeight = self._genSkillWeight()
		
		self.campSkills = {
			'singing': {'skillID': 0, 'skillTotal': singing, 'skillWeight':self._genSkillWeight()},
			'cooking': {'skillID': 1, 'skillTotal': cooking, 'skillWeight': self._genSkillWeight()},
			'animals': {'skillID': 2, 'skillTotal': animals, 'skillWeight': self._genSkillWeight()},
			'studying': {'skillID': 3, 'skillTotal': studying, 'skillWeight': self._genSkillWeight()},
			'apothecary': {'skillID': 4, 'skillTotal': apothecary, 'skillWeight': self._genSkillWeight()}
		}
		
		self.battleSkills = {
			'sword': {'skillID': 5, 'skillTotal': sword, 'skillWeight': self._genSkillWeight()},
			'axe': {'skillID': 6, 'skillTotal': axe, 'skillWeight': self._genSkillWeight()},
			'lance': {'skillID': 7, 'skillTotal': lance, 'skillWeight': self._genSkillWeight()},
			'bow': {'skillID': 8, 'skillTotal': bow, 'skillWeight': self._genSkillWeight()},
			'fists': {'skillID': 9, 'skillTotal': fists, 'skillWeight': self._genSkillWeight()},
			'blackMagic': {'skillID': 10, 'skillTotal': blackMagic, 'skillWeight': self._genSkillWeight()},
			'whiteMagic': {'skillID': 11, 'skillTotal': whiteMagic, 'skillWeight': self._genSkillWeight()}
		}
		
		self.levelUp(3)
		
		
	def _genSkillWeight(self, suggestedWeights=None):
		if suggestedWeights: # skills generated for a child character
			weightOffset = (random.randint(1, 3) - 2) / 10.0 # either -.1, +.1, or 0
			weightRaw = sum(suggestedWeights) / len(suggestedWeights) # avg parents' weights
			weight = round(weightRaw + weightOffset, 1) # combine
		else:
			weightOffset = random.randint(1, 5) # average weightOffset is .3
			weightRaw = Decimal((weightOffset / 10.0) + .7) # adding 0.7 gives us an avg weight of 1 but a range of .8 -> 1.2
			weight = round(weightRaw, 1) # round to one decimal place
		
		if weight > 1.3:
			weight = 1.3
		elif weight < 0.8:
			weight = 0.8
		return weight
		
		
	def _groupSkills(self):
		pass
	
	def _levelSkills(self, items, skillType=None):
		'''
		To explain what is going on here, and why it was built this way
		
		Goal: Create a random stat generator that avoided the following problems:
		1. If all stats are p even with eachother, there's nothing unique or interesting about characters. 
		I want to aim for characters with clear, but not debilitating, weaknesses and strengths.
		2. Even if stats start unique early, additional levelups can even a character out. A 5 point 
		difference means a lot less between  100 & 105 vs 2 & 7. We should let current stats influence 
		how skill increases are weighted.
		
		Implementation:
		We have to understand how skill points are represented during skill generation. We seed a list with 
		two integers, up to the total number of items. Each instance of an integer in this list represents 
		one skill point. The integer itself represents the skill the point is for. 
		
		For example, if the function were provided with 5 items:
		baseSkillPoints = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
		For each integer in the range of 5 (items), we put that integer into the list twice.
		
		This seeds our base skill points. We then take items, and increase it by 20%. This number becomes 
		the number of skillpoints we'll assign. So for example, if I had 10 "items", we'd assign 12 skill 
		points across them. We then apply 12 points 5 times, to simulate 5 levelups. We do this by picking 
		a random skill point out of our current skill points, and add another to the list. We do this for 
		every one of the 12 skill points, and then repeat 4 more times. With each generation or levelup,
		strengths and weeknesses naturally develop as items that get skill points are more likely to be 
		chose in the next levelup.
		
		Future improvements:
		Allow for different "types" of levelup to produce more or less unique characters. A "goofy" 
		character might have night variance while a "disciplined" one might be more well-rounded.
		
		Arguments
		items (list): a list of skills you'd like to seed points into
		'''
		
		skills = []
		numberOfSkills = 0
		
		if skillType == "camp":  
			for data in self.campSkills.values():
				numberOfSkills = len(data)
				for point in range(data['skillTotal']):
					skills.append(data['skillID'])  
		elif skillType == "battle":
			for data in self.battleSkills.values():
				numberOfSkills = len(data)
				for point in range(data['skillTotal']):
					skills.append(data['skillID'])
		
		currentSkillPoints = skills
		pointsPerRound = int(round(numberOfSkills * 1.2)) # increase "items" by 20% to get the number of skill points we'll hand out per round, after 5 rounds it should avg out to about 6 points given to each skill (plus the 2 base points)
		for i in range(5):
			skills = currentSkillPoints
			for j in range(pointsPerRound):
				currentSkillPoints.append(random.choice(skills))
		
		if skillType == "camp":
			self.singing = skills.count(self.campSkills['singing']['skillID'])
			self.cooking = skills.count(self.campSkills['cooking']['skillID'])
			self.animals = skills.count(self.campSkills['animals']['skillID'])
			self.studying = skills.count(self.campSkills['studying']['skillID'])
			self.apothecary = skills.count(self.campSkills['apothecary']['skillID'])
		elif skillType == "battle":
			self.sword = skills.count(self.battleSkills['sword']['skillID'])
			self.axe = skills.count(self.battleSkills['axe']['skillID'])
			self.lance = skills.count(self.battleSkills['lance']['skillID'])
			self.bow = skills.count(self.battleSkills['bow']['skillID'])
			self.fists = skills.count(self.battleSkills['fists']['skillID'])
			self.blackMagic = skills.count(self.battleSkills['blackMagic']['skillID'])
			self.whiteMagic = skills.count(self.battleSkills['whiteMagic']['skillID'])
		
		self._groupSkills()

	def _levelSkill(self, skill, weight):
		pass

	def levelUp(self, levelsGained=1):
		for i in range(levelsGained):
			self._levelSkills(len(self.campSkills.items()), 'camp')
			self._levelSkills(len(self.battleSkills.items()), 'battle')

class Character(Person):
	def __init__(self, parents=None):
		with open('data/firstNames.json') as firstNamesJson:
			self.firstNames = json.load(firstNamesJson)['firstNames']
		with open('data/lastNames.json') as lastNamesJson:
			self.lastNames = json.load(lastNamesJson)['lastNames']
		
		singing = 0
		cooking = 0
		animals = 0
		studying = 0
		apothecary = 0
		sword = 0
		axe = 0
		lance = 0
		bow = 0
		fists = 0
		blackMagic = 0
		whiteMagic = 0
		
		for parent in parents:
			singing += parent.skills.singing
			cooking += parent.skills.cooking
			animals += parent.skills.animals
			studying += parent.skills.studying
			apothecary += parent.skills.apothecary
			sword += parent.skills.sword
			axe += parent.skills.axe
			lance += parent.skills.lance
			bow += parent.skills.bow
			fists += parent.skills.fists
			blackMagic += parent.skills.blackMagic
			whiteMagic += parent.skills.whiteMagic
		
		singing = singing // len(parents)
		cooking = cooking // len(parents)
		animals = animals // len(parents)
		studying = studying // len(parents)
		apothecary = apothecary // len(parents)
		sword = sword // len(parents)
		axe = axe // len(parents)
		lance = lance // len(parents)
		bow = bow // len(parents)
		fists = fists // len(parents)
		blackMagic = blackMagic // len(parents)
		whiteMagic = whiteMagic // len(parents)
		
		skillTotal = singing + cooking + animals + studying + apothecary + sword + axe + lance + bow + fists + blackMagic + whiteMagic
		singing = round((singing/skillTotal) * 12)
		cooking = round((cooking/skillTotal) * 12)
		animals = round((animals/skillTotal) * 12)
		studying = round((studying/skillTotal) * 12)
		apothecary = round((apothecary/skillTotal) * 12)
		sword = round((sword/skillTotal) * 12)
		axe = round((axe/skillTotal) * 12)
		lance = round((lance/skillTotal) * 12)
		bow = round((bow/skillTotal) * 12)
		fists = round((fists/skillTotal) * 12)
		blackMagic = round((blackMagic/skillTotal) * 12)
		whiteMagic = round((whiteMagic/skillTotal) * 12)
		
		characterSkills = Skills(singing, cooking, animals, studying, apothecary, sword, axe, lance, bow, fists, blackMagic, whiteMagic)
		
		characterFirstName = random.choice(self.firstNames)
		characterLastName = random.choice(parents).lastName
		characterName = (characterFirstName, characterLastName)
		
		super().__init__(characterName,None,None,characterSkills)

class Interaction():
	def __init__(self):
		pass

parent1Skills = Skills()
parent1 = Person(None,None,None,parent1Skills)
parent1.levelUp(19)
parent1.characterSheet()


parent2Skills = Skills()
parent2 = Person(None,None,None,parent2Skills)
parent2.levelUp(19)
parent2.characterSheet()

parents = [parent1, parent2]

character = Character(parents)
character.characterSheet()
