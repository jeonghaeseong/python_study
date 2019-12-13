# 문제31: 파이썬 자료형의 복잡도
# 다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌것은?
# 1. l[i]
# 2. l.append(5)
# 3. l[a:b]
# 4. l.pop()
# 5. l.clear()
# 3번?

# 문제32: 문자열 만들기
# 취업 준비생인 원영이는 자기소개서를 쓰고 있습니다. 열심히 자기소개서를 작성하던 도중 원영이는 자기가 지금까지 단어를 얼마나 적었는지 궁금하게 됩니다.
# 원영이를 위해 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램을 작성해주세요.

# print(len(input('문자열을 입력하세요. : ').split(' ')))

# 문제33: 거꾸로 출력하기
# 한 줄에 여러개의 숫자가 입력되면, 역순으로 그 숫자들을 하나씩 출력하는 프로그램을 작성하시오.

# print(list(reversed(input('숫자를 입력하세요.').split(' '))))

# 문제34: sort 구현하기
# 민주는 체육부장으로 체육시간이 되면 반 친구들이 제대로 키 순서대로 모였는지를 확인해야 한다.
# 그런데 요즘 민주는 그것이 너무 번거롭게 느껴져 한 번에 확인하고 싶어한다.
# 민주를 위해 키가 주어지면 순서대로 제대로 섰는지를 확인하는 프로그램을 작성해보자.

# user_input = input()
# l = list(user_input.split())
# l = [int(i) for i in l]

# print(id(l), id(sorted(l)))

# if l != sorted(l):
#     print('NO')
# else:
#     print('YES')

# print( [1, 2, 3] == [1, 2, 3, 4] )

# 문제35: Factory 함수 사용하기
# 2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수를 만들려고 합니다.

def one(n):
    def two(m):
        return m ** n
    return two

a = one(2)
b = one(3)
c = one(4)

print(a(10))
print(b(10))
print(c(10))

# 문제36: 구구단 출력
# 1-9까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한 줄에 출력하는 프로그램을 작성하세요.

gugudan = int(input())

for i in range(1, 10):
    print(gugudan * i, end=' ')

# 문제37: count 사용하기
# 새 학기를 맞아 은비네 반은 반장 선거를 하기로 했습니다.
# 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 하였습니다.

l = user_input = input().split()
count = 0

for i in range(1, len(l)):
    if l.count(l[i - 1]) < l.count(l[i]):
        count = i
