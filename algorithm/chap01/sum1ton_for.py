# 1부터 n까지 정수의 합 구하기

n = int(input('n의 값 입력하시오 : '))

sum = 0

for i in range(1,n+1):
    
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')