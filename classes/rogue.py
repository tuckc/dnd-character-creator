from char_class import Class

class Rogue(Class):
    def __init__(self, skills, equipment, expert1, expert2):
        Class.__init__(self)
        self.other = [
            'Light Armor',
            'Simple Weapons',
            'Hand Crossbows',
            'Longswords',
            'Rapiers',
            'Shortswords',
            'Thieves\' Tools'
        ]
        self.features = [
            'Expertise: '+ expert1 + ', ' + expert2,
            'Sneak Attack',
            'Thieves\' Cant'
        ]
        self.saving_throws = ['Dexterity', 'Intelligence']
        self.skills = skills
        self.equipment = equipment
        self.expertise = [expert1, expert2]

    def __str__(self):
        return super(Rogue, self).__str__()
