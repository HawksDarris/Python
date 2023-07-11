'''
You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
Note:
If you are given an array with multiple answers, return the lowest correct index.
'''
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[0:i])==sum(arr[i+1:len(arr)]):
            return i
    return -1

a = [1,2,1]
b = [1,2,1,4]
print(find_even_index(a))
print(find_even_index(b))
