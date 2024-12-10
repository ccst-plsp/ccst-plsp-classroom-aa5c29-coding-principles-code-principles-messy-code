# Messy Code
print("Enter your name:")
name = input()
if len(name) > 20:
    print("Name is too long, must be less than 20 characters.")
else:
    print("Hello, " + name)

print("Enter your email:")
email = input()
if len(email) > 50:
    print("Email is too long, must be less than 50 characters.")
else:
    print("Email saved: " + email)

print("Enter your address:")
address = input()
if len(address) > 100:
    print("Address is too long, must be less than 100 characters.")
else:
    print("Address saved: " + address)
