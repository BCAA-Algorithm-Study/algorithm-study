N = int(input())
move_list = input().split()
x, y = 1, 1
for m in move_list :
    m = m.upper()
    if m == 'L' and y > 1 :
        y -= 1
    elif m == 'R' and y < N :
        y += 1
    elif m == 'U' and x > 1 :
        x -= 1
    elif m == 'D' and x < N :
        x += 1

print(x, y)