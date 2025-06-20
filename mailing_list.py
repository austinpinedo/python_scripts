##cola

class Person:
    
    def __init__(self, name, address, phone_num):                           #creating super class with attributes
        self.name = name
        self.address = address
        self.phone_num = phone_num
    
class Customer(Person):                                                     #creating subclass
    
    def __init__(self, name, address, phone_num, cust_num, mail_list):      #adding two new attributes
        
        super().__init__(name, address, phone_num)                          #initializing new attributes
        self.cust_num = cust_num
        self.mail_list = mail_list
        
def main():
    name = input('what is your name: ')                                     #getting attributes from user
    address = input('what is your address: ')                               #honestly idk if we were supposed to do this, i was confused
    phone_num = input('what is your phone number: ')
    cust_num = input('what is your customer number: ')
    mail_list = input('do you want to me on our mailing list? y/n ')
    
    mail_list_boolean = mail_list.lower() == "y"                            #if they answer y it returns true, else false

    
    customer1 = Customer(name, address, phone_num, cust_num, mail_list)     #this is customer 1 with all attributes being passed to Customer class
    print("Customer Info:")
    print("-"*50)
    print(f'Customer Name: {name}')
    print(f'Address: {address}')
    print(f'Phone Number: {phone_num}')
    print(f'Customer Number: {cust_num}')
    print(f'Mail List: {mail_list_boolean}')
    print(isinstance(customer1, Customer))                                  #using isinstance to get back boolean
    
        

if __name__ == "__main__":
    main()
    


    
    