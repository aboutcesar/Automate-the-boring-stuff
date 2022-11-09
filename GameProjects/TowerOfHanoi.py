#! Tower of Hanoi Program
import copy, sys

total_disks = 5

solved_tower = list(range(total_disks, 0, -1))

#main
def main():
    print("welcome to the tower of Hanoi")
    print("""
                Move the tower of disks, one disk at a time, to another tower.
                Larger disks cannot rest on top of smaller disks.
More info at: 
                """)


    display_Tower(towers)

    fromTower, toTower = getPlayerMove()
    

#Display Tower
def display_Tower(towers):
    for levels in range(total_disks, -1, -1):
        for tower in (towers["A"],towers["B"],towers["c"]):
            if level >= len(towers):
                print(0)
            else:
                print(tower[level])

    print()

    #display the colums
    emptySpace = " " * total_disks
    print(" {0} A{0}{0} B{0}{0} C\n".format(emptyspace))

#get the player move
def getPlayerMove():
    while True:
        print("please enter the tower letters to move the from and to")
        print("eg. from tower A to tower B --> AB\n")

        response = input().upper().strip()

        if response == "QUIT":
            print("Thanks for playing")
            sys.exit()

        if reponse not in ("AB", "AC", "BA", "

        
#Check if valid Move
def isvalidmove():
    pass

#Change the board


#Check if won
def gameOver():
    pass
