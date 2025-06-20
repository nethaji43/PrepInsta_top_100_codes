#Sum of numbers in a given range.
starting=int(input("enter starting number"))
ending=int(input("enter ending number"))
total=0
for i in range(starting,ending):
     total+=i
print(f"{total} is sum of {starting},{ending}")