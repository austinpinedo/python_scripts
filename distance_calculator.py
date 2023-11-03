#distance calculator

g = 9.8
t = int(input("how many seconds would you like to input? "))

#defining distance function
def distance(t):
    d = 0.5 * g * t**2  #distance function
    return(d)           #returning variable

for i in range(1, t+1):  #numbering every second in chosed range
    d = distance(i)      #getting distance output in meters
    print(f"for {i} seconds, it is {d} meters")
    