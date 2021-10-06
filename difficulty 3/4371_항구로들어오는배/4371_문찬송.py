# SWEA 4371 항구에 들어오는 배

import sys
sys.stdin = open("4371.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    funDay = []
    for n in range(N):
        funDay.append(int(input())) # 즐거운 날을 리스트로 입력받는다

    funLst = []
    for i in range(1, len(funDay)):
        funLst.append(funDay[i] - 1)    # 0번 인덱스를 제외한 나머지 요소에서 1을 빼서 차이값만큼의 리스트로 재생성

    funSet = set(funLst)    # cpLst의 요소를 가진 set을 생성한다

    for c in funLst: # 리스트의 요소 기준으로 반복
        funSet -= set(range(c*2, funLst[-1]+1, c))     # c의 2의 배수부터 리스트의 가장 큰수까지 중에서 c의 배수를 요소로 하는 set을 생성하여
                                                       # 기존에 생성한 funSet에서 빼준다(차집합???)
                                                       # 리스트와 달리 기존 set에 없는 요소가 있어도 오류가 나지 않고, 동일한 요소만 뺀다(삭제)..(차집합???)

    print(f'#{tc} {len(funSet)}')  # funSet에 남은 요소의 길이를 반환한다(빼주지 않은 요소는 2(이상)의배수에 해당되지 않는, 주기에 해당하는 요소만 남아있으므로)
                                                                   # (해당 주기를 가진 배의 대수 == funSet에 남은 요소의 개수)를 반환