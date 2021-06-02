number = input("enter the number:")
number_digits = len(number)
number = int(number)
digit = 0
total = 0

temporary_number = number

while (temporary_number > 0):
    digit = temporary_number % 10

    total += digit ** number_digits

    temporary_number //= 10

if (total == number):
    print(number, "number is a Armstrong ")
else:
    print(number, "number is not a Armstrong")
