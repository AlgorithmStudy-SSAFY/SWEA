import sys
sys.stdin = open(f'input_2805.txt','r')
# swea 2805 농작물 수확하기

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    lst = [list(input()) for _ in range(n)] #[['1', '4', '0', '5', '4'], ['4', '4', '2', '5', '0']...

    mid = n//2
    start = n//2
    end = n//2
    result = 0
    for i in range(n):
        for j in range(start, end):
            sum += int(lst[i][j])
        if i < mid:  # 마름모 위쪽 -> 양옆으로 1씩 넓어짐
            start -= 1
            end += 1
        else:        # 마름모 아래쪽 -> 양옆으로 1씩 좁아짐
            start += 1
            end -= 1

    print('#{} {}'.format(tc, result))
    #print(lst)