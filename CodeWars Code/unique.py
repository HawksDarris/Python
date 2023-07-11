'''
returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
'''
def unique_in_order(sequence):
    uniques = []
    mostrecent = ''
    for i in sequence:
        if i == mostrecent:
            continue
        else:
            uniques.append(i)
            mostrecent = i
    return uniques

print(unique_in_order('ADAAABBBCCDAABBB'))
