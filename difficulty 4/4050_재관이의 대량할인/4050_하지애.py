import sys
sys.stdin = open("input_4050.txt","r")


t = int(input())
for tc in range(1,t+1):
    n=int(input())
    lst = sorted(list(map(int,input().split())), reverse=True)

    sub_lst = []
    if len(lst)>= 3:
        for i in range(2,len(lst),3):
            sub_lst.append(lst[i])

    result = sum(lst) - sum(sub_lst)

    print('#{} {}'.format(tc,result))