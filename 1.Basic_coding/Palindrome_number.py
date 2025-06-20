#Palindrome number
number=int(input("enter a number"))
reverse=0
temp=number
while number>0:
   remainder=number%10
   reverse=remainder+(reverse*10)
   number//=10
if (temp==reverse):
   print(f"{temp} is a palindrome.")
else:
   print(f"{temp} is not a palindrome.")