import sys
sys.stdin = open(f'input_1984.txt','r')

t = int(input())
for tc in range(1,t+1):
    lst = list(map(int, input().split()))
    lst_min = 10000
    lst_max = 0
    for i in range(len(lst)):
        if lst[i] > lst_max:
            lst_max = lst[i]
        if lst[i] < lst_min:
            lst_min = lst[i]
    # 최소 수와 최대 수가 여러개일때는?
    lst.remove(lst_max)
    lst.remove(lst_min)
    while lst_max in lst:
        lst.remove(lst_max)
    while lst_min in lst:
        lst.remove(lst_min)

    sum = 0
    for j in range(len(lst)):
        sum += lst[j]
    result = round(sum/len(lst))
    print('#{} {}'.format(tc, result))