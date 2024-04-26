# Sensor Data Management App (V0)
# Omer Furkan Coban
# SoSe 24

# Printing welcome message
print("Welcome to the Sensor Data Management App (V0)!")
print("Please enter ...")

# We are getting inputs from user such as name of the sensor, unit and time step.
sensor_name=str(input("The name of the sensor:"))
unit= str(input("The unit of the sensor's measurements:"))
time_step = int(input("The time step of the mesurement (in minutes):"))

# We are calculating here the time span between measurement

day= time_step//(24*60)
hour = (time_step % (24*60))//60
minute = time_step % 60

print(f"The time span between measurements is {day} days {hour} hours {minute} minutes.")

print("Please enter ...")

# We are getting inputs from user such as name of the date, time and measured value.

year=int(input("The year of the measurement:"))
month=int(input("The month (as int) of the measurement:"))
day=int(input("The day of the measurement:"))
hour=int(input("The hour of the measurement:"))
minutes=int(input("The minute of the measurement:"))
measurement=float(input ("The measured value (float):"))

print(f"Sensor '{sensor_name}' measured {measurement} {unit} on {day}.{month}.{year} at {hour}:{minutes}.")