#Armstrong number
number=int(input("enter a number:"))
length=len(str(number))
armstrong=0
temp=number
while number>0:
    remainder=number%10
    armstrong+=remainder**length
    number//=10
if armstrong==temp:
    print(f"{temp} is a Armstrong number.")
else:
    print(f"{temp} is not a Armstrong number.")