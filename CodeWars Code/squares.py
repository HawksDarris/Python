'''
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
'''
def checksquare(num):
    return num >= 0 and num**0.5 % 1 == 0

print(checksquare(-25))
print(checksquare(25))
print(checksquare(5))
