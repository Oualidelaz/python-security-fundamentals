credentials = {
    "oualid": 12323424,
    "khalid": 29382342,
    "adil": 3212234,
    "omar": 7823423,
    "othman": 92343231,
    "ahmed": 12301012,
    "hicham": 123211923
}

user = input("Enter username: ")
try:
    if user in credentials.keys():
        result = credentials[user]
        print(f"Password: {result}")
    else:
        print("Unavailable!")
except Exception as e:
    print("Something Wrong!")
