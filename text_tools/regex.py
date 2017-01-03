# -*- coding: utf-8 -*-


import string

# f = open('allLeft00_cleaned.txt','w')
f = open('allRight01_cleaned.txt','w')

with open('allRight01.txt') as inputfile:
    for line in inputfile:
        line = line.lower()
        line = line.replace('“','').replace('”','')
        line = line.replace('‘','')
        line = line.replace('\'',' ').replace('’',' ')
        line = line.replace('-',' ')
        line = line.replace('—',' ')
        line = line.translate(None, string.punctuation)
        line = line.translate(None, string.digits)
        print "_______________________"
        f.write(line) # python will convert \n to os.linesep

f.close()


# s.translate(None, string.punctuation)

# def addOne(number):
#     return number + 1
#
# print 4
# print addOne(4)
#
# foo = 11
# addOne(foo)
# print foo
