import random 

user_number = int(input('Enter your number: '))

number = random.randint(0, 11)

count = 0

while user_number != number:
    
    if user_number > number:
        print("Wrong! Your number is greater.")
    elif user_number < number:
        print("Wrong! Your number is less.")

    user_number = int(input('Enter your number again: '))
    count += 1

print(f'Correct! Your attempts: {count}')