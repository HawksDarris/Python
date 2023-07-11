def longest(s1,s2):
    uniques = []
    s3 = s1+s2
    for i in s3:
        if uniques.count(i) > 0:
            continue
        else:
            uniques.append(i)
    return ''.join(sorted(uniques))

print(longest('abcd','abcdefg'))

'''
Better solution:
def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))
'''
