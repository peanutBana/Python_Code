# 배열 원소의 최댓값을 구해서 출력하기

from max import max_of

number = 0
x = []

while True:
    s = input(f'x[{number}]의 값을 입력하세요: ')
    if s =='End':
        break
    x.append(int(s))
    number += 1

print(f'{number}의 개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}개 입니다.')