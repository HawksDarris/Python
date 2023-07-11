def spin(word):
    return word[::-1]

def spin_words(sentence):
    spun = []
    for word in sentence.split():
        if len(word)>=5:
            spun.append(spin(word))
        else:
            spun.append(word)
    return ' '.join(spun)


print(spin_words('Hello my'))
