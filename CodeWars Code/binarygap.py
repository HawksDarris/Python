def solution(N):
    # Convert N to binary string
    binary = bin(N)[2:]

    # Initialize variables
    max_gap = 0
    current_gap = 0

    # Iterate over binary string
    for digit in binary:
        if digit == '1':
            # End of a gap
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        else:
            # Inside a gap
            current_gap += 1

    return max_gap

a = 1041
b = 65
c = 15
print(f'{a:08b}')
print('The longest string of 0s is',solution(a))
print(f'{b:08b}')
print('The longest string of 0s is',solution(b))
print(f'{c:08b}')
print('The longest string of 0s is',solution(c))
