import sys
sys.stdin = open("input_5431.txt","r")
#  민석이의 과제 체크하기

t = int(input())
for tc in range(1,t+1):
    #n:수강생, k:과제 제출한 사람
    n,k = map(int, input().split())
    #과제 제출한 사람의 번호
    lst = list(map(int, input().split()))
    #전체 번호 넣어서 만들고 lst 숫자 빼주기
    total = [0] * (n)
    for i in range(1,n+1):
        total[i-1] = i
    for i in range(len(lst)):
        total.remove(lst[i])

    print('#{}'.format(tc), end=' ')
    print(*total)


    # print('#{} {}'.format(tc, " ".join(map(str,total))))