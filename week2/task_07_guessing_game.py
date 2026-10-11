import random
random = random.randint(1, 10)
i = 1
while i < 6:
  value = int(input("Guess the number from 1 - 10"))
  if random == value:
    print(f"Congratulations! You guessed the number in {i} attempts.")
    break
  else:
    print("Game over")
  i +=1