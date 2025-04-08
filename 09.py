number=int(input("place the number here: "))

if number%3==0 and number%5==0:
    print("the number is divisible by either")
elif number%3==0:
    print("the number is divisible by 3")
elif number%5==0:
    print("the number is divisible by 5")
else:
    print("number not divisible by either ")
    
