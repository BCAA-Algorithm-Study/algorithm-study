from collections import Counter

nums = int(input())
for i in range(nums) :
    A, B = input().split()
    A_cnt = Counter(A)
    B_cnt = Counter(B)
    if A_cnt != B_cnt :
        print(-1)
        continue

    A_idx_a = [i for i, a in enumerate(A) if a == 'a']
    B_idx_a = [i for i, a in enumerate(B) if a == 'a']
    diff = [abs(a - b) for a, b in zip(A_idx_a, B_idx_a)]
    print(sum(diff))
