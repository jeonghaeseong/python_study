# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True))
print(type(False))

# 예1
if True:
    print('Good')

if False:
    print('Bad')

# 예2
if False:
    print('Bad')
else:
    print('Good')

# 관계 연산자
# >, >=, <, <=, --, !=

x = 15
y = 10

# 양변이 같을 경우 참
print(x == y)

# 양변이 다를 경우 참
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 오른쪽이 클 때 참
print(x < y)

city = ""

if city:
    print('You are in:', city)
else:
    print('plz enter tour city')