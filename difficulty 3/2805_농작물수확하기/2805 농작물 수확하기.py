import sys
sys.stdin = open('농작물 수확하기.txt','r')

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    M = [list(map(int, input())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            h = N//2
            if abs(h-r) + abs(h-c) <= h:
                result += M[r][c]
    print('#{} {}'.format(test_case, result))