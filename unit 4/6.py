class Animal:
    def speak(self):
        return"Anima sound"
    
class dog:
    def speak(self):
        return"woo"
    
class cat:
    def speak(self):
        return"meow"
    
def make_animal_speak(animal_object):
    print(animal_object.speak())
    
make_animal_speak(dog())
make_animal_speak(cat())