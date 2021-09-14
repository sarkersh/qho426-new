import random
print("Please enter the minimum value:")
min_value = int(input())
print("Please enter the maximum value:")
max_value = int(input())
random_number = random.randrange(min_value, max_value)
print("I am thinking of a number between {} and {}.".format(min_value, max_value))
print(random_number)
print("Can you guess what it is?")
guess = 0
while(guess != random_number):
  print("Please enter a number:")
  guess = int(input())
  if (guess == random_number):
      print("Congratulations!")
      break
  elif (guess < random_number):
      print("Guess higher")
  else:
      print("Guess lower")

print("Game over!")