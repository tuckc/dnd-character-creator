#UserInterface.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
#from ..races import *
#print sys.path
#print '---------------------------------------'
sys.path.append(sys.path[0][:-2]+"races")
sys.path.append(sys.path[0][:-2])
#print 'NEW path --------------->', sys.path
import dragonborn
import human
import gnome
import halforc
import halfling
import elf
import halfelf
import tiefling
import dwarf
import subrace_dwarf_gui
import ancestry_dragonborn_gui
import subrace_gnome_gui
import subrace_elf_gui
import subrace_halfling_gui
import language_human_gui
import subrace_halfelf_gui
import stats_gui

class RaceWindow(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.tab_window = parent
		self.window_title = QLabel("Choose your race!")
		self.title = QLabel("Your current race is: ")	
		self.label = QLabel()
		self.setup()
		
	def handler(self,pickedRace):
		if pickedRace == 'dwarf':
			self.race = subrace_dwarf_gui.SubraceDwarf(self)
			self.tab_window.main_window.raceset = True

			#print "dwarf charisma->",self.tab_window.main_window.race.charisma
			#SUBRACE PAGES FINISHED

		elif pickedRace == 'elf':
			self.race=subrace_elf_gui.SubraceElf(self)
			self.tab_window.main_window.raceset = True
			#print "elf charisma->",self.tab_window.main_window.race.charisma
			#SUBRACE PAGES FINISHED


		elif pickedRace == 'dragonborn':
			self.race=ancestry_dragonborn_gui.AncestryDragonborn(self)
			self.tab_window.main_window.raceset = True
			#print "dragonborn charisma->",self.tab_window.main_window.race.features.charisma
			#ANCESTRY PAGE FINISHED

		elif pickedRace == 'halfling':
			self.race=subrace_halfling_gui.SubraceHalfling(self)
			self.tab_window.main_window.raceset = True
			#print "halfling charisma->",self.tab_window.main_window.race.charisma
			#SUBRACE PAGE FINISHED

		elif pickedRace == 'gnome':
			self.race=subrace_gnome_gui.SubraceGnome(self)
			self.tab_window.main_window.raceset = True
			#print "gnome charisma->",self.tab_window.main_window.race.charisma
			#SUBRACE PAGES FINISHED

		elif pickedRace == 'halforc':
			self.tab_window.main_window.race=halforc.Halforc()
			self.tab_window.main_window.raceset = True
			self.label.setText("Half-Orc")
			#print "halforc charisma->",self.tab_window.main_window.race.charisma
			#PAG FINISHED
		
		elif pickedRace == 'tiefling':
			self.tab_window.main_window.race=tiefling.Tiefling()
			self.tab_window.main_window.raceset = True
			self.label.setText("Tiefling")
			#print "tiefling charisma->",self.tab_window.main_window.race.charisma
			#PAGES FINISHED


		elif pickedRace == 'human':
			self.race=language_human_gui.LanguageHuman(self)
			self.tab_window.main_window.raceset = True
			#self.label.setText("Human")
			#print "human charisma->",self.tab_window.main_window.race.charisma



		elif pickedRace == 'halfelf':
			self.race=subrace_halfelf_gui.SubraceHalfelf(self)
			self.tab_window.main_window.raceset = True
			#self.label.setText("Half-Elf")
			#print "halfelf charisma->",self.tab_window.main_window.race.charisma


		
		

	def setup(self):	
		self.gnomeButton=QPushButton('Gnome')
		self.gnomeButton.setToolTip("Gnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.<br>Gnomes average slightly over 3 feet tall and weigh 40 to 45 pounds.<br>------------Stats------------<br>Intelligence +2<br>Speed:25 Feet<br>Skills:Darkvision, Gnome Cunning<br>Languages: Common and Gnomish<br>Subrace: Yes")
		self.gnomeButton.clicked.connect(lambda :self.handler("gnome"))
		
						
		self.halflingButton=QPushButton("Halfling")
		self.halflingButton.setToolTip("these wanderers love peace, food, hearth, and home, though home might be a wagon jostling along an dirt road or a raft floating downriver.<br>The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense.<br> Standing about 3 feet tall, they appear relatively harmless and so have managed to survive for centuries in the shadow of empires and on the edges of wars and political strife<br>------------Stats------------<br>Dexterity +2<br>Speed:25 Feet<br>Skills:Lucky, Brave, Halfling Nimbleness<br>Languages: Common and Halfling<br>Subrace: Yes")
		self.halflingButton.clicked.connect(lambda :self.handler("halfling"))	

		self.dwarfButton=QPushButton("Dwarf")
		self.dwarfButton.setToolTip("Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.<br> Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller.<br> Their courage and endurance are also easily a match for any of the larger folk.<br>------------Stats------------<br>Constitution +2<br>Speed:25 Feet<br>Skills:Darkvision, Dwarven Resilience, Dwarven Combat Training, Tool Proficiency, Stonecunning<br>Languages: Dwarvish<br>Subrace: Yes")
		self.dwarfButton.clicked.connect(lambda :self.handler("dwarf"))

		self.elfButton=QPushButton("Elf")
		self.elfButton.setToolTip("Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.<br>With their unearthly grace and fine features, elves appear hauntingly beautiful to humans and members of many other races.<br>------------Stats------------<br>Dexterity +2<br>Speed:30 Feet<br>Skills:Darkvision, Keen Senses, Fey Ancestry, Trance<br>Languages: Common and Elvish<br>Subrace: Yes")
		self.elfButton.clicked.connect(lambda :self.handler("elf"))

		self.halfelfButton=QPushButton("Half-Elf")
		self.halfelfButton.setToolTip("Walking in two w orlds but truly belonging to neither,half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes o f the elves.<br>Many half-elves,unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.<br>------------Stats------------<br>Charisma +2 and 2 Skills of your choice +1<br>Speed:30 Feet<br>Skills:Darkvision, Fey Ancestry, Skill Versatility<br>Languages: Common, Elvish, And 1 more of your choice<br>Subrace: No")
		self.halfelfButton.clicked.connect(lambda :self.handler("halfelf"))

		self.tieflingButton=QPushButton("Tiefling")
		self.tieflingButton.setToolTip("To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye.<br> This is the lot of the tiefling. <br>Their appearance and their nature are not their fault but the result of an ancient sin.<br>------------Stats------------<br>Charisma +2 and Intelligence +1<br>Speed:30 Feet<br>Skills:Darkvision, Hellish Resistance, Infernal Legacy<br>Languages: Common and Infernal<br>Subrace: No")
		self.tieflingButton.clicked.connect(lambda :self.handler("tiefling"))

		self.humanButton=QPushButton("Human")
		self.humanButton.setToolTip("In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons.<br>Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.<br>------------Stats------------<br>Each Base Score +1<br>Speed:30 Feet<br>Skills: 1 Skill and Feat of your choice<br>Languages: Common and Another of Your Choice<br>Subrace: No")
		self.humanButton.clicked.connect(lambda :self.handler("human"))

		self.dragonbornButton=QPushButton("Dragonborn")
		self.dragonbornButton.setToolTip("Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension.<br> Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids.<br>------------Stats------------<br>Strength +1 and Charisma +1<br>Speed:30 Feet<br>Skills:Dragonic Ancestry, Breath Weapon, Damage Resistance<br>Languages: Common and Dragonic<br>Subrace: No")
		self.dragonbornButton.clicked.connect(lambda :self.handler("dragonborn"))		
		

		self.halforcButton=QPushButton("Half-Orc")
		self.halforcButton.setToolTip("Whether united under the leadership of a mighty warlock or having fought to a standstill after years of conflict, orc and human tribes sometimes form alliances, joining forces into a larger horde to the terror of civilized lands nearby. When these alliances are sealed by marriages, half-orcs are born.<br> Some half-orcs rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full-blooded orc rivals.<br>------------Stats------------<br>Strength +2 and Constitution +1<br>Speed:30 Feet<br>Skills:Darkvision, Menacing, Relentless Endurance, Savage Attack<br>Languages: Common and Orc<br>Subrace: No")
		self.halforcButton.clicked.connect(lambda :self.handler("halforc"))		




		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()
		self.titlebox = QHBoxLayout()
		self.titlebox.addWidget(self.title)
		self.titlebox.addWidget(self.label)


		self.vbox.addWidget(self.window_title)
		self.vbox.addLayout(self.titlebox)
		self.racepic = QLabel(self)
		self.pixmap = QPixmap('race.jpg')
		self.racepic.setPixmap(self.pixmap)
		self.picbox.addWidget(self.racepic)
		self.racepic.resize(self.width()-50,self.height()-400)
		
		self.buttonbox.addWidget(self.gnomeButton)		
		self.buttonbox.addWidget(self.halflingButton)		
		self.buttonbox.addWidget(self.dwarfButton)
		self.buttonbox.addWidget(self.elfButton)
		self.buttonbox.addWidget(self.halfelfButton)
		self.buttonbox.addWidget(self.tieflingButton)
		self.buttonbox.addWidget(self.humanButton)
		self.buttonbox.addWidget(self.dragonbornButton)
		self.buttonbox.addWidget(self.halforcButton)

		
		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.clicked.connect(self.confirm)

		self.setLayout(self.vbox)
		self.vbox.addLayout(self.picbox)
		self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.confirmButton)

		self.show()


	def confirm(self):
		if self.tab_window.main_window.raceset:
			if self.tab_window.main_window.statspagecount < 1:
				self.tab_window.RaceWindowObject = stats_gui.StatsWindow(self.tab_window)
				self.tab_window.addTab(self.tab_window.RaceWindowObject, "&Stats")
				self.tab_window.setCurrentIndex(2)
				self.window_title.setText("Race confirmed")
				self.tab_window.main_window.statspagecount = 1
			else:
				self.tab_window.setCurrentIndex(2)
		else:
			self.window_title.setText("YOU MUST CHOOSE A RACE TO CONTINUE!")


	

if __name__ == "__main__":

	app = QApplication(sys.argv)
	main_window = RaceWindow()
	app.exec_()
