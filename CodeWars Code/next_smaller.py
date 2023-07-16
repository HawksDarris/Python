'''
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
    return -1 when there is no smaller number that containst the same digits
    some tests will be with very large numbers
    only positive integers

Thought process:
    1. Each digit in a number from right to left will be == 10^[index]+digit, so I think I need to make the number into a list and move backward through the list.
        Therefore any digit that moves up needs to move an equal or larger digit down or the number would be getting bigger, not smaller.

    2. Sorting the list to find the smallest possible number is probably not helpful because we only want the next smallest number.

    3. With very large numbers, there are many permutations (n^r)
        where n is the number of digits and r is the number of options for each digit (0-9)).
            so, in a 10-digit number, n = 10 and r = 10; 10^10 is 10 billion, so brute forcing not ideal

    4. If I move rightward the first digit that is larger than the digit to its right, the number will certainly be lower by the correct order of magnitude for the next lowest number, but the digits remaining to the changed digit's right could make it smaller than the next smaller number.
    I think I figured it out.
        Because we are in the correct order of magnitude now, if I sort the remaining digits in descending order, it will be the highest number within that order of magnitude, which is the only possible order of magnitude to correctly return the next smaller number.

---------------------------------------------------------------
------------------------------------------------------------------
Plan:
    1. Make a list of the digits in num
    2. loop through the list from the right until a digit on the left is higher than the current digit
    3. swap those two digits
    4. after swapping, sort the digits to the right of the lower digit in descending order
    5. turn it back into an int and return it
'''
def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]

def next_smaller(num):
    digits = [x for x in str(num)]

    # Find the first occurrence where the current digit is greater than the next digit
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            # Find the rightmost digit that is smaller than the current digit
            for j in range(len(digits) - 1, i, -1):
                if digits[j] < digits[i]:
                    # Swap the digits
                    swap(digits, i, j)
                    # Sort the remaining digits in ascending order, and put them back in the list
                    # This is necessary to make sure it's the NEXT smallest
                    # number.
                    digits[i+1:] = sorted(digits[i+1:], reverse=True)
                    # convert back to int, return
                    # Oops. Forgot to deal with leading zeroes.
                    # If the first is not 0 and it's not the same as it started,
                    # return it.
                if digits[0] != '0' and int(''.join(digits)) != num:
                    return int(''.join(digits))
    return -1  # Return -1 if no smaller number exists

test = 907
test2 = 1234567908
test3 = 1027
test4 = 43

print(next_smaller(test))
print(next_smaller(test2))
print(next_smaller(test3))
print(next_smaller(test4))
