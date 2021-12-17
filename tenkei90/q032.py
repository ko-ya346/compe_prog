from itertools import permutations

n = int(input())
time = []

for _ in range(n):
    a = list(map(int, input().split()))
    time.append(a)

orders = ["".join([str(aa) for aa in a]) for a in list(permutations(range(n), n))]
# orders = list(permutations(range(n), n))
possible_orders = []

m = int(input())
pairs = []
for _ in range(m):
    x, y = map(lambda x: str(int(x) - 1), input().split())
    pairs.append(x + y)
    pairs.append(y + x)


ans = float("inf")
for order in orders:
    flag = 1
    for pair in pairs:
        if pair in order:
            flag = 0
            break
    if flag == 0:
        continue
    cost = 0
    for i, s in enumerate(order):
        cost += time[int(s)][i]
    #    print(f"cost: {cost}")
    ans = min(ans, cost)

# print(orders)
# print(possible_orders)

if ans == float("inf"):
    print(-1)
else:

    print(ans)
