import random
num = random.randint(1,10)
for i in range(0,3):
    guess = int(input("guess a number between 1 and 10,you have 3 chance:"))
    if guess > num:
        print("guess smaller")
    elif guess < num:
        print("guess bigger")
    elif guess == num:
        print("Bingle,you win!")
        break
else:
    print("Sorry,the number is",num)

