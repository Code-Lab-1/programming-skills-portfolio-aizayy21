X = "\nWhat topping you like on your pizza?"
Y= "\nEnter 'quit':"

while True:
    topping = input(X)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        StopIteration