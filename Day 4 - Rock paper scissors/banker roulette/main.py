
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# random.shuffle(names)
# print(names[0]+" is going to buy the meal today!")

lenth= len(names)
choice= random.randint(0,lenth-1)
print(names[choice]+ " is going to buy the meal today!")
