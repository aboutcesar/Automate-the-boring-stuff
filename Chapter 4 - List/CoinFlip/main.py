import random

numberStreaks = 0
streak = 0
streakfound = []

for experimentNumber in range(10000):
    #code that creates a list of 100 heads or 100 tail values
    for i in range(100):
        streakfound.append(random.randint(0,1))
    #Code that checks if there is a streak of 6+ tail or head values

    for i in range(len(streakfound)):
        if i == 0:
            pass
        elif streakfound[i] == streakfound[i-1]:
            streak+=1
        else:
            streak = 0
        if streak == 6:
            numberStreaks+=1
            streak = 0

    streakfound = []

print("chance if streak: %s%%" % (numberStreaks/(100)))

