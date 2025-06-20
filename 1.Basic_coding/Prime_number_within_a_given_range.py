#Prime number within a given range
starting=int(input("enter starting number:"))
ending=int(input("enter ending number:"))
for i in range(starting,ending+1):
    flag=0
    if i<2:
        flag=1
    for j in range(2,i):
	    if i%j==0:
	        flag=1
	        break
    if flag==0:
       print(i)