import copy

def numOfIslands(arr):
    """Returns the number of islands in a given 2d Array"""
    #remember to guard against nulls
    if(not arr or len(arr[0]) is 0):
        return 0
    temp = copy.deepcopy(arr)
    for x in xrange(len(temp)):
        for y in xrange(x):
            if (temp[x][y] is not 0):
                count = count + 1
                bfs(temp,x,y)

def bfs(tempArr, x, y):
    """Performs a breadth first search and marks 1's as seen by changing their value to 0"""
    stack = [[x,y]]
    while (not stack):
        i, j = stack.pop(0)
        tempArr[i,j] = 0
        stack.append(findOneAround(tempArr,i,j))



def findOneAround(tempArr,x,y):
    """Returns a list of lists that each contain x,y coordinates of where the value is 1"""
    xLimit = len(tempArr)
    yLimit = len(tempArr[0])
    #ehhh needs help lol
    listComp = [ [[i,j] if i >= 0 and i < xLimit j>= 0 and j < yLimit
                    for i in xrange(x-1,x)]
                        for j in xrange(y-1,y)]



    return listComp

    # output=[]
    # if(x-1 >= 0 and x+1 < len(tempArr)):
    #     if (y-1 >= 0) and x+1 < len(tempArr):
    #         for i in xrange(3):
    #             for j in xrange(3):
    #                 currX = x-1 + i
    #                 currY = y-1 + j
    #                 if (tempArr[currX][currY] is 1):
    #                     output.append([i,j])
    #         if(tempArr[x][y+1])
