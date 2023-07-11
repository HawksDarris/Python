def solution(s):
    breakcamel = []
    i = int(-1)
    for char in s:
        i += 1
        if char.isupper():
            breakcamel.append(' ')
        breakcamel.append(char)
        s = ''.join(breakcamel)
    return(s)

'''
Better solution:

def solution(s):
    return ''.join(' ' + x if x.isupper() else x for x in s)
'''
print(solution("camelCaseTest"))
