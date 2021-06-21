import csv
from collections import OrderedDict

"""
    The Levenshtein distance is a string metric for measuring the difference between two sequences.
    It is calculated as the minimum number of single-character edits necessary to transform one string into another
"""

"""
this part of the code changes the csv into a list
"""
results = []
with open("D:\Dokumente\Downloads/20210103_hundenamen.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
"""
this part of the code checks how many names are in the list have a Levenshtein distance of 1
"""
names = []
test = 'Luca'
distacne = 0
for i,e in enumerate(results):
    name = str(e).split(',')
    """ checks is Luca is the name list """
    if name[0][2:-1] == test:
        names.append('Luca')

        """ checks is many names with 4 letters are the name list with a distance of 1 """
    elif len(name[0][2:-1]) == 4:
        nametest=name[0][2:-1]
        for i in range(len(nametest)):
            if nametest[i]!=test[i]:
                distacne+=1
        if distacne<=1:
            names.append(nametest)

            """ checks is many names with 3 letters are the name list with a distance of 0 """
    elif len(name[0][2:-1]) == 3:
        nametest=name[0][2:-1]
        for i in range(len(nametest)):
            if nametest[i]!=test[i]:
                distacne+=1
        if distacne<=0:
            names.append(nametest)

            """ checks is many names with 5 letters are the name list with a distance of 0 """
    elif len(name[0][2:-1]) == 5:
        nametest=name[0][2:-1]
        for i in range(len(nametest)-1):
            if nametest[i]!=test[i]:
                distacne+=1
        if distacne<=0:
            names.append(nametest)
        distacne = 0
        for i in range(1,len(nametest)):
            if nametest[i]!=test[i-1]:
                distacne+=1
        if distacne<=0:
            names.append(nametest)

    distacne = 0

""" All duplicates are removed """
names = list(OrderedDict.fromkeys(names))
print("The found names are:")
print(names)
