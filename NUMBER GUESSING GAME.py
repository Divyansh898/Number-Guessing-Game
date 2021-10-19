#NUMBER GUESSING GAME

import random
import math
lower = int(input("Enter Lower bound: "))

upper = int(input("Enter Upper bound: "))
x = random.randint(lower, upper)

print("\nYou have only ",

 round(math.log(upper - lower + 1, 2)),

 " chances to guess the number!\n")

count = 0

while count < math.log(upper - lower + 1, 2):

 count += 1 
 no = int(input("Guess a number:- ")) 
 
 if x == no:

  print("Congratulations you did it in ",

   count, " try")

 

  break

 elif x > no:

  print("You guessed too small!")

 elif x < no:

  print("You Guessed too high!")
  if count >= math.log(upper - lower + 1, 2):

   print("\nThe number is %d" % x)

 print("\tBetter Luck Next time!")