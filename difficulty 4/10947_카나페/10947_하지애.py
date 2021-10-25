import sys
sys.stdin = open("input_10947.txt","r")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    lst_b = sorted(list(map(int, input().split())))
    lst_g = sorted(list(map(int, input().split())))
    result = 0
    for i in range(n):
        result += lst_b[i]*lst_g[i]
    print('#{} {}'.format(tc,result))