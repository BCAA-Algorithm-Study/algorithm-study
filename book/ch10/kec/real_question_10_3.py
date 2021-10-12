def find_route(route, a) :
    if route[a] != a :
        route[a] = find_route(route, route[a])
    return route[a]

def union_route(route, a, b) :
    a = find_route(route, a)
    b = find_route(route, b)
    if a < b :
        route[b] = a
    else :
        route[a] = b

N, M = map(int, input().split())
route = [i for i in range(N + 1)]
edges = []
result = []

for _ in range(M) :
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges :
    c, a, b = edge
    if find_route(route, a) != find_route(route, b) :
        union_route(route, a, b)
        result.append(c)

# print(result)
print(sum(result) - max(result))
