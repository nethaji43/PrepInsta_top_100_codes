#Reverse of a number
number=int(input("enter a number:"))
reverse=0
temp=number
while number>0:
   remainder=number%10
   reverse=(reverse*10)+remainder
   number//=10
print(f"reverse of {temp} is {reverse}")