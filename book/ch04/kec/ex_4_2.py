hour = int(input())
cnt = 0
minute = 60
second = 60
saved_cnt = 0
for m in range(minute) :
    m = str(m)
    if '3' in m :
        saved_cnt += 60
    else :
        for s in range(second) :
            s = str(s)
            if '3' in s :
                saved_cnt += 1

for h in range(hour + 1) :
    h = str(h)
    if '3' in h :
        cnt += 60 * 60
    else :
        cnt += saved_cnt

print(cnt)