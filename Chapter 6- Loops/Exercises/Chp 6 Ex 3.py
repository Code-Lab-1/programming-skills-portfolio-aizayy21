#a statement for the ride 
#age as a input 
while True:
    age = input("How old are you? ")
    age = int(age)
    if age < 6:
        print("Babies aren't allowed.")
    elif age <= 13:
        print("Okay, But take the parents with you on the ride.") 
    else:
        print("Okay, You are allowed.")