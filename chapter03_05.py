# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {
    'name': 'Kim',
    'phone': '01033337777',
    'birth': '870514'
}

b = {
    0: 'Hello Python'
}

c = {
    'arr': [1, 2, 3, 4]
}

d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
# print('a - ', a['name1']) # 존재x -> 에러발생
print('a - ', a.get('name1')) # 존재x - > None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['name'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# dict_keys, dict_values, dict_items : 반복
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', type(a.keys()))

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print('a - ', a.values())
print('b - ', b.values())

print('a - ', a.items())
print('b - ', b.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('a - ', 'birth2' in a)

print()

# 수정
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a - ', a)