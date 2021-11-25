import bisect

a = [1, 10, 30, 100]
print(bisect.bisect_left(a, 0))
print(bisect.bisect_left(a, 5))
print(bisect.bisect_left(a, 20))
print(bisect.bisect_left(a, 101))
print(bisect.bisect_left(a, 100))
