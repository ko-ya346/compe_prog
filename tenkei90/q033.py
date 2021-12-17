h, w = map(int, input().split())
if h == 1 or w == 1:
    print(h * w)
else:
    print((h // 2 + h % 2) * (w // 2 + w % 2))
