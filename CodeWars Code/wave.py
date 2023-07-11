'''
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
'''
def wave(text):
    textlist = list(text.lower())
    wave = []
    i = 0
    for i in range(len(textlist)):
        if not textlist[i].isspace():
            textlist[i]=textlist[i].upper()
            wave.append(''.join(textlist))
            textlist[i]=textlist[i].lower()
    return wave

print(wave("  AB C"))

# Lowercase entire list
# uppercase index 0
# append index 0 to list
# append index 1 through len(list) to list
# Convert list to string
# append string to list
# Lowercase entire list
# uppercase index 0
