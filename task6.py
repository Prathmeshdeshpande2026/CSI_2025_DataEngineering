<<<<<<< HEAD
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)

    print(hash(t));
=======
from collections import Counter
X = int(input())
sizes = list(map(int, input().split()))
money = 0
N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    cnt = Counter(sizes)
    if lst[0] in cnt.keys():
        money += lst[1]
        sizes.remove(lst[0])
    else:
        money += 0
print(money)
>>>>>>> 00ae9eb (Assignments 2)
