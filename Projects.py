import random

def projectlist():
    numberofprojects = 8
    projects=[]
    for i in range(numberofprojects):
        projects.append(i)
    return projects

def printprojects():
    projects = projectlist()
    for i in range(len(projects)):
        print("Project",projects[i]+1)

def getanswer():
    answer = input('Please select a project. ')
    while True:
        if not answer in projects:
            print('You must select a project number from the list with a numeral.')
        else:
            print("Coming right up...")
            return answer
        break

def getcalcnumbers():
    str1 = input("First number ")
    str2 = input("Second number ")
    return float(str1), float(str2)

def getoperator():
    while True:
        try:
            operator = int(input('Choose one\n'))
            break
        except ValueError:
            print('Please use a numeral')
        except:
            print('Please use one of the numerals I gave you.')
    return operator


def printcalc():
    print('The first number will be on the left of the equation. Which operation would you like?')
    print('The available operators are:\n + (1)\n - (2)\n * (3)\n / (4) and\n ^ (5)')
    operator = getoperator()
    num1, num2 = getcalcnumbers()
    if operator == 1:
        print("Added:\n", num1, "+", num2, "=", num1+num2)
    elif operator == 2:
        print("Subtracted:\n", num1 , "-", num2 , "=", num1-num2)
    elif operator == 3:
        print("Multiplied:\n", num1 , "*", num2 , "=", num1*num2)
    elif operator == 4:
        print("Divided:\n", num1 , "/", num2 , "=", num1/num2)
    elif operator == 5:
        print("Exponentialized:\n", num1 , "^", num2 , "=", num1**num2)

def getdimensions():
    str1 = input("Give the base: ")
    str2 = input("Give the height: ")
    return(float(str1),float(str2))

def printarea():
    dimensions = getdimensions()
    base = dimensions[0]
    height = dimensions[1]
    return base*height/2

def getmultiplicative():
    num = input('What number would you like a table for?\n')
    return int(num)

def printmultiplicative(i=0):
    i = getmultiplicative()
    ii = 0
    print(str(i)+":")
    for ii in range(12):
        ii += 1
        if ii%3 != 0:
            print(i,'*',ii,'=',i*ii,end='   ')
        else:
            print(i,'*',ii,'=',i*ii)
        print('')

def hasdigit(str1='1'):
    # returns True if there is a digit
    # default is True
    return any(char.isdigit() for char in str1)

def hasletter(str1='a'):
    # returns True if there is a letter
    # default is True
    return any(char.isalpha() for char in str1)


def getnumbers():
    userinput = input('Enter some numbers separated with spaces and hit enter.\n')
    while hasletter(userinput):
        print('It should have only numbers and spaces.')
        userinput = input('Enter some numbers separated with spaces and hit enter.\n')
    inputlist = userinput.split()
    return inputlist


def printlargest():
    inputlist = getnumbers()
    inputlist = [int(i) for i in inputlist] # if you don't convert it to ints, it will think 4 is larger than 24 because 2 is before 4 alphabetically in strings.
    print('Your largest number is',sorted(inputlist,reverse=True)[0])

def getwords():
    userinput = input('Enter some words you want to sort separated with spaces and hit enter.\n')
    while hasdigit(userinput):
        print('It should have no digits.')
        userinput = input('Enter some words you want to sort separated with spaces and hit enter.\n')
    inputlist = userinput.split()
    return inputlist

def printalphabetically():
    inputlist = getwords()
    inputlist.sort()
    print("This is your list resorted:")
    for i in range(len(inputlist)):
        print(inputlist[i],end=' ')
        i += 1
    print('')

def diceroll():
    i = 0
    ii = 0
    while True:
        i = random.randint(1,6)
        ii = random.randint(1,6)
        print('You got',i)
        print('I got', ii)
        if i == ii:
            print('We tied.')
        elif i <= ii:
            print('I win.')
        elif i >= ii:
            print('You win.')
        userinput = input('Enter "Y" to play again.')
        if userinput.lower() != 'y':
            print('Good game. See you later.')
            break

def getrandomword():
    file = open('projectRandomWords','r')
    with file as myfile:
        words = myfile.readline().strip()
        wordlist = words.split()
        numberofwords = len(wordlist)
        randindex = random.randint(0,numberofwords)
        print('The whole list of words:', wordlist)
        print('A random word:')
        print(wordlist[randindex])

def computermove():
    moves=['Rock','Paper','Scissors']
    computermove = random.randint(0,len(moves)-1)
    return moves,computermove

def getusermove():
    while True:
        try:
            usermove = int(input('Choose one:\n'))
            break
        except:
            print('Enter 1, 2, or 3.')
    return usermove

def rockpaperscissors():
    # bring in the list of moves and the computer move:
    moves, computermoveint = computermove()
    # assign the computer move to the list:
    compmove = moves[computermoveint]

    while True:
        print(moves[0],'(1)', moves[1],'(2)', moves[2], '(3)')
        usermoveint = getusermove()-1
        usermove = moves[usermoveint] # -1 because otherwise choosing scissors makes it out of range
        if usermoveint == computermoveint:
            print('We both played', compmove,end='. ')
        elif usermoveint == 0:
            if computermoveint == 2:
                print('I played', compmove,end='. ')
                print('You played', usermove,end='. ')
                print('You win.')
            else:
                print('I played', compmove,end='. ')
                print('You played', usermove,end='. ')
                print('I win.')
        elif usermoveint == 1:
            if computermoveint == 2:
                print('I played', compmove,end='. ')
                print('You played', usermove,end='. ')
                print('I win.')
            else:
                print('I played', compmove,end='. ')
                print('You played', usermove,end='. ')
                print('You win.')
        elif usermoveint == 2:
            if computermoveint == 0:
                print('I played', compmove,end='. ')
                print('You played', usermove,end='. ')
                print('I win.')
            else:
                print('I played', compmove,end='. ')
                print('You played', usermove,end='. ')
                print('You win.')
        playagain = input('Enter "Y" to play again. ')
        if playagain.lower() == 'y':
            print('')
        else:
            print('Good game. Goodbye.')
            break

printprojects()
answer = getanswer()
if answer == projects[0]:
    print('This project will do simple arithmetic with two numbers.')
    try:
        printcalc()
    except:
        print("Use numerals that make sense, please")
if answer == projects[1]:
    print('This project will find the area of a triangle with user input for the base and height.')
    try:
        print("The area of the triangle is:",printarea(),"square units")
    except:
        print("Use numerals that make sense, please")
if answer == projects[2]:
    print('This project prints a times table to 12 for a user-input digit')
    try:
        printmultiplicative()
    except:
        print("Use numerals that make sense, please")
if answer == projects[3]:
    print('This project compares numbers the user gives it and prints the largest.')
    try:
        printlargest()
    except:
        print("Use numerals that make sense, please")
if answer == projects[4]:
    print('This project prints words you give it after sorting alphabetically.')
    try:
        printalphabetically()
    except:
        print("Use letters, not numbers, please")
if answer == projects[5]:
    print('This project simulates a dice game.')
    diceroll()
if answer == projects[6]:
    print('This project gets a random word from a file I put random words in.')
    getrandomword()
if answer == projects[7]:
    print('This project plays Rock, Paper, Scissors.')
    rockpaperscissors()
