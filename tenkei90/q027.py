from collections import defaultdict

n = int(input())
d = defaultdict(int)
rm_lst = []

for i in range(n):
    s = input()
    if d[s]:
        continue
    print(i + 1)
    d[s] = 1
