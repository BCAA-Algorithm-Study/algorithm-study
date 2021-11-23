'''
문제 설명
당신에게 학생들의 이름, 거주지역 좌표, 그리고 학점이 주어집니다. 다음의 우선순위에 따라 학생들에게 기숙사 배정순위를 부여해주세요.

학점의 앞자리가 높을수록 배정순위가 높습니다.
예를 들어, 학점이 3.9인 학생과 4.1인 학생 중에서는 4.1이 배정순위가 더 높습니다.
하지만 학점이 3.9인 학생과 3.7인 학생은 학점에서 순위가 갈리지 않고 다른 기준에서 갈리게 됩니다.
학점의 앞자리가 동일한 학생들끼리는, 학교에서부터 거주지역까지의 직선거리가 더 먼 학생이 배정순위가 더 높습니다. 학교의 좌표는 (0, 0)입니다.
예를 들어, (2, 3)에 사는 학생보다 (1, 4)에 사는 학생의 배정순위가 더 높습니다.
학점의 앞자리, 학교와 거주지역 사이의 거리가 둘 다 동일한 학생들끼리는 이름이 사전 순으로 더 빠를수록 배정순위가 더 높습니다.
예를 들어, "azad"의 배정순위가 "daza"의 배정순위 보다 더 높습니다.
가장 배정순위가 높은 사람의 순위는 1이고, 그 뒤로 2, 3, 4,... 순위를 배정받습니다.

학생들의 이름이 담긴 문자열 배열 names, 거주지역의 좌표가 담긴 2차원 정수 배열 homes, 그리고 학점이 담긴 실수 배열 grades가 매개변수로 주어집니다. 각 학생별로 받을 배정순위를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한 사항
names의 길이는 1 이상 100,000 이하입니다.
names[i] 는 i+1번째 학생의 이름을 의미합니다.
names의 각 원소는 영어 소문자로 이루어져 있으며, 길이는 1 이상 30 이하입니다.
동명이인은 존재하지 않습니다.
homes의 길이는 names의 길이와 같습니다.
homes[i] 는 i+1번째 학생의 거주지역 좌표를 의미합니다.
homes의 각 원소는 [x, y] 2개의 정수로 이루어져 있으며, 이는 해당 학생의 거주지역 좌표를 의미합니다.
x, y는 -10,000 이상 10,000 이하의 정수입니다.
같은 좌표에 사는 학생들이 여러 명 있을 수도 있습니다.
grades의 길이는 names의 길이와 같습니다.
grades[i] 는 i+1번째 학생의 학점을 의미합니다.
grades의 각 원소는 1.0 이상 4.5 이하의 실수이며, 소수점 아래 자리 수는 최대 2자리입니다.
입출력 예
names	homes	grades	result
["azad","andy","louis","will","edward"]	[[3,4],[-1,5],[-4,4],[3,4],[-5,0]]	[4.19, 3.77, 4.41, 3.65, 3.58]	[2,3,1,5,4]
["clanguage","csharp","java","python"]	[[3,-3],[-2,7],[-1,-1],[5,4]]	[1.27, 4.31, 4.26, 3.99]	[4,1,2,3]
["zzzzzzzzzz"]	[[9999,-9999]]	[1.0]	[1]
입출력 예 설명
입출력 예 #1

학생들에게 주어진 기준에 따라 순위를 배정하면 다음과 같습니다.
학점	학점 앞자리	거주 지역	학교까지의 거리의 제곱	이름	순위
4.41	4	(-4, 4)	32	louis	1
4.19	4	(3, 4)	25	azad	2
3.77	3	(-1, 5)	26	andy	3
3.58	3	(-5, 0)	25	edward	4
3.65	3	(3, 4)	25	will	5
louis와 azad가 학점의 앞자리가 4로 가장 높으므로, 두 사람이 1~2순위를 나눠갖습니다.
louis가 학교에서 더 먼 곳에 살고 있으므로, louis가 1순위, azad가 2순위를 갖습니다.
andy, edward, will이 학점의 앞자리가 3이므로, 세 사람이 3~5순위를 나눠갖습니다.
andy가 학교에서 가장 먼 곳에 살고 있으므로, andy가 3순위입니다.
edward와 will은 학교에서부터 동일한 거리에서 살고 있으므로, 이름을 비교하여 사전 순서로 앞인 edward가 4순위를, 뒤인 will이 5순위를 갖습니다.
입출력 예 #2

학생들에게 주어진 기준에 따라 순위를 배정하면 다음과 같습니다.
학점	학점 앞자리	거주 지역	학교까지의 거리의 제곱	이름	순위
4.31	4	(-2, 7)	53	csharp	1
4.26	4	(-1, -1)	2	java	2
3.99	3	(5, 4)	41	python	3
1.27	1	(3, -3)	18	clanguage	4
입출력 예 #3

이 예시에서는 학생의 수가 1명이므로, 그 학생은 항상 1순위입니다.
solution.go
1
func solution(names []string, homes [][]int, grades []float64) []int {
2
    return []int{}
3
}
실행 결과
실행 결과가 여기에 표시됩니다.
'''

def solution(names, homes, grades):
    grades_int = [int(x) for x in grades]
    distances = [x**2 + y**2 for x, y in homes]
    students = [(i, grades_int[i], distances[i], names[i]) for i in range(len(grades_int))]
    students = sorted(students, key = lambda x : (x[1], x[2]), reverse = True)
    sorted_names = sorted(names)
    rank = []

    for i in range(len(names) - 1) :
        if students[i][1] == students[i + 1][1] and students[i][2] == students[i + 1][2] :
            if sorted_names.index(students[i][3]) <= sorted_names.index(students[i + 1][3]) :
                rank.append(students[i][0])
                continue
            else :
                students[i], students[i + 1] = students[i + 1], students[i]
                rank.append(students[i][0])
                continue
        rank.append(students[i][0])
    rank.append(students[-1][0])

    rank = sorted(enumerate(rank), key = lambda x : x[1])
    answer = [r + 1 for r, idx in rank]
    return answer

names = ["azad","andy","louis","will","edward"]
homes = [[3,4],[-1,5],[-4,4],[3,4],[-5,0]]
grades = [4.19, 3.77, 4.41, 3.65, 3.58]

solution(names, homes, grades)