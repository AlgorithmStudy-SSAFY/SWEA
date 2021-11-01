import sys
sys.stdin = open('쥬스 나누기.txt', 'r')

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())

    print('#{} '.format(tc), end='')
    for q in range(n):
        print('{}{}{}'.format(1, '/', n), end=' ')
    print()