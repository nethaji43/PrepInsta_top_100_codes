#sum of first n natural numbers
number=int(input("enter a number"))
total=0
for i in range(0,number):
     total+=i
print(f"{total} is sum of {number}")