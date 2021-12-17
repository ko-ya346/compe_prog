import numpy as np

T = int(input())
L, X, Y = map(int, input().split())

r = L / 2  # 半径
v_angle = 360 / (T * 60)  # 角速度


def calc_yz(t):
    angle = np.radians(v_angle * t)
    y = -r * np.sin(angle)
    z = r - r * np.cos(angle)
    return y, z


Q = int(input())
for _ in range(Q):
    e = int(input()) * 60
    y, z = calc_yz(e)
    y -= Y
    print(np.degrees(np.arctan2(z, np.sqrt(X ** 2 + y ** 2))))
