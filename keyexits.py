l={'a':"Daniel",'b':"Dhiraj",'c':"Yash",'d':"Amar"}
print("Initial Dictionary",l)
d=input("Enter key to be deleted:")
if(d in l):
      del l[d]
      print("Element deleted succesfully")
      print(l)
else:
	print("Element not found")	
