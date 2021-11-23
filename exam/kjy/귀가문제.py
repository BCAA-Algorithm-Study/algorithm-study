import heapq

def solution(n, s, a, b, fares):
    answer = []
    INF = 1e9
    graph = [[INF]*(n+1) for _ in range(n+1)]
    adj_graph = [[] for _ in range(n+1)]
    for i in range(len(fares)):
        node_a, node_b, fare = fares[i]
        graph[node_a][node_b] = fare
        graph[node_b][node_a] = fare
        adj_graph[node_a].append(node_b)
        adj_graph[node_b].append(node_a)
        
    def dijkstra(start,end):
        distances = [INF] * (n+1)
        if start == end:
            return 0
        q = [[0,start]]
        while q:
            c, current_node = heapq.heappop(q)
            if c > distances[current_node]:
                continue
            for adj_node in adj_graph[current_node]:
                cost = c + graph[current_node][adj_node]
                if distances[adj_node] > cost:
                    distances[adj_node] = cost
                    heapq.heappush(q,[cost, adj_node])
        return distances[end]
    # print(adj_graph)
    queue = [[0, s]]
    distances = [INF] * (n+1)
    # print('graph',graph)
    while queue:
        c, current_node = heapq.heappop(queue)
        if c > distances[current_node] :
            continue
        answer.append(c + dijkstra(current_node, a) + dijkstra(current_node, b))
        # print('dij' ,current_node,a,b,c,dijkstra(current_node, a), dijkstra(current_node, b))
        # print('answer',answer)
        for adj_node in adj_graph[current_node]:
            cost = c + graph[current_node][adj_node]
            # print('dis',distances)
            
            if distances[adj_node] > cost:
                distances[adj_node] = cost
                heapq.heappush(queue,[cost, adj_node]) 
                # print('que',queue)
    return answer

# n= 6
# s= 4	
# a = 6
# b = 2	
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# print(solution(n,s,a,b,fares))

n= 6
s= 4	
a = 5
b = 6	
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s,a,b,fares))