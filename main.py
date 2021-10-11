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




#Множества
#1
str = input()
mySet = set(str.lower())
print(len(mySet))

#2
mySet = set(input().split())
print(len(mySet) - 1)


#3
m = int(input())
mySet = set(input().split())
print(len(mySet) ** m)


#4
myStr = input()
mySet = set(myStr)
myList = list(i for i in mySet if myStr.count(i) == 1)
print(''.join(str(i) for i in sorted(myList)))


#5
myStr = input()
mySet = set(myStr)
if len(myStr) == len(mySet):
    print("NO")
else:
    print("YES")


#6
str1 = set(input())
str2 = set(input())
print(str1.intersection(str2) == str2)


#7
n, m = map(int, input().split())
list1 = set(tuple(map(int, input().split())) for i in range(n))
list2 = set(tuple(map(int, input().split())) for j in range(m))
mySet1 = sorted(list1 & list2)
mySet2 = sorted(list1 - list2)
if len(mySet1) == 0:
    print("empty")
else:
    print(' '.join(str(i) for i in mySet1))
if len(mySet2) == 0:
    print("empty")
else:
    print(' '.join(str(i) for i in mySet2))


#8
n, m = map(int, input().split())
myList = [tuple(map(int, input().split())) for i in range(m)]
sets = list(set(tuple(map(int, input().split())) for k in range(m)) for j in range(n - 1))
myResSet = [0] * m
for i in range(n - 1):
    for j in set(myList) & sets[i]:
        myResSet[myList.index(j)] += 1
if max(myResSet) == 0:
    print(-1)
else:
    print(' '.join(str(i) for i in myList[myResSet.index(max(myResSet))]))


#9
size = int(input())
count = 0
numbers = []
for i in range(size):
    numbers.append(int(input()))
if size == 1:
    print('N')
else:
    for i in range(size - 1):
        list_first = list(str(numbers[i]))
        list_second = list(str(numbers[i + 1]))
        result = list(set(list_first) & set(list_second))
        if len(result) == 2:
            print(numbers[i])
            count = 1
    if count == 0:
        print('N')


#10
n = int(input())
myListOfString = input().split()
myResList = []
for i in range(n):
    if len(myListOfString[i]) != len(set(myListOfString[i])):
        myResList.append(myListOfString[i])
print(' '.join(str(i) for i in myResList))