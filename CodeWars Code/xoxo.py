'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
If it has no x or o, it should return True
Easy
'''
def XO(text):
    text = text.lower()
    return text.count('x') == text.count('o')
