'''
Subtract one list from another and return the result
It should remove all values from list a, which are present in list b keeping their order.

My original solution:
'''
def array_diff(a,b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a

print(array_diff([1,2,2],[2]))

'''
# better way:
def array_diff(a, b):
   return [x for x in a if x not in b]
'''
