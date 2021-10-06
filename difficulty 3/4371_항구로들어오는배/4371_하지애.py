import sys
sys.stdin = open("input_4371.txt","r")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    happy = [int(input()) for i in range(n)]
    #[1, 3, 4], [1, 7, 10, 13, 19]

    lst = []
    cnt = 0
    for i in range(1,len(happy)):
        sub = happy[i] - 1
        lst.append(sub)
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[j] % lst[i] == 0:
                lst[j] = 0.1
    for i in range(len(lst)):
        if lst[i] != 0.1:
            cnt += 1


    print('#{} {}'.format(tc, cnt))