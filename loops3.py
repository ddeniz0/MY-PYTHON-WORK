total = 0

while True:

    number = input("number :")

    if (number == "q"):
        break
    number = int(number)

    total = total + number

print("sum of entered numbers:", total)