import sys
sys.stdin = open("input_6019.txt","r")

#swea D3 6019 기차 사이의 파리

# 전체 250, A:10, B:15, 파리 :20
# d: 두 기차 전면부 사이의 거리, a: a 기차 속력, b : b 기차 속력, f : 파리 속력

t = int(input())
for tc in range(1, t+1):
    lst = list(map(int, input().split()))
    t = lst[0]/(lst[1] +lst[2])
    result = lst[3]*t
    print('#{} {:.6f}'.format(tc,result))
