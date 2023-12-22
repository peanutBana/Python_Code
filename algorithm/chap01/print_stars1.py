n =  int(input("몇개 출력할까 : "))
w =  int(input("몇개마다 줄바꿈 할까 : "))

for i in range(n):
    print('*', end='')
    if i%w == w-1:
        print()

if n%w:
    print()


