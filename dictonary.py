m={"a":100,"b":200,"c":300,"d":400}
print(m)

n=input("enter the key which you want to delete :")
if n in m:
      del m[n]
else:
    print("key not found")

print(m)
