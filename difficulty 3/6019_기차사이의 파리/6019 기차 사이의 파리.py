import sys
sys.stdin = open('기차 사이의 파리.txt','r')

T = int(input())

for tc in range(T):
    d, a, b, f = map(int, input().split())
    time = d / (a + b)
    dist = time * f

    print('#{} {}'.format(tc+1,dist))