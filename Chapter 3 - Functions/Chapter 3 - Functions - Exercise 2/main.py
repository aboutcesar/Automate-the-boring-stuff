#Collatz Sequence

def collatz(number):
    while number > 1:

        if number % 2 == 0:
            number = number //2
            print(number)
        else:
            number = number * 3 + 1
            print(number)


userInput = input("Enter a number: ")

try:
    int(userInput)
except:
    print("Error: Enter a valid number")

collatz(int(userInput))