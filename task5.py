<<<<<<< HEAD
import itertools

n = int(input())
letters = input().split()
k = int(input())

nb, tot = 0, 0
for t in itertools.combinations([i for i in range(n)], k):
    tot += 1
    for i in t:
        if letters[i] == 'a':
            nb += 1
            break
print(round(nb / tot, 3))
=======
import textwrap
def merge_the_tools(st, k):
    # your code goes here
    t=textwrap.wrap(st, k)
    for i in t:
        l=[]
        for j in i:
            if j not in l:
                l.append(j)
        print(''.join(l))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
>>>>>>> 00ae9eb (Assignments 2)
