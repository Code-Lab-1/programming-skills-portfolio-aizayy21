#they won’t arrive in time for the dinner, 
#you have space for only two guests.
guests = ["Erina","Elvina","Ruby","Sofia"]
#Erina isn't coming.
name = guests[0].title()
print("\nSorry, " + name + " I can't invite you to dinner.")
#Elvina isn't coming.
name = guests[1].title()

guests.pop(1)
print("\nSorry, " + name + " I can't invite you to dinner")

del(guests[1])
guests.insert(1, 'Mary'+' Can you come?')

# insert other guest who's coming

name = guests[1].title()
print(name + " is coming to dinner.")

name = guests[2].title()
print(name + " is coming to dinner.")