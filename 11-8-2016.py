### class for peoples' information and how they want it dealt with ##########
class Person:
    def createName(self, name):
        self.name = name
    def birthday(self, birthdate):
        self.birthdate = birthdate
    def address(self, address):
        self.address = address
    def displayName(self):
        return self.name
    def displayBirthday(self):
        return self.birthdate
    def displayAddress(self):
        return self.address
    def displayInfo(self, boolean):
        self.boolean = boolean
    def publicOrNah(self):
        if self.boolean == False:
            return "Don't display Info Publicly"
        else:
            return "Display my Info Please Baby"

Brigham = Person()
James = Person()
Brigham.createName("Brigham")
James.createName("James")
Brigham.birthday("10 / 28 / 20003")
James.birthday("9 / 5 / 3003")
Brigham.address("34443 E apple LN")
James.address("566454 N kickass ave")
Brigham.displayInfo(True)
James.displayInfo(False)
print(Brigham.displayName())
print(Brigham.displayBirthday())
print(Brigham.displayAddress())
print(James.displayName())
print(James.displayBirthday())
print(James.displayAddress())
print(Brigham.publicOrNah())
print(James.publicOrNah())

##### worksheet from BBLEARN ################################################
'''
1)
x = cyclops.get_identity()
Scott Summers

2)
wolverine.powers[1] "Adamantium Claws"
x = wolverine.powers
Healing Factor, Adamantium Claws, Retractable Bone Claws, Enhanced Senses

3)
cyclops.powers = "Laser Eyes"
x = cyclops.powers[0]
None

4)
professorX = Mutant()
professorX.set_identity("Charles Francis")
x = professorX.get_powers()
None

5)
x = cyclops.get_powers()
del(cyclops)
Projects concussive force from his Eyes

6)
gambit.powers[0] = gambit.powers[1]
gambit.powers[2] = gambit.powers[0]
x = gambit.get_powers()
Enhanced Agility, Hypnotic Charm, Enhanced Agility

7)
x = gambit.get_powers().sort()
Enhanced Agility, Explosive Kinetic Energy, Hypnotic Charm

8)
storm = Mutant()
storm.set_identity("Ororo Monroe")
storm.set_powers("Weather manipulation")
x = storm.get_powers()[0]
Weather manipulation

9)
x  = gambit.get_identity()
