# algorithm-study
알고리즘 스터디를 위한 저장소입니다.

# Programming Language
Python

# 알고리즘 사이트
- baekjoon: https://www.acmicpc.net/
- programmers: https://programmers.co.kr/learn/challenges
- codility: https://app.codility.com/programmers/ 
- hackerrank: https://www.hackerrank.com/
- leetcode: https://leetcode.com/
- codeground: https://www.codeground.org/about
- synap: http://euler.synap.co.kr/
- topcoder: https://www.topcoder.com/
- algospot: https://algospot.com/judge/problem/list/
- swexpertacademy: https://www.swexpertacademy.com/main/main.do
- geeksforgeeks: https://www.geeksforgeeks.org/
- codeforces: http://codeforces.com

# 폴더 구조
- 폴더 구조는 다음과 같습니다.
  - 사이트 폴더 - 문제 폴더 - 본인 이니셜 폴더, README.md - 소스코드, 풀이방법 파일
```
baekjoon/
├── 1417/
| ├── README.md
│ ├── kjy
│ | ├── 1417.py
│ | ├── solution.md
│ └── ljh
│ └── chj
│ └── kec
│ └── ojs
│ └── yyh
│ └── pjy
```

  - 사이트 폴더: 누구나 사이트를 알아볼 수 있게 영어로 작성합니다.
    - 예) baekjoon, programmers, codeground
  - 문제 폴더: 숫자를 우선적으로 작성, 숫자가 없다면 영어로 작성합니다.
    - 예) 1417
  - 본인 이니셜 폴더: 해당 문제를 풀 본인의 저장 공간을 생성합니다.
  - README.MD : 해당 문제에 대한 구체적인 설명을 작성한다. main branch에서 바로 생성합니다.
    - 예) 다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있다. 다솜이는 이 기계를 이용해서 2008년 4월 9일 국회의원 선거를 조작하려고 한다...
  - 소스코드: 자신의 이니셜 혹은 아이디 뒤에 .확장자명으로 작성합니다.
    - 예) 1417.py
  - 풀이방법: 자신의 이니셜 혹은 문제번호 뒤에 solution.md 로 작성합니다.
    - 예) 1417_solution.md

# Commit Rule
- Commit Rule은 다음을 참고합니다. 
  - 브런치 생성: 자기이름(혹은 아이디)_사이트_문제번호
    - 예) kjy_baekjoon_1417를 브런치 이름으로 합니다.
  - commit message는 자유롭게 합니다.

# 파일이름.md Rule
- 각 문제별 파일이름.md Rule은 다음을 참고합니다.
  - 문제 주소, 문제 접근 방법 를 작성합니다.
  - 문제 접근 방법 은 되도록이면 구체적으로 작성합니다.

# PullRequest(PR) Rule
- PR rule은 다음을 참고합니다
  - 최소 2명이상 리뷰가 달릴 경우에 PR Merge가 가능합니다.
  - Pull request 제목 및 내용은 자유롭게 합니다.
  - Merge 버튼은 2명이상이 리뷰 comment를 남겼을 때, 마지막 리뷰어가 누르는 것으로 합니다. 단, 질문을 남겼을 경우 질문에 대한 답을 받고 Merge 해야합니다.

# 리뷰어 순서
- kec -> kjy -> ojs -> yyh -> ljh -> chj
- 편의상 이니셜로 적겠습니다. kec는 kjy와 ojs 2명을 리뷰해야합니다. kjy는 ojs와 yyh를 리뷰해야 합니다.

# 스터디 Rule
일주일에 최소 3번 이상 Commit하는 것을 규칙으로 합니다.

- 개인이 할 일
  - 이론 정리
    - 알고리즘 이론 내용을 간단히 정리합니다.
  - 문제 풀이
    - 알고리즘 문제를 푼다.
    - 각자가 해당 코드의 좋은 예제를 찾아서 분석한다.
    - 각 문제 폴더 마다 파일이름.md Rule에 맞게 작성한다.
  - 공유 및 피드백
    a. 각자가 푼 문제에 대한 코드를 브런치를 따서 github에 push한 후 pull request를 날린다.
    b. 상대방의 코드를 확인한 후 리뷰나 피드백을 작성하면 된다.
    c. 만약 리뷰나 피드백할 의견이 없을 경우 approve 기능을 사용해 승인해주면 된다.
    d. 두개 이상의 리뷰어가 approve 혹은 리뷰나 피드백을 작성하였을 경우, 해당하는 브런치를 Merge한다.
- 스터디 모임에서 할 일
    - 이론 정리 공유
    - 문제를 풀 때 발생한 리뷰 및 피드백 에 대해 논의
    - 좋은 코드에 대한 분석 공유
    - 문제 및 스터디에 대한 회고

# Commit 방법


# 참고 사이트 
https://github.com/epicarts/algorithm-study#algorithm-study
