password_is_correct = False
 
while not password_is_correct: 
    attempt = input("Enter password: ") 
    if attempt == "secret123": 
        password_is_correct = True
        print("Access granted!") 
    else: 
        print("Incorrect password. Try again.")