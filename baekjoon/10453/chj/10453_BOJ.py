import sys
input = sys.stdin.readline

def move(a, b):
    result = 0
    if len(a) != len(b):
        return -1

    a_trg_pos = [i for i in range(len(a)) if a[i] == 'a']
    b_trg_pos = [i for i in range(len(b)) if b[i] == 'a']

    if len(a_trg_pos) != len(b_trg_pos):
        return -1

    for pos in range(len(a_trg_pos)):
        result += abs(a_trg_pos[pos] - b_trg_pos[pos])
    return result


n = int(input())
text = []
for _ in range(n):
    text.append(input().split())

for t in text:
    a, b = t
    print(move(a, b))
