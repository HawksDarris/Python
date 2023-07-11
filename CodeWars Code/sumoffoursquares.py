'''
This is the inefficient method, brute forcing it.
def four_squares(n: int) -> tuple[int, int, int, int]:
    if n < 0:
        return None
    for a in range(int(n**0.5)+1):
        for b in range(int((n-a*a)**0.5)+1):
            for c in range(int((n-a*a-b*b)**0.5)+1):
                dsquared = n - a*a - b*b - c*c
                d = int(dsquared**0.5)
                if d**2 == dsquared:
                    return (a,b,c,d)

def four_squares(n: int) -> tuple[int, int, int, int]:
    memo = {}
    a_max = int(n**0.5)

    for a in range(a_max, -1, -1):
        a_squared = a*a
        if a_squared > n:
            continue

        b_max = int((n - a_squared)**0.5)
        for b in range(b_max, -1, -1):
            b_squared = b*b
            if a_squared + b_squared > n:
                continue

            c_max = int((n - a_squared - b_squared)**0.5)
            for c in range(c_max, -1, -1):
                c_squared = c*c
                if a_squared + b_squared + c_squared > n:
                    continue

                dsquared = n - a_squared - b_squared - c_squared
                if dsquared in memo:
                    d = memo[dsquared]
                else:
                    d = int(dsquared**0.5)
                    memo[dsquared] = d

                if a_squared + b_squared + c_squared + dsquared == n:
                    return (a, b, c, d)

    return None
'''


print(four_squares(215))
