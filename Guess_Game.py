# how to generate random numbers in python -> by using random module
# print(random.randint(1,100))
# jo number generate hoga wo 1 se 100 ke bich hoga 1 and 100 bhi ho skta hai
# flow 
# jackpot ek random number hai jo generate hoga
# guess wo number hai jo user guess krega
# now 2 scenario hai ek to user ka guess kia hua number chhota ho skta hai ya bada
# agr bada hai to guess lower and agr chhota hai to guess higher
# we will use while loop because we dont know how many attempts user will take 

import random
jackpot = random.randint(1,100)
guess = int (input("Chal guess kr"))
counter = 1
while guess != jackpot:

    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
# dobara number maangoge if the guess is wrong hence 
    guess = int (input("Chal guess kr"))
    counter+=1

print("Sahi Jawab")
print("You took",counter,"attempts")



