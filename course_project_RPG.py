##course project RPG

import random

class Humanoid():           #super class with all base attributes
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height            #assigning the attributes from characterCreation
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        

class Humans(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.stats()        
        self.bonus()
    
    def stats(self):        #this shows stats from when you first create a human before you pick an attribute to add +2
        print("\nyour character stats: ")
        print("-"*50)
        print(f"{'height:':<20} {self.height}ft")
        print(f"{'weight:':<20} {self.weight}lbs")
        print(f"{'hair color:':<20} {self.hair_color}")
        print(f"{'eye color:':<20} {self.eye_color}")
        print(f"{'strength:':<20} {self.strength}")
        print(f"{'dexterity:':<20} {self.dexterity}")
        print(f"{'constitution:':<20} {self.constitution}")
        print(f"{'intelligence:':<20} {self.intelligence}")
        print(f"{'wisdom:':<20} {self.wisdom}")
        print(f"{'charisma:':<20} {self.charisma}")
        
    def bonus(self):        #this lets user choose what to add to 
        user_choice = input('what attribute would you want to add +2? (strength, dexterity, constitution, intelligence, wisdom, charisma) ')
        if user_choice.lower() in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:      #makes choice lower and checks if in list
            setattr(self, user_choice, getattr(self, user_choice) + 2)       #i found this online not the textbook. setattr sets value getattr gets value and ties it to attribute
            
        

class Elves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.dexterity += 2     #elves getting their buffs
        self.charisma += 2

class Dwarves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.strength += 2      #dwarves getting their buffs
        self.constitution += 2
        self.charisma -= 2
        
def characterCreation():
    while True:     #making you choose correct class
        race_choice = input("choose your race (human, elf, dwarf): ")
        if race_choice.lower() in ['human','elf','dwarf']:
            break
        else:
            print("invalid. please choose human, elf, or dwarf. ")

    while True:     #loop to force you to choose good number
        height = int(input("enter your characters height: (3ft-7ft) "))
        if 3 <= height <= 7:
            break
        else:
            print("invalid. please enter a number 3-7. ")
            
    while True:     #loop to force you to choose good number  
        weight = int(input("enter your characters weight: (60lbs-300lbs) "))
        if 60 <= weight <= 300:
            break
        else:
            print("invalid. please enter a number 60-300. ")
            
    hair_color = input("enter a color for your characters hair: (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde) ")  #choosing hair color
    eye_color = input("enter a color for your characters eyes: (white, black, red, green, blue, brown, purple, amber) ")            #choosing eye color
    strength = random.randint(1,18)     #creating a random number to store into different variables as stats 
    dexterity = random.randint(1,18)
    constitution = random.randint(1,18)
    intelligence = random.randint(1,18)
    wisdom = random.randint(1,18)
    charisma = random.randint(1,18)
    
    if race_choice.lower() == 'human':
        character = Humans(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)        #sending choices to proper subclasses
    elif race_choice.lower() == 'elf':
        character = Elves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    elif race_choice.lower() == 'dwarf':
        character = Dwarves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    else:
        race_choice = input('incorrect. please choose human, elf, or dwarf: ')

    print("\nyour final character: ")       #displaying final stats with format f
    print("-"*50)
    print(f"{'race:':<20} {race_choice}")       #making a table from challenge 9
    print(f"{'height:':<20} {character.height}ft")
    print(f"{'weight:':<20} {character.weight}lbs")
    print(f"{'hair color:':<20} {character.hair_color}")
    print(f"{'eye color:':<20} {character.eye_color}")
    print(f"{'strength:':<20} {character.strength}")
    print(f"{'dexterity:':<20} {character.dexterity}")
    print(f"{'constitution:':<20} {character.constitution}")
    print(f"{'intelligence:':<20} {character.intelligence}")
    print(f"{'wisdom:':<20} {character.wisdom}")
    print(f"{'charisma:':<20} {character.charisma}")
    
    if race_choice.lower() == 'elf':        #i think this is what you meant for special ability percentages
        print("special ability: 100% resistance to sleep")
    elif race_choice.lower() == 'dwarf':
        print("special ability: 20% resistance to magic")

if __name__ == "__main__":      #calling characterCreation
    characterCreation()
