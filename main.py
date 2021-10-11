#1
myStr = input()
if len(myStr) % 2 == 0:
    if myStr[:len(myStr) // 2] == myStr[len(myStr) // 2:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")


#2
n = int(input())
myList = []
for i in range(n):
    myList.append(input())
count = int(0)
for i in myList:
    if i.count('..') == 0 and i.count('@') == 1 and i[0] != '@' and i[len(i) - 1] != '@':
        count += 1
print(count)


#3
import re

myStr = input()
print(re.sub(r'(\w)\1+', r'\1\1', myStr))

#4
myStr = input()
if myStr.isupper():
    myStr = myStr.lower()
elif myStr[0].islower():
    if len(myStr) > 1 and myStr[1:].isupper():
        myStr = myStr[0].upper() + myStr[1:].lower()
    elif len(myStr) == 1:
        myStr = myStr.upper()
print(myStr)


#5
myStr = input()
while myStr.find('oops') != -1:
    myStr = myStr.replace('oops', '')
print(myStr)


#6
k = int(input())
myStr = input()
myList = []
i = int(0)
j = int(0)
while i < len(myStr):
    if myStr[i] == '.':
        if i < len(myStr) - 2 and myStr[i + 1] == '.':
            myList.append(myStr[j: i + 3])
            j = i + 3
            i += 3
        else:
            myList.append(myStr[j: i + 1])
            j = i + 1
            i += 1
    else:
        i += 1
print(myList[k - 1])


#7
def findPal(myStr):
    def findOdd(myStr):
        maxLenght = 1
        for i in range(len(myStr)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(myStr) and myStr[l] == myStr[r]:
                new_str = myStr[l:r + 1]
                if len(new_str) > maxLenght: maxLenght = len(new_str)
                l -= 1
                r += 1
        return maxLenght

    def findEven(myStr):
        maxLenght = 1
        for i in range(len(myStr)):
            l = i
            r = i + 1
            while l >= 0 and r < len(myStr) and myStr[l] == myStr[r]:
                new_str = myStr[l:r + 1]
                if len(new_str) > maxLenght: maxLenght = len(new_str)
                l -= 1
                r += 1
        return maxLenght

    return max([findOdd(myStr), findEven(myStr)])


myStr = input()
print(findPal(myStr))

#8
def isPalindrom(myStr):
    return myStr == myStr[::-1]


myStr = input()
if not isPalindrom(myStr):
    j = int(0)
    while j < len(myStr):
        if isPalindrom(myStr[j:]):
            print(myStr + myStr[:j][::-1])
            break
        j += 1
else:
    print(myStr)


#9
list = ['a', 'i', 'u', 'o', 'e']


def isVowel(ch):
    if list.count(ch) != 0:
        return True
    else:
        return False


myStr = input()
flag = True
for i in range(len(myStr)):
    if isVowel(myStr[i].lower()):
        print("V", end="")
        flag = True
    elif myStr[i].upper() == 'Y':
        if i == 0 or not flag:
            print("V", end="")
            flag = True
        else:
            print("C", end="")
            flag = False
    else:
        print("C", end="")
        flag = False