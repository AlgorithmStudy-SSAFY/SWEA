import sys
sys.stdin = open("input_5601.txt","r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = ('1/'+str(n)+' ')*n
    print('#{} {}'.format(tc,result))