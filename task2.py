<<<<<<< HEAD
from itertools import groupby
s=input()
l=[]
l2=[]
for k,g in groupby(s):
    l.append(list(g))
    l2.append(k)
for i in range(len(l2)):
    print("("+str(len(l[i]))+", "+str(l2[i])+")",end=" ")
=======
def average(array):
    # your code goes here
    setCollection = set()


    for x in array:
         setCollection.add(x)

    sum = 0
    i = 0
    for val in setCollection:
        sum = sum + val
        i = i + 1

    total = sum/i

    return total

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
>>>>>>> 00ae9eb (Assignments 2)
