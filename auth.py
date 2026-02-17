print("--- Welcome to Libris ---")
print("Login ---")
username = input("Enter your username: ")
password = input("Enter your password: ")

while password != "123":
    password = input("Incorrect password. Please try again....")

print("Login successful!")
