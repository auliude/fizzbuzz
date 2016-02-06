import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv[1:])))

if len(sys.argv) >= 2:
    for arg in sys.argv[1:]:
        
        n = int(arg)
        print ("Fizz buzz counting up to " +str(n))
    
        for n in range (1, n+1):
            if n % 3 == 0:
                print ("fizz")
            elif n % 5 == 0:
                print ("buzz")
            else:
                print (n)
            
else:
    n = input ("Enter the number you'd like to count up to!")
    n = int(n)

    print ("Fizz buzz counting up to " + str(n))

    for n in range (1, n+1):
        if n % 3 == 0:
            print ("fizz")
        elif n % 5 == 0:
            print ("buzz")
        else: 
            print(n)
    