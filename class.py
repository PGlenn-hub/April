
class Ennemy:


    def __init__(self, name, pronouns, possessive_pronouns, reflexive_pronouns, weapons):

        self.name = name
        self.pronouns = pronouns
        self.possessive_pronouns = possessive_pronouns
        self.reflexive_pronouns = reflexive_pronouns    
        self.weapons = weapons
#
#    def introduce(self):
#        print "My name is ", name, "."
#        print "I use ", pronouns, "pronouns, and my possessive pronouns are ", possessive_pronouns, "and my relfexive pronouns are ", reflexive_pronouns, "."
#        print "I will kill you with my ", weapons, "."
#
#
E1 = Ennemy("Greta", ["the woman", "she"], "her", "herself", "knife")
##Ennemy.introduce(E1)
print E1
