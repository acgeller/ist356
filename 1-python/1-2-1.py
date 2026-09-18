PASSWORD = "secret"
MAX_ATTEMPTS = 5
success = False
for attempts in range(MAX_ATTEMPTS):
    your_password = input("Enter the password: ")
    if your_password == PASSWORD:
        print("Access granted")
        success = True
        break
    else:
        print("Access denied")

    print(f"Attempt {attempts + 1} of {MAX_ATTEMPTS}")
        
if not success:
    print("Too many failed attempts.")