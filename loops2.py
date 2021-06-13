number = int(input("number:"))

i = 1
total = 0

while(i<number):
    if (number % i == 0):
        total = total + i
    i = i + 1

if (total == number):
    print("number is a perfect number:", number)
else:
    print("number is not a perfect number:", number)




