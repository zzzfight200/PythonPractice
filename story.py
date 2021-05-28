import random
when = ["a few years ago","yesterday","last night","a long time ago","on 20th Jan"]
who = ["a rabbit ","an elephant ","a mouse ","a dog ","a cat "]
name = ["aleen ","peter ","judy ","james ","ali "]
residence = ["barcelona ","india ","germany ","england ","china "]
went = ["cinema ","university ","seminar ","school "]
happend = ["made a lot of friends","eats a burger","found a secret key","solved a mistery","wrote a book"]
print(random.choice(when).capitalize()+","+random.choice(who)+"that lived in "+random.choice(residence).capitalize()+"went to the " +random.choice(went)+"and "+random.choice(happend))
