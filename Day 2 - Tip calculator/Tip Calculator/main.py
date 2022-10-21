#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to tip calculator')
bill1 = input("What was the total bill? $")
percent1 = input("What percentage tip would you like to give? 10,12,15? ")
split1 = input("How many people are there to split your bill? ")

bill2 = float(bill1)
percent2 = float(percent1)
split2 = float(split1)

splitBill1= ((bill2*(1+percent2/100))/split2)
splitBill2=round(splitBill1,2)

print(f"Each person should pay {splitBill2}")