def wish():
    print("Thank You")
# double nd
print("Welcome User")
i=int(input("Starting number "))
e=int(input("Ending number "))
e=e+1
steps=int(input("Steps between two consecutive nos. "))
z=input("Do you want any no. to not display(Yes or No)\n")
s=z[:3]
ns=s.upper()
p=z[:2]
np=p.upper()
if (ns=="YES"):
  nd=int(input("No. not be undisplayed "))
  if (i<= nd < e):
    for j in range(i,e,steps):
      if j==nd:
        continue
      print(j,",",end="")  
  else:
        print("Enter Number within the given range")
elif (p=="NO"):
  nd=""
  for j in range(i,e,steps):
    print(j,",",end="")  
print("\n")
wish()
