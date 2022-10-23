# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
namelower1= name1.lower()
namelower2= name2.lower()
name3= namelower1+namelower2
t1=name3.count('t')
t2=name3.count('r')
t3=name3.count('u')
t4=name3.count('e')
total1=str(t1+t2+t3+t4)
l1=name3.count('l')
l2=name3.count('o')
l3=name3.count('v')
l4=name3.count('e')
total2=str(l1+l2+l3+l4)
total=int(total1+total2)
if total>90 or total<10:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>40 and total<50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")