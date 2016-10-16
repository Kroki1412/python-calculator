import sys

print ("This is a simple calculator that can do addition, subtraction, multiplicatin and division. "
       "If a letter is entered instead of a natural Number or an operation the application will exit")

# this function validates the number. If it is a letter it will quit, if it is number it will continue.
# if an other character is present it will ask for an other number (making it only work for natural numbers).
def isLetter(userinput):
    if userinput.isalpha():
        sys.exit()
    elif userinput.isdigit():
        userinputvalid = 'valid'
    else:
        userinputvalid = 'invalid'
        print ("that is not a natural number!")
    return userinputvalid

# This function is for determing the action (which is not used later on) it also eliminates invalid characters as operations.
def isOperation(userinput):
    if userinput == '+':
        operation = 'addition'
    elif userinput == '-':
        operation = 'subbtraction'
    elif userinput == '*':
        operation = 'multiplication'
    elif userinput == '/':
        operation = 'division'
    else:
        print('How do you think this math operation will look?')
        operation = 'invalid'
    return operation

#This function is used for calculation. but first boty numbers are converted into integers.
def theMath(num1, oper, num2):
    num1 = int(num1)
    num2 = int(num2)
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        result = num1 / num2
    else:
        print ("Something went horribly wrong so I quit!")
        sys.exit()
    return result

#This variable is only to keep a forever loop for the 4 while loops ahead.
userinputvalid1 = 'unknown'

#The first loop is letting the script run indefinetly. the 3 loops inside are to ask for other data to be entered.
while (userinputvalid1 != 'valid'):
    while (userinputvalid1 != 'valid'):
        firstnumber = input("Enter a number (or a letter to exit):")
        if (isLetter(firstnumber) != 'valid'):
            continue
        else:
            break


    while (userinputvalid1 != 'invalid'):
        operator = input("Enter an operation:")
        if (isOperation(operator) == 'invalid'):
            continue
        else:
            break


    while (userinputvalid1 != 'valid'):
        secondnumber = input ("Enter another number:")
        if (isLetter(secondnumber) != 'valid'):
            continue
        else:
            break
    print ('%s %s%s%s%s %s' % ('Result:',firstnumber,operator,secondnumber,'=',theMath(firstnumber, operator, secondnumber)))
    print ('\n')