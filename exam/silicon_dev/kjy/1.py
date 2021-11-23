def solution(rows, columns, connections, queries):
    answer = []
    remove_list = []
    for r1, c1, r2, c2 in queries:
        count = 0
        box = [min([r1, r2]), min([c1,c2]), max([r1,r2]), max(c1,c2)]
        width = range(box[1], box[3]+1) # 가로 
        height = range(box[0], box[2]+1) # 세로
        
        
        for c_box in connections:
            if c_box not in remove_list:
                first, second = min([[c_box[0], c_box[1]], [c_box[2], c_box[3]]]), max([[c_box[0], c_box[1]], [c_box[2], c_box[3]]]) #왼쪽 위가 먼저
                # print(first,second)
                if first[0] in height and first[1] == box[1]-1 and second[1] == box[1] :  # 왼쪽
                    count+=1
                    remove_list.append(c_box)
                    # print('왼쪽',first, second)
                elif first[0] in height and first[1] == box[3] and second[1] == box[3]+1:  # 오른쪽
                    count+=1
                    remove_list.append(c_box)
                    # print('오른쪽',first,second)
                elif first[1] in width and first[0] == box[0]-1 and second[0] == box[0] : # 위쪽
                    count+=1
                    remove_list.append(c_box)
                    # print('위쪽',first,second)
                elif first[1] in width and first[0] == box[2] and second[0] == box[2]+1 : # 아래쪽
                    count+=1
                    remove_list.append(c_box)
                    # print('아래쪽',first,second)
                
        # print(width, height, box)
        # print(connections)
        # print(count)        
        # print('='*30)
        answer.append(count)
        # print('remove',remove_list)
    
    return answer

rows = 4
cols = 3
connections = [[1,1,2,1],[1,2,1,3],[1,3,2,3],[2,2,2,3],[2,2,3,2],[2,3,3,3],[3,2,3,3],[3,2,4,2],[4,1,4,2]]
queries = [[2,2,3,1],[1,2,4,2]]	
print(solution(rows,cols, connections, queries))
