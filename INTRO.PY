a = 4
b = 7
c_squared = a**2 + b**2
c = c_squared **(1/2)
print(c)

import math\
    #Given a number, create a program which checks
    #if a number is even or  odd. If number
    #is even, print "Even" else print "Odd"
    #If the number is both divisible by 2 and
    #3 print "EvenOdd"

    #Input: Type a number here 4
    #Output: Even

    #Input: Type a number here: 6
    #Output: EvenOdd

num = int(input("Type a number here: "))
if (num % 2) == 0:
     print(num, "even")
if (num % 3) == 0:
   print(num, "odd")

#Loop in Python
for x in range (10):
    print(x)



i=1
while i <= 100:
    if i%3==0:
        print("Fizz", end="")
        if i%5==0:
            print("Buzz", end="")
    elif i%5==0:
        print("Buzz", end="")
    else:
        print(i, end="")
    print()
    i+=1




