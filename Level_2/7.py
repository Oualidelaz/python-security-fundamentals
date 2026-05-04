attempts = 0
max_attempts = 7

print("Guess a number between 0-100")
print("You Have 7 attempts")
while (attempts < max_attempts):
    user_number = int(input("Guess a number between 0-100: "))
    if user_number > 69:
        print("High ...")
    elif user_number < 69:
        print("Low ...")
    elif user_number == 69:
        break
    attempts += 1


if user_number == 69:
    print("Success, The correct number is: 69")
else:
    print("Error: 7 failed attempts!")