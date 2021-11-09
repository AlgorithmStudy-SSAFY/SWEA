import sys
sys.stdin = open('input_5948.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    numbers = list(map(int,input().split()))
    N = len(numbers)
    temp = []

    for i in range(N): # 중복되지 않게 하나씩 숫자를 뽑아서 완전탐색을 한다.
        for j in range(i+1, N):
            for k in range(j+1, N):
                temp_sum = numbers[i] + numbers[j] + numbers[k]
                if temp_sum not in temp:
                    temp.append(temp_sum)

    temp.sort(reverse=True) # 내림차순 정렬

    print(f'#{test_case} {temp[4]}')