# def binary_search(input_array, value):
#     left = 0
#     right  = len(input_array)-1
#     mid = (right - left) / 2
#     while (left <= right):
#         if (input_array[mid] == value):
#             return mid
#         elif(input_array[mid] > value):
#             right = mid - 1
#             mid = left + (right-left)/2
#         elif(input_array[mid] < value):
#             left = mid + 1
#             mid = left + (right-left)/2
#     return -1
#
# test_list = [1,3,9,11,15,19,29]
# test_val1 = 25
# test_val2 = 15
# #print binary_search(test_list, test_val1)
# #print binary_search(test_list, test_val2)

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def swap(array,index1,index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def getIndexOfMedian(array,index1,index2,index3):
    if (array[index2] <= array[index3]):
        if(array[index2] >= array[index1]):
            pivotIndex = index2
        elif(array[index1] <= array[index3]):
            pivotIndex = index1
        else:
            pivotIndex = index3
    else:
        if(array[index2] <= array[index1]):
            pivotIndex = index2
        elif(array[index3] <= array[index1]):
            pivotIndex = index1
        else:
            pivotIndex = index3
    return pivotIndex
    
def quicksort(array,start,end):
    # print array[start:end+1]
    if (end-start < 1):
        return array
    else:
        left = start
        right = end
        mid = (right+left)/2
        pivotIndex = getIndexOfMedian(array,left,mid,right)
        pivot = array[pivotIndex]
        # print "pivot: ", pivot
        swap(array,right,pivotIndex)
        pivotIndex = right

        i = left
        j = right - 1

        while i <= j:
            while array[i] < pivot:
                # print i, "Value:", array[i], " ? ", pivot
                i = i + 1
                # print
            # print "i:", i
            while array[j] > pivot:
                # print j, "Value:", array[j], " ? ", pivot
                j = j - 1
                # print
            # print "j:", j
            if i <= j:
               # print array[start:end+1]
                swap(array,i,j)
                i = i + 1
                j = j - 1
            # print array[start:end+1]
        swap(array,i,pivotIndex)
        # print array[start:end+1]
        # print "before partition","i:", i
        holdVali = i
        quicksort(array,left,i-1)
        quicksort(array,holdVali+1,right)
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test1 = [1,2,3,4,5,6,7,8]
test3 = [9,8,7,6,4,2]
test4 = []
test5= [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
test2 = [3]
print quicksort(test1,0,len(test1)-1)
print quicksort(test4,0,len(test4)-1)
print quicksort(test3,0,len(test3)-1)
print quicksort(test5,0,len(test5)-1)
# print quicksort(test,0,len(test)-1)