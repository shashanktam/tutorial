orders = {}
print("To enter a new order, type yes else no:") 
response = input()                                  # Taking user response
while(response.lower() == "yes"):
    print("Enter your user-ID:")
    id = input()
    if id not in orders:                            # If user-ID is new, create an entry
        orders[id] = []
    print("Enter the book you want:")               # else ask for the order
    book = input()
    orders[id].append(book)                         # add the book to the user's order list
    print("To enter a new order, type yes else no:")
    response = input()                              # Taking user response again
if response.lower() == "no":
    print("Exiting order entry.")                   # checking for valid response
else:
    print("Invalid response")