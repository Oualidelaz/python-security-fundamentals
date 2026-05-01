attempts = 0
max_attempts = 3
while (attempts < max_attempts):
    user_pass = input("Enter password: ")
    if user_pass != "password":
        attempts += 1
    else:
        print("Success: Correct password!")
        break
if attempts == 3:
    print("Error: 3 failed attempts!")
