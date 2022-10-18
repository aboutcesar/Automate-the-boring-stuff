# simple lists being printed

def commaCode(list):

    if len(list) == 1:
        return list[0]

    print( '{}, and {}'.format(', '.join(list[:-1]), list[-1]))

spam = ["egg", "rice", "tree"]

userList = []
while True:
    print("Enter item " + str(len(userList)) + " to the list: (Or enter to stop)")
    spam = input()

    if spam == "":
        break

    userList.append(spam) #list


print("The items are" )


commaCode(userList)