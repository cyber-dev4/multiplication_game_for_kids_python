print ("Welcome to the game of multiplying numbers !")
print ("-"*75)

from random import randint
a = randint (1, 10)

from random import randint
b = randint (1, 10)

result = a * b

solution = int(input(str(a) + "x" + str(b) + "=")) 

print ("-"*75)

if solution == result:
    print ("Correct answer!")
elif solution != result:
    print ("Incorrectly. The correct answer is: ", result)
