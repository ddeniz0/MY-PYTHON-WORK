islem = input("select the mathematical operation: (+ - / *) : ")

if islem == "+":
    print("addition")
    t1 = int(input("enter the first number: "))
    t2 = int(input("enter the second number: "))
    tr = int
    tr = t1 + t2
    print("result: ",tr)
elif islem == "-":
    print("subtraction ")
    s1 = int(input("enter the first number: "))
    s2 = int(input("enter the second number: "))
    sr = int
    sr = s1 - s2
    print("result: ",sr)
elif islem == "/":
    print("division")
    d1 = float(input("enter the first number: "))
    d2 = float(input("enter the second number: "))
    dr = float
    dr = d1 / d2
    print("result: ",dr)
elif islem == "*":
    print("multiplication")
    m1 = int(input("enter the first number: "))
    m2 = int(input("enter the second number: "))
    mr = int
    mr = m1 * m2
    print("result: ",mr)
else:
    print("wrong keying")