import sys
sys.stdin = open("input_5948.txt","r")

def f(n, m, k):   # n:순열의 길이, k:결정할 위치
    if n==k:
        sumV.append(sum(p))
    else:
        for i in range(m):   #주어진 숫자의 개숨나큼
            if u[i] == 0:
                u[i] = 1
                p[k] = lst[i]
                f(n, m, k+1)
                u[i] = 0

t = int(input())
for tc in range(1,t+1):
    lst = list(map(int, input().split()))
    p = [0]*3
    u = [0]*7
    sumV = []
    f(3,7,0)
    result_lst = list(set(sumV))
    result = sorted(result_lst)
    print('#{} {}'.format(tc,result[-5]))
