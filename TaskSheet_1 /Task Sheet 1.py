# Timetracker
# Omer Furkan Coban
# SoSe 24

# Here I get inputs as an integer from user as year, month, day, hour, minutes variables.

year = int(input("Enter the year:"))
month = int(input("Enter the month:"))
day = int(input("Enter the day:"))
hour = int(input("Enter the hour:"))
minutes = int(input("Enter the minutes:"))


# Calculation of minutes

result_minutes = ( ( ( year * 12 + month ) * 30 + day ) * 24 + hour ) * 60 + minutes

print(f"Result: {day}.{month}.{year}  {hour}:{minutes}: It has been {result_minutes} minutes since we began counting.")