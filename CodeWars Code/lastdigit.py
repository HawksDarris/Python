'''
Returns the last digit of a large number while avoiding computation.

I am proud of myself for this one. I had to do a bunch of research into this because it kept timing out. Then I learned that the last digit of X^n is predictable because the last digit will repeat at least once in X^n, X^(n+1), X^(n+2), X^(n+3), and X^(n+4), so you can just skip all of the calculations that would make the last digit the same as the last digit of the number you're currently on.
'''
def lastdigit(a):
    if not a:
        return 1
    result = 1
    for x in reversed(a):
        result = x ** (result if result < 4 else result % 4 + 4)
    return result % 10

a = [7,6,21]
print(lastdigit(a))
