# Code an unsigned value in binary representation
# Omer Furkan Coban
# SoSe 24

new_base = 2
n = int(input("Please enter a positive int number: "))
n_original = n # save the value in another variable, as n will be modified in the loop
while n < 0 :
    print("Try again! You entered a negative number.")
    n = int(input("Try again: Enter a positive int number: "))

if n == 0:
    result = "0"
else:
    result = ""
    while n > 0:
        digit = n % new_base # new digit
        print(f"Next digit: {digit}") # printing digit by digit
        n = n // new_base  # Continue with n = n div 2 in the next iteration
        result = str(digit) + result

print(f"The representation of {n_original} in base {new_base} is: {result}.")