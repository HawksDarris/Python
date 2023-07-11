'''
Returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
'''
def sum_two_smallest_numbers(numbers):
    for i in numbers:
        if i < 0:
            numbers.remove(i)
    numbers.sort()
    return numbers[0]+numbers[1]

print(sum_two_smallest_numbers([5,-2,10,100,1000]))

'''
Apparently I misunderstood.
The array will have only positive numbers, so I don't need to remove the negatives
'''
