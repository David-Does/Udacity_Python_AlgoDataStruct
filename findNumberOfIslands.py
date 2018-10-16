import copy

def numOfIslands(arr):
    """Returns the number of islands in a given 2d Array"""
    #remember to guard against nulls
    if(not arr or len(arr[0]) is 0):
        return 0
    temp = copy.deepcopy(arr)
    count = 0
    for x in xrange(len(temp)):
        for y in xrange(x):
            if (temp[x][y] is not 0):
                count = count + 1
                print temp
                bfs(temp,x,y)
                print 'end of bfs'
    return count

def bfs(tempArr,x,y):
    """Performs a breadth first search and marks 1's as seen by changing their value to 0"""
    stack = [[x,y]]
    while (stack):
        i,j = stack.pop(0)
        tempArr[i][j] = 0
        stack = stack + findOneAround(tempArr,i,j)
def findOneAround(tempArr,x,y):
    """Returns a list of lists that each contain x,y coordinates of where the value is 1"""
    xLimit = len(tempArr)
    yLimit = len(tempArr[0])

    result = []
    for i in xrange(x-1,x+2):
        for j in xrange(y-1,y+2):
            if ((i >= 0 and i < xLimit) and (j>= 0 and j < yLimit)):
                if(tempArr[i][j] is 1):
                    result.append([i,j])
    return result

testArray = [[1,0,1],[0,0,0],[1,0,1],[1,1,0]]
print (numOfIslands(testArray))