correct_pass = "password"
user_pass = None
while user_pass != correct_pass:
    user_pass = input("Enter a password: ")
if user_pass == correct_pass:
    print(f"Success, The password is: '{correct_pass}'")