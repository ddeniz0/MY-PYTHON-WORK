a= int(input("enter the x number"))
b= int(input("enter the y number"))
c= int(input("enter the z number"))

if a > b and a >c:
    print("the highest digit is the number x")
elif b > a and b > c:
    print("the highest digit is the number y")
elif c > a and c > b:
    print("the highest digit is the number z")
else:
    print("entered numbers are equal")
