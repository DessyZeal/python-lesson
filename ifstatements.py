# writing an if statement thhat when a person is above 18 show adult
# first create a variable age
age = 32
print("Your age is:", age)
# if statements
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# now lets make a dice game
import random
# generate a random number between 1 and 6
dice = random.randint(1, 6)
print ("You rolled a", dice)
if dice == 6:
    print('You got 6 🎉')
    else:
    print('You did not get 6 😞')