from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))

right = 0
ans = 0
cnt = 0
kind = defaultdict(int)
for left in range(n - 1):
    #    print("s", s)
    #    print(f"left: {left}")
    while right < n and cnt <= k:
        kind[A[right]] += 1
        if kind[A[right]] == 1:
            cnt += 1

        #        print(f"right: {right}")
        right += 1
    #    print(f"right - left: {right - left}")
    if cnt <= k:
        right += 1
    ans = max(ans, right - left - 1)
    kind[A[left]] -= 1
    if kind[A[left]] == 0:
        cnt -= 1
print(ans)
