Money = 100
total = 0
for i in range(5):
    if Money < 50:
        continue
    else:
        total += Money
    
print(total)