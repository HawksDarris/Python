'''
returns the sum of multiples of 5 and 3 in a given integer
'''
def solution(n):
    return sum([i for i in range(n) if (i%3==0 and i%5==0) or (i%3 == 0 or i%5 == 0)])

print(solution(16))
