import sys
n = int(sys.stdin.readline())
students = []
for i in range(n):
    student = sys.stdin.readline().split()
    students.append((student[1], student[0]))
students.sort()
for score, student in students:
    print(student, end=' ')