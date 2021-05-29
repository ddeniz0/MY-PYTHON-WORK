a=float(input("enter your weight"))
b=float(input("enter your height"))

index=float
index=a/b

print("body mass index:",index)

if index > 30:
    print("obese")
elif index > 25:
    print ("overweight")
elif index > 18.50:
    print("normal")
else:
    print("low weight")