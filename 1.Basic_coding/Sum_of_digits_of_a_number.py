#Sum of digits of a number
number=int(input("enter a number:"))
total=0
temp=number
while number>0:
   remainder=number%10
   total+=remainder
   number//=10
print(f"sum of {temp} is {total}")