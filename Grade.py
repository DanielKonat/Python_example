a=int(input("Enter marks of A:"))
b=int(input("Enter marks of B:"))
c=int(input("Enter marks of C:"))
d=int(input("Enter marks of D:"))
e=int(input("Enter marks of E:"))
avg=a+b+c+d+e/5
print("average",avg)
p=(a+b+c+d+e/5)*100
if((p>=35)&(p<=50)):
	print("C Grade")
elif((p>50)&(p<=70)):
	print("B Grade")
elif(p>70):
	print("A Grade")
else:
	print("Fail")

