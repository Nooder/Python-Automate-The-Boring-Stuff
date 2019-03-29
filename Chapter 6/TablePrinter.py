tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongestMemberColumn(table, col):
    longest = 0
    for i in table:
        if len(i[col]) > longest:
            longest = len(i[col])
    return longest

def findLongestMember2d(table):
    longest = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if len(table[i][j]) > longest:
                longest = len(table[i][j])
    return longest

def printTable(table):
    for i in range(len(table[0])):
        longest = findLongestMember2d(table)
        for j in range(len(table)):
            print(table[j][i].rjust(longest), end="")
        print("")
printTable(tableData)
#print(findLongestMemberColumn(tableData, 4))