import sys
sys.stdin = open('시각 덧셈.txt','r')

T = int(input())
for tc in range(1, T+1):

    h1, m1, h2, m2 = map(int, input().split())

    hour = h1+h2
    if hour > 12:
        hour -= 12

    minutes = m1+m2

    if minutes > 60:
        minutes -= 60
        hour += 1

    print('#{} {} {}'.format(tc, hour, minutes))