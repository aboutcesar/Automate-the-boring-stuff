tableData = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]


def printPicnic(items):
    colWidths = [0] * len(items)

    for line in items:
        # find max word
        max = 0
        for word in line:
            if len(word) > max:
                max = len(word)
        colWidths[items.index(line)] = max

    print(colWidths)

    #print with center
    print('Picnic Items'.center(colWidths.index(max)))
    for x in range(len(items[0])):
        for y in range(len(items)):
            print(items[y][x].center(colWidths[y]), end=" ")
        print('')


printPicnic(tableData)