# returns the smallest positive integer not in the list
def smallest(A):
    # Remove negative numbers from the list
    A = [a for a in A if a > 0]

    # If the list is empty, the smallest positive integer is 1
    if not A:
        return 1

    # Sort the list
    A.sort()
    # make a variable that starts as the smallest positive integer A (not including 0)
    smallest = 1

    for i in A:
        # If the element is equal to the smallest positive integer, increment it
        if i == smallest:
            smallest += 1
        # If the element is greater than the smallest positive integer, return it
        elif i > smallest:
            return smallest

    # If all elements in the list are consecutive positive integers, return the next one
    return smallest
A = [1,2,3]
B = [1,2,4,6]

print(smallest(A))
print(smallest(B))
