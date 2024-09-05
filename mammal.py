class Mammal:
    def __init__(self, name, type, sound):
        self.name = name 
        self.type = type
        self.sound = sound
        
    def make_sound(self):
        return "Monkey makes Chatter"
        
    def get_kingdom(self):
        return "animals"
        
    def info(self):
        return "Monkey is of Wild Monkey"

mammal = Mammal("Monkey", "Wild Monkey", "Chatter")
print(mammal.make_sound()) 
print(mammal.get_kingdom())
print(mammal.info())      