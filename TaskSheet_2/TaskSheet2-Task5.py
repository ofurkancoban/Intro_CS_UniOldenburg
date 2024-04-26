# Coding unsigned integers with an arbitrary base
# Omer Furkan Coban
# SoSe 24

new_base = int(input("Pleasenter a positive int number as new base (>=2): "))
while new_base < 2:
    print("Numbers can't be represented by a base <=1: ")
    new_base = int(input("Try again: Enter a positive int number >=2: "))

n = int(input("Enter a positive int number: "))
while n < 0:
    print("I can't convert negative numbers")
    n = int(input("Try again: Enter a positive int number: "))

if n == 0:
    result = "0"
else:
    result = ""
    while n > 0:
        digit = n % new_base  # new digit
        if digit < 10:  # convert into feasible digits of new_base
            digitChar = str(digit)  # 0..9: change in String '0',..,'9'
        else:
            digitChar = chr(ord('A') + digit - 10)  # chr(Unicode number of the correct letter)

        print(f"Next digit: {digitChar}")  # print digits
        n = n // new_base  # Continue with n // new_base in the next iteration

        result = result + digitChar # print the result

print(f"Result: {result}")
