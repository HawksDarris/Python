'''
This returns a list of ints from a list of multiple item types
A little too easy.
'''
def filter_list(l):
    filteredlist=[]
    for item in l:
        if isinstance(item, int):
            filteredlist.append(item)
    if not filteredlist:
        return 'No integers in list'
    return filteredlist

a = [1,'a',2]
b = ['a','b']
print(filter_list(a))
print(filter_list(b))
