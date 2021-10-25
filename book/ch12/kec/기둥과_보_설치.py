# https://programmers.co.kr/learn/courses/30/lessons/60061
import copy

def check_possible(answer, array) :
    x, y, a, b = array
    if b == 1 :
        if a == 0 :         # 기둥 설치시
            if y != 0 and [x, y - 1, 0] not in answer : # 바닥 X, 밑에 기둥 X
                if [x - 1, y, 1] not in answer and [x, y, 1] not in answer: # 밑에 보 X
                    return False

        else : # 보 설치시
            if y != 0 and ([x, y - 1, 0] not in answer and [x + 1, y - 1, 0] not in answer): #바닥 X, 밑에 기둥 X
                if [x - 1, y, 1] not in answer or [x + 1, y, 1] not in answer : #양 끝에 보 X
                    return False
        return True
    else :
        temp = copy.deepcopy(answer)
        temp.remove([x, y, a])
        if a == 0 : #기둥 삭제시
            if [x, y + 1, 1] in answer and not check_possible(temp, [x, y + 1, 1, 1]) : # 오른쪽 보 확인
                return False
            if [x - 1, y + 1, 1] in answer and not check_possible(temp, [x - 1, y + 1, 1, 1]) : # 왼쪽 보 확인
                return False
            if [x, y + 1, 0] in answer and not check_possible(temp, [x, y + 1, 0, 1]) : # 위 기둥 확인
                return False
            return True
        else :  #보 삭제시
            if y == 0 :
                return True
            if [x + 1, y, 0] in answer and not check_possible(temp, [x + 1, y, 0, 1]) : # 오른쪽 기둥 확인
                return False
            if [x, y, 0] in answer and not check_possible(temp, [x, y, 0, 1]) : # 오른쪽 기둥 확인
                return False
            if [x - 1, y, 1] in answer and not check_possible(temp, [x - 1, y, 1, 1]) : # 왼쪽 보 확인
                return False
            if [x + 1, y, 1] in answer and not check_possible(temp, [x + 1, y, 1, 1]) : # 오른쪽 보 확인
                return False
            return True


def solution(n, build_frame):
    answer = []
    for temp in build_frame :
        # print(answer)
        # print(check_possible(answer, temp), temp, answer)
        if not check_possible(answer, temp) :
            continue
        b = temp.pop()
        if b == 1 :
            answer.append(temp)
        else :
            answer.remove(temp)

    answer = sorted(answer, key = lambda x : (x[0], x[1], x[2]))
    return answer

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(5, build_frame)
