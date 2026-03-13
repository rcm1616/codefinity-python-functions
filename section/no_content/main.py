users_db = []

def register_user(username, email, age):
    if age < 18:
        message = "Registration failed: age must be 18 or older."
    else:
        user = {"username": username, "email": email, "age": age}
        users_db.append(user)
        message =  f"User {username} registered successfully!"
    return message

# Pass the parameters in any way to register a user
result1 = register_user("Peter", "peter@mail.com", 20)

# Testing the result
print(result1)
print(users_db)  # List of registered users
