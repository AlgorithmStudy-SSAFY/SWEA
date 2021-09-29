#10912. 외로운 문자
import sys
sys.stdin = open("input_10912.txt", "r")

t = int(input())
for tc in range(1, t+1):
    word = input()
    word_s = sorted(word)
    result = []
    for i in word_s:
        if i not in result:   #리스트 안에 없으면 추가
            result.append(i)
        else:
            if result[-1] == i: #겹치면 제외
                result.pop()
            else:
                result.append(i)

    if len(result) == 0:
        print('#{} Good'.format(tc))
    else:
        print('#{}'.format(tc), "".join(result))
        # for i in result:
            #print(i,end = '')
        #print()

