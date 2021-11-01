import sys
sys.stdin = open('중간 평균값 구하기.txt','r')

T = int(input())
for tc in range(1, T+1):
    nums = sorted(list(map(int, input().split())))

    sumV = sum(nums[1:9])
    avg = round(sumV/8)

    print('#{} {}'.format(tc,avg))