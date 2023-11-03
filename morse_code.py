#morse code converter

#these are both lists with correct indexing
morse = ['/','--..--','.-.-.-','..--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.-','--..']
alphanum = [' ',',','.','?','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#main function to get string and send each char to get_morse_code
def get_string():
    string = input('what would you like to convert to morse code? ')  
    morse_code = ''                                                   #empte string to put this in 
    for char in string.lower():                                       #forcing string to lower
        morse_char = get_morse_code(char)                             #putting char from get_morse_code into variable
        morse_code += morse_char + ' '                                #adding morse_char to empty string and seperating by a space
    print(morse_code)
#converting char to morse char
def get_morse_code(char):               
    if char in alphanum:
        index = alphanum.index(char)                                  #finding index of char in alphanum list
        return morse[index]                                           #returning morse char with the index of where the char was at 

def main():
    get_string()

if __name__ == "__main__":
    main()






##checking to see lengths of both lists match
#nummorse = len(morse)
#numalpha = len(alphanum)
#print(nummorse)
#print(numalpha)