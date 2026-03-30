def login(username, password):

    if username == "employee" and password == "1234":
        print("Login Successful")
        return True

    print("Invalid Credentials")

    print("Authentication UI Loaded")
    return False