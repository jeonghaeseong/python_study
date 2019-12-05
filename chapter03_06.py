# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서x, 중복x, 수정o, 삭제o)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0])

# 리스트변환
l = list(c)
l2 = list(e)

print('l - ', l)
print('l - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 ', s1 & s2)
print('s1 & s2 ', s1.intersection(s2))

print('s1 | s2 ', s1 | s2)
print('s1 | s2 ', s1.union(s2))

print('s1 - s2 ', s1 - s2)
print('s1 - s2 ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 ', s1.isdisjoint(s2))

# 부분 집합 확인
print(s1.issubset(s2))
print(s2.issuperset(s1))

# 추가 & 제거
s1 = set([6, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)
s1.remove(6)
print('s1 - ', s1)
s1.discard(3)
print('s1 - ', s1)






