import copy

def numOfIslands(arr):
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
    stack = [[x,y]]
    while (not stack):
        i, j = stack.pop(0)
        tempArr[i,j] = 0
        stack.append(findOneAround(tempArr,i,j))



def findOneAround(tempArr,x,y):
    output=[]
    if(x-1 >= 0):
        if (y-1 >= 0):
            for i in xrange(3):
                for j in xrange(3):
                    currX = x-1 + i
                    currY = y-1 + j
                    if (tempArr[currX][currY] is 1):
                        output.append([i,j])

