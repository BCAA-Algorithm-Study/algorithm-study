num = int(input())

students = {}
for i in range(num) :
    k, v = input().split()
    students[k] = int(v)

students = sorted(students.items(), key = lambda x : x[1])

for k, v in students :
    print(k, end = ' ')