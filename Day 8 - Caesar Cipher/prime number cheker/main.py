#Write your code below this line 👇
def prime_checker(number):
    prime_number=False
    i=2
    while not prime_number:
        if number%i==0:
            if i!=number:
                print("It's not a prime number.")
                prime_number=True
            else:
                print("It's a prime number.")
                prime_number=True
        i+=1

        
  
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



