import sys
sys.stdin = open("input_1940.txt","r")

#swea D2 1940 가랏! RC카!
# 0 유지 1 가속 2 감속
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    s = 0  #거리
    v = 0  #속도
    for i in range(n):
        lst = list(map(int, input().split()))

        if lst[0] == 0:
            s += v
        elif lst[0] == 1:
            v += lst[1]
            s += v
        elif lst[0] == 2:
            if v < lst[1]:   #현재 속도보다 감속할 속도가 더 클 경우
                v = 0
            else:
                v -= lst[1]
                s += v


    print('#{} {}'.format(tc,s))

