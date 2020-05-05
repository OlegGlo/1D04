
class dog:
    def __init__(self,breed,name,weight):
        self.breed = breed
        self.name = name
        self.weight = weight
        self.age = 0
        self.tricks = []

    def speak(self):
        print("speak method")

    def learnTrick(self,newTrick):
        self.tricks.append(newTrick)
    
    def getVetRec(self):
        return self.name, self.breed, self.age , self.weight

    def haveBDay(self):
        self.age += 1
        print("happy ", self.name," !")

dog1 = dog("asad","sasd",500)
dog2 = dog1
dog2.learnTrick("trick1")
dog3 = dog2
dog3.learnTrick("tricl2")
print("done")

hello = dog1.getVetRec()
print(type(hello))




