##text file reader/dictionary





def file_string():
    dictionary = {}
    with open("Word Frequency.txt","r") as file:
        for line in file:                                           #iterating through the lines
            words = line.strip().split()                            #stripping and splitting lines
            for word in words:                                      #iterating through words
                word = word.lower()                                 #forcing all to lower
                if word in dictionary:                              
                    dictionary[word] += 1                           #if word in dictionary then count increases
                else:
                    dictionary[word] = 1                            #if not in dictionary then it adds it
    return dictionary
    
        

def display_word_count(words):                                      #receiving words parameter
    print(f"{'Word:':<30} {'Count:'}")                              #page 107 thank you Safria
    print('-'*60)                                                   
    for word, count in sorted(words.items()):                       #using key,value for a sorted dictionary of the words and returns tuples
        print(f"{word:<30}{count}")          
    
        
def main():
    words = file_string()
    display_word_count(words)
    
    
main()


