import random
length = int(input("enter the length of password:"))
list = ["a","b","c","d","e","f","g","h","i","j","k","l","1","2","3","4","5","6","7","8","9","0","!","@","$","%","^","&","#"]
password = "".join(random.sample(list, length))
print(password)