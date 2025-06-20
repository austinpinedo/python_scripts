'''
Animals module
'''
#Superclass Animals
class Animals:
    def __init__(self, epidermis, cognitive, living, vocalize):
        self.__epidermis = epidermis
        self.__cognitive = cognitive
        self.__living = living
        self.__vocalize = vocalize
    #setters & getters
    def set_epidermis(self, epidermis):
        self.__epidermis = epidermis
    def get_epidermis(self):
        return self.__epidermis
    def set_congitive(self, cognitive):
        self.__cognitive = cognitive
    def get_cognitive(self):
        return self.__cognitive
    def set_living(self, living):
        self.__living = living
    def get_living(self):
        return self.__living
    def set_vocalize(self, vocalize):
        self.__vocalize = vocalize
    def get_vocalize(self):
        return self.__vocalize
    #methods (would contain variables, lists, tuples, dictionaries, etc)
    def is_animal():
        #use the values returned from the getters to determine if the object is an animal.  For instance, if living attribute is false, then it's not an animal (yes, it could be dead, but we will ignore that possibility for now).
        
        
class Dog(Animals):
    #this init function overrides the parent init function
    def __init__(self, epidermis, cognitive, living, vocalize, legs, tail):
        #to keep the inheritance of the parent's init function, we need to add a call to it here
        Animals.__init__(self, epidermis, cognitive, living, vocalize)
        #we can also use the super to avoid having to use the name of the parent class, as such:
        #super().__init__(self, epidermis, cognitive, living, vocalize)
        self.__legs = legs
        self.__tail = tail
        #mutator and accessor for legs and tail.  legs would be an int, tail would be boolean T/F
        #we need a method to return True if the Dog has 4 legs, has a tail, and says woof woof
class Cat(Animals):
    #this init function overrides the parent init function
    def __init__(self, epidermis, cognitive, living, vocalize, legs, tail):
        #to keep the inheritance of the parent's init function, we need to add a call to it here
        Animals.__init__(self, epidermis, cognitive, living, vocalize)
        #we can also use the super to avoid having to use the name of the parent class, as such:
        #super().__init__(self, epidermis, cognitive, living, vocalize)
        self.__legs = legs
        self.__tail = tail
        #mutator and accessor for legs and tail.  legs would be an int, tail would be boolean T/F
        #we need a method to return True if the cat has 4 legs, has a tail, and says meow
class Human(Animals):
    #this init function overrides the parent init function
    def __init__(self, epidermis, cognitive, living, vocalize, legs, upright):
        #to keep the inheritance of the parent's init function, we need to add a call to it here
        Animals.__init__(self, epidermis, cognitive, living, vocalize)
        #we can also use the super to avoid having to use the name of the parent class, as such:
        #super().__init__(self, epidermis, cognitive, living, vocalize)
        self.__legs = legs
        self.__upright = upright
        #mutator and accessor for legs and tupright.  legs would be an int, upright would be boolean T/F
        #We need a method to return True if the user input 2 legs and upright is True. This would tell us that the object is a Human
    
        