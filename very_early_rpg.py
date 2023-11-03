##modest RPG

class PlayerCharacter:
    
    def __init__(self, health, armor_rating, attack_power):         #initiating everything and assigning it health armor and attack 
        self.set_health(health)                                     #this shows where parameters go in the setters
        self.set_armor_rating(armor_rating)
        self.set_attack_power(attack_power)
        
    def set_health(self, health):                                   #self is needed and health is next 
        while not (1 <= health <= 100):                             #using while not loop to force user to do what i ask
            print("that is not a valid number for health. ")        #i think it looks better with two differnt statements
            health = int(input("enter a number 1-100: "))           #get out of loop by following instructions
        self.health = health                                        #seetting health so all instances of health are userinput
#        if 1 <= health <= 100:
#            self.health = health
#        else:
#            print("that is not within 1-100. ")
#            self.health = int(input("please enter a number 1-100: "))
            
    def set_armor_rating(self, armor_rating):                       #this is a repeat of set_health
        while not (1<= armor_rating <= 20):
            print("that is not a valid number for armor.")
            armor_rating = int(input("enter a number 1-20: "))
        self.armor_rating = armor_rating
#        if 1 <= armor_rating <= 20:
#            self.armor_rating = armor_rating
#        else:
#            print("that is not within 1-20. ")
#            self.armor_rating = int(input("please enter a number 1-20: "))
            
    def set_attack_power(self, attack_power):                       #this is also a repeat of set_health
        while not (1 <= attack_power <= 20):
            print("that is not a valid number for attack power.")
            attack_power = int(input("enter a number 1-20: "))
        self.attack_power = attack_power
#        if 1 <= attack_power <=20:
#            self.attack_power = attack_power
#        else:
#            print("that is not within 1-20. ")
#            self.attack_power = int(input("please enter a number 1-20: "))
            
    def get_health(self):                                           #using getters to get attributes
        return self.health
    
    def get_armor_rating(self):                                     #same as get_health
        return self.armor_rating
    
    def get_attack_power(self):                                     #same as get_health
        return self.attack_power

def main():
    health = int(input("what would you like your wizard's health to be? (1-100) "))             #asking users to input stats for wizard
    armor_rating = int(input("what would you like your wizard's armor rating to be? (1-20) "))
    attack_power = int(input("what would you like your wizard's attack power to be? (1-20) "))
    
    wizard = PlayerCharacter(health, armor_rating, attack_power)    #creating wizard object with this class
    
    print("your wizards attributes are: ")
    print("-"*50)
    print("health:", wizard.get_health())                           #using getters to display attributes
    print("armor:", wizard.get_armor_rating())
    print("attack power:", wizard.get_attack_power())
    
main()