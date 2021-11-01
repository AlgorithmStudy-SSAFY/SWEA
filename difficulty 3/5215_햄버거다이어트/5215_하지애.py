import sys
sys.stdin = open("input_5215.txt","r")

t = int(input())
for tc in range(1,t+1):
    n, l = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for i in range(1<<n):
        g_s = []
        g_c = []
        for j in range(n):
            if i & (1<<j):
                g_s.append(g[j][0])
                g_c.append(g[j][1])
        if sum(g_c) <= l:
            maxG = sum(g_s)
            if maxG >= maxV:
                maxV = maxG

    print('#{} {}'.format(tc, maxV))


#부분집합(시간초과)
    # maxV = 0
    # for i in range(1<<n):
    #     g_s = []
    #     g_c = []
    #     for j in range(n):
    #         if i & (1<<j):
    #             g_s.append(g[j][0])
    #             g_c.append(g[j][1])
    #             if sum(g_c) <= l:
    #                 maxG = sum(g_s)
    #                 if maxG >= maxV:
    #                     maxV = maxG
