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
    towers = {"A": copy.copy(solved_tower), "B": [], "C": []}
    

    display_Tower(towers)
    fromTower, toTower = getPlayerMove()

    #change
    diskleaving = towers[fromtower].pop()
    towers[totower].append(diskleaving)
    #Check if won
    gameOver(towers)

#Display Tower
def display_Tower(towers):
    for levels in range(total_disks, -1, -1):
        for tower in (towers["A"],towers["B"],towers["c"]):
            if level >= len(towers):
                print(0)
            else:
                print(tower[level])

    #display the colums
    emptySpace = " " * total_disks
    print(" {0} A{0}{0} B{0}{0} C\n".format(emptyspace))

#get the player move
def getPlayerMove(towers):
    while True:
        print("please enter the tower letters to move the from and to")
        print("eg. from tower A to tower B --> AB\n")

        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing")
            sys.exit()

        if reponse not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("That is not a valid Selection, Enter (AB, AC, BA, BC, CA, CB)" )
            continue
        fromtower, totower = response[0],response[1]
        elif len(tower[fromtower]) == 0:
            print("Tower empty, please pick a start tower that has disks")
            continue

        elif tower[totower][-1] > tower[fromtower][-1]:
            print("You cannot place a bigger disk on top of a biigger disk.")
            print("Try again")
            continue

        elif len(tower[totower]) == 0:
            return fromtower, totower
        

#Check if won
def gameOver(towers):
    if solved_tower in towers:
        print("you won")
        print("congrats")
        sys.exit()
