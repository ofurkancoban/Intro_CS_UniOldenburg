# Converting a number into date and time
# Omer Furkan Coban
# SoSe 24

# We get the a number as an integer
number_minutes = int(input("Enter a number: "))

# We added an if-else condition to ensure that the entered number is greater than 0. If the entered number is less than or equal to 0, the program will not run and a warning will be printed stating that a number greater than 0 must be entered.
if number_minutes <= 0:
    print("Please enter a number greater than 0.")
else:
    # We converted minutes into hours, days, months, and years.
    hours = number_minutes // 60
    days = hours // 24
    months = days // 30
    years = months // 12

    # We calculated the remaining months, days, hours, and minutes
    remaining_months = months % 12
    remaining_days = days % 30
    remaining_hours = hours % 24
    remaining_minutes = number_minutes % 60

    # Print the result
    print(f"Result: {number_minutes} minutes = {years} years, {remaining_months} months, {remaining_days} days, {remaining_hours} hours, and {remaining_minutes} minutes.")