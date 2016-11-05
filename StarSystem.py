import Orbitals
import random
import math


class StarSystem(Orbitals.Orbitals):
    def __init__(self, orbitalDistance, angle, name):
        Orbitals.Orbitals.__init__(self, orbitalDistance)
        self.angle = angle
        self.orbitalPeriod = 1   #A static Galaxy
        self.name = name
        self.maxOrbitalDistance = None




    def generate(self):

        pType = None    #'Rocky' or 'Gas Giant'
        pMass = 0 #This is in Earth Masses
        moons = 0 # number of moons

        #Star
        myStar = Orbitals.Star(self.name)
        myStar.generate()
        myPlanet = None

        self.addChild(myStar)


        #Generate the number of planets

        #Assume 1000Mkm has largest gas giants
        gasGiantMassModifier = [(1 / math.sqrt(2 * math.pi)) * math.e ** (-0.5 * ((x / 6) ** 2)) * 2.5 for x in range(-10, 11)]
        #There are 20 planet 'electron shells'
        orbitShells = [0.07 * (i * 15) ** 2 + 25 for i in range(20)]
        chancePlanet = 60
        planetNumber = 0

        #Planets
        suffix = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii',
                  'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'ix', 'xx']

        for i in range(0, 20):

            if random.randint(0, 100) < chancePlanet:
                orbitalDistance = orbitShells[i] + (orbitShells[i] * (random.randint(-7, 12)) / 100)
                planetNumber += 1
                if gasGiantMassModifier[i] + 0.25 > 1:
                    pType = 'Gas Giant'
                    pMass = gasGiantMassModifier[i] ** 3 * (255) + random.randint(0, 100)
                    moonChance = 500
                else:
                    pType='Rocky'
                    pMass=random.randint(1, 1000) / 1000 * 1.2 + 0.5
                    moonChance = 40
                moons = 0
                x = random.randint(0, 100)
                while x < moonChance:
                    moonChance -= x
                    moons += 1
                    x = random.randint(0, 100)
                #Create the planet object
                #print(" ".join(('Planet Number is', str(planetNumber))))
                myPlanet = Orbitals.Planet(orbitalDistance, " ".join( (self.name, suffix[planetNumber -1 ]) ), pType, pMass, moons )
                self.addChild(myPlanet)
            #print(myPlanet)

        #last object in system
        self.maxOrbitalDistance = myPlanet.orbitalDistance * 3

        self.update(10)



        #A check on generation
        # for item in self.children:
        #     print(item)


#A little test
#
# mySystem = StarSystem(10000000, 25)
# mySystem.generate()
# print(mySystem.children[1].angle)
# mySystem.update(55000000)
# print(mySystem.children[1].angle)
# print(mySystem.children[1].orbitalPeriod)
#
# mySystem.update(55000000)
# print(mySystem.children[1].angle)
