from race import Race

class Human(Race):
    def __init__(self, language):
        Race.__init__(self)
        self.strength = 1
        self.dexterity = 1
        self.constitution = 1
        self.intelligence = 1
        self.wisdom = 1
        self.charisma = 1
        self.languages = ['Common', language]
    def __str__(self):
        return super(Human,self).__str__()
        