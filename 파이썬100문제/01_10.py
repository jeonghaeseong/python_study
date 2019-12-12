# 문제1 : 리스트의 삭제

nums = [100, 200, 300, 400, 500]

print(nums)

# nums.remove(400)
# nums.remove(500)

nums = nums[:3]

print(nums)

# 문제2 : 리스트의 내장함수
# 200, 100, 10000, 300

l = [200, 100, 300]
l.insert(2, 10000)
print(l)

# 문제3 : 변수의 타입
l = [100, 200, 300]
print(type(l))

# 문제4 : 변수의 타입2
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은?
a = 'p'
print(type(a))

# 문제5 : for문 계산

a = 10
b = 2
for i in range(1, 5, 2): # 1 3
    print(i)
    a += i

print(a+b)

# 문제6 : False
# 다음은 파이썬 문법 중에서 False로 취급하는 것들 입니다.
# 앗, False로 취급하지 않는 것이 하나 있네요! True를 찾아주세요.

print(type(None))

if None:
    print('False')
else:
    print('True')

# 문제7 : 변수명
# 다음 중 변수명으로 사용할 수 없는 것 2개를 고르시오.

# 1) age
# 2) a
# 3) as
# 4) _age
# 5) 1age

# 정답 : 3) as

# 문제8 : 딕셔너리 키 이름 중복
# 딕셔너리를 다음과 같이 만들었다.
# 출력값을 입력하시오(출력값은 공백을 넣치 않습니다.)

d = { 'height':100, 'weight': 70, 'weight': 84, 'temparture': 36, 'eyesight': 1 }
print(d['weight'])
# 84

# 문제9 : sep과 end를 활용한 출력방법
# 다음 소스 코드를 환성하여 날짜와 시간을 출력하시오.
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# 문제10 : 별 찍기
# 크리스마스 날,은비는 친구들과 함께 파티를 하기로 했습니다. 그런데 크리스마스 트리를 사는것을 깜빡하고 말았습니다.
# 온 가게를 돌아다녀 봤지만 크리스마스 트리는 모두 품절이었습니다.
# 하는 수 없이 은비는 프로그래밍으로 트리를 만드리고 합니다.

count = int(input('입력하세요 : '))

for i in range(count):
    for j in range(0, count * 2 - 1):
        if j in range( count - (i + 1), count + i ):
            print('*', end='')
        else:
            print(' ', end='')
    print()