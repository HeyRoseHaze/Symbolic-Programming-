import datetime

name = input("Enter your name: \n")
year_of_birth = int(input("Enter your year of birth: "))

time = datetime.datetime.now()
current_year = time.year 

age = current_year - year_of_birth

print(f"{name.title()}, you are {age} years old.")

