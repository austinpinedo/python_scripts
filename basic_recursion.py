#recursion

def recur(n):                           #recur accepts param
    if n == 1:                          #setting my basecase
        return 1
    else:                               #basecase not met so it calls recur again with n-1 
        return recur(n - 1) + n         #keeps recuring until ==1 and then adds all with +n
    
def main():
    num = int(input('what num would you like to use? (0-100) '))
    while num < 0 or num > 100:                                     #while loop to force u into 0-100
        num = int(input('that is not between 0-100. please retry: '))
    result = recur(num)
    print(result)

if __name__ == '__main__':
    main()