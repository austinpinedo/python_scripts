'''
Driver for our Animals program
'''
import animals_module
import inspect

def menu():
    #here we need to ask the user for the values of the Animal object, to determine if it is a cat, a dog, or a human.  Depending on which one returns true, we will create an object of that class, which will inherit the attributes of the supercalss - Animals.
    is_alive = input('is the object alive? ')
    has_skin = input('does it have skin? ')
    is_aware = input('is it aware? ')
    can_vocalize = input('can it vocalize? ')
    
    is_animal = False
    
    if is_alive.lower() == 'yes' and has_skin.lower() == 'yes' and is_aware.lower() == 'yes' and can_vocalize.lower() == 'yes':
        is_animal = True 
        
    if is_animal == True:
        
        is_upright = input('is animal upright? ')
        if is_upright.lower() == 'yes':
            my_human = animals_module.Human()
            
        
        #animal_epidermis = input('what type of epidermis does the animal have? ')
        
        #my_animal = animals_module.Animals(animal_epidermis, has_skin, is_aware, can_vocalize)
        
        #for i in inspect.getmembers(my_animal):
        #    print(i)
        
    
if __name__ == "__main__":
    menu()







