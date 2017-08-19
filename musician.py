## Python Classes project 3 - Musician.py


# PARENT CLASS:
class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

# CHILD CLASSES:
class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"]) # super() calls parent class

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
   
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Blam", "Thud"])
    
    def count(self):
        print("One! Two! One, two, three, four!")
    
    def combust(self):
        print("It's true. There was a little green globule on his drum seat.")
        print("Like a stain, really.")
        print("It was more of a stain than a globule, actually.")

class Band():
    def __init__(self):
        # instantiate classes
        self.derek = Bassist()
        self.david = Guitarist()
        self.mick = Drummer()
    
    def hired(self):
        member = str(input("Who do you want to hire: Bassist, Guitarist, or Drummer? "))
        if member == "Bassist":
            print("Say hello to our new Bassist, Derek!")
        elif member == "Guitarist":
            print("Say hello to our new Guitarist, David!")
        elif member == "Drummer":
            print("Hey Mick... just don't ask what happened to our last drummer.")
        else:
            print("I guess no one is being hired today.")
            
    def fired(self):
        member = str(input("Who do you want to fire: Bassist, Guitarist, or Drummer? "))
        if member == "Bassist":
            print("Sorry, take a hike, Derek!")
        elif member == "Guitarist":
            print("Sorry, take a hike, David!")
        elif member == "Drummer":
            Drummer().combust()
        else:
            print("I guess no one is being fired today.")
    
    def play(Musician):
        Drummer().count()
        Bassist().solo(6)
        Guitarist().solo(9)
        Drummer().solo(3)
        
if __name__ == "__main__":
    spinaltap = Band()
    spinaltap.play()
    spinaltap.hired()
    spinaltap.fired()

