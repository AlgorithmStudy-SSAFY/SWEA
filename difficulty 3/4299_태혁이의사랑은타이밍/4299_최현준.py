import sys
sys.stdin = open('태혁이의 사랑은 타이밍.txt','r')

for t in range(int(input())):
    d, h, m = map(int, input().split())
    a = [11, 11, 11]
    result = 0
    if d - a[0] < 0:
        result = -1
    elif a[0] == d:
        if h - a[1] < 0:
            result = -1
        else:
            if m - a[2] < 0:
                result = -1
            else:
                result += (d-a[0]) * 60 * 24
                result += (h-a[1]) * 60
                result += (m-a[2])
    else:
        result += (d-a[0]) * 60 * 24
        result += (h-a[1]) * 60
        result += (m-a[2])
    print(f"#{t+1} {result}")
