class Animal ():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def what_type (self, animal_type):
        self.animal_type = animal_type
        return self.animal_type
    
def run_animal(animal_name, animal_color):
    one_animal = Animal(animal_name, animal_color)
    return one_animal

bullmastiff = run_animal("Roscoe", "fawn")
orpington = run_animal("Buster", "buff")
print(bullmastiff, orpington)

bullmastiff.what_type("dog")
orpington.what_type("chicken")

print(bullmastiff.animal_type)
print(orpington.animal_type)