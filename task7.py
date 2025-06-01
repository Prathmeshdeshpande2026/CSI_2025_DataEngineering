<<<<<<< HEAD
if __name__ == '__main__':

    n = int(input())

    student_marks = {}

    for _ in range(n):

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores

    query_name = input()

    l1 = list(student_marks[query_name]) 

    addition = sum(l1)

    result = addition/len(l1)

    print('%.2f'% result)
=======
T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
>>>>>>> 00ae9eb (Assignments 2)
