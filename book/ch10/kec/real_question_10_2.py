def find_team(team, x) :
    if team[x] != x :
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b) :
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b :
        team[b] = a
    else :
        team[a] = b

N, M = map(int, input().split())

team = [i for i in range(N + 1)]
for _ in range(M) :
    c, a, b = map(int, input().split())
    if c == 0 :
        union_team(team, a, b)
    else :
        if find_team(team, a) == find_team(team, b) :
            print('YES')

        else :
            print('NO')
