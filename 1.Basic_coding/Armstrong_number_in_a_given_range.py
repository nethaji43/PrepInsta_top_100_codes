#Armstrong number in a given range
starting=int(input("enter starting number:"))
ending=int(input("enter ending number:"))
for i in range(starting,ending+1):
   length=len(str(i))
   armstrong=0
   temp=i
   while i>0:
       remainder=i%10
       armstrong+=remainder**length
       i//=10
   if armstrong==temp:
       print(temp)
