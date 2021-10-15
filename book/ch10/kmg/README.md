

### 크루스칼 알고리즘
#### 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘 "최소 신장 트리 알고리즘" -> 크루스칼 알고리즘

### 위상 정렬: O(v+e)
```python
    def topology_sort():
        result = []
        q = deque()

        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            now= p.popleft(q)
            result.append(now)
            for i in graph[now]:
                indefree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
```


#### 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'

#### 진입 차수: 특정 한 노드로 '들어노는' 간선의 개수를 의미한다. 
