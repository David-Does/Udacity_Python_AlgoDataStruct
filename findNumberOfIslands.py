import copy

def numOfIslands(arr):
    """Returns the number of islands in a given 2d Array"""
    if (not arr[0] or len(arr[0]) == 0):
        return 0
    temp = copy.deepcopy(arr)
    count = 0
    for x in xrange(len(temp)):
        for y in xrange(len(temp[0])):
            if (temp[x][y] is not 0):
                count = count + 1
                bfs(temp,x,y)
    return count

def bfs(tempArr,x,y):
    """Performs a breadth first search and marks 1's as seen by changing their value to 0"""
    stack = [[x,y]]
    while (stack):
        r,c = stack.pop()
        tempArr[r][c] = 0
        stack = stack + findOneAround(tempArr,r,c)

def findOneAround(tempArr,x,y):
    """Returns a list of lists that contain x,y coordinates of where the value is 1"""
    xLimit = len(tempArr)
    yLimit = len(tempArr[0])
    tempArr[x][y] = 0
    for i in xrange(x-1,x+2):
        for j in xrange(y-1,y+2):
            if ((i >= 0 and i < xLimit) and (j>= 0 and j < yLimit)):
                if(tempArr[i][j] is 1):
                    return [[i,j]]
    return []

testArray1 = [[1,0,1],[0,0,0],[1,0,1],[1,1,0]]
testArray2 = [None]
testArray3 = [[]]
print (numOfIslands(testArray1))
print (numOfIslands(testArray2))
print (numOfIslands(testArray3))