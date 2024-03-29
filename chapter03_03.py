# Chapter03-03
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[0] + d[1] + d[1])
print('d - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print()

# Identify(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print(c)
del c[2]
print(c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3))
a.insert(2, 7)
print('a - ', a)
# del a[6]
# print('a - ', a)

a.remove(6)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count('사과'))

ex = [8,9]
a.extend(ex)
print('a - ', a)

# 반목문 활용
while a:
    data = a.pop()
    print(data)