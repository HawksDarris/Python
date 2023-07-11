
'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.
'''
def alphabet_position(text):    text = text.lower()
    output = []
    for char in text:
        if ord(char)<123 and ord(char)>95:
            num = ord(char) - 96
            output.append(num)
    final = ' '.join(str(e) for e in output)
    return final

# Better solution:
# def alphabet_position(text):
    #return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# I did not know that "isalpha" was a test :)
