import random
while True:
    temp= int(input("Press 1 to roll the dice or others to exit:\n"))
    if temp == 1:
        print(random.randint(1, 6))
    else:
        break
