# 문제21 : set은 어떻게 만드나요?
# 다음 중 set을 만드는 방법이 아닌 것?
x = {}
print(type(x))

# 문제22 : 배수인지 확인하기
# 다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것은?
i = 13
i % 6 == 0

# 문제23 : OX문제
# print(10/2)의 출력 결과는 5이다.
# X 5.0

# 문제24 : 대문자로 바꿔주세요!
print('mary'.upper())

# 문제25: 원의 넓이를 구하세요.
# 원의 넓이는 반지름의 길이 x 반지름의 길이 x 3.14로 구할 수 있습니다.
# 함수를 사용하여 원의 넓이를 구하는 코드를 작성해봅시다.
# 입력을 반지름의 길이로 정수 n이 주어지면 원의 넓이를 반환하는 함수를 만들어 주세요.


def get_elipse_width(x):
    return x * x * 3.14


print(get_elipse_width(7))

# 문제26: 행성 문제2
# 우리 태양계를 이루는 행성은 수성,금성,지구,화성,목성,토성,천왕성,해왕성이 있습니다.
# 이 행성들의 영어 이름은 Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune
# 이 행성들의 영어 이름을 반환하는 프로그램을 만들어 주세요.
# 행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램을 만들어 주세요.

# solar_system = {'수성': 'Mercury', '금성': 'Venus', '지구': 'Earth', '화성': 'Mars',
#                 '목성': 'Jupiter', '토성': 'Saturn', '천왕성': 'Uranus', '해왕성': 'Neptune'}

# planet = input('행성의 한글 이름을 입력 : ')

# print(solar_system.get(planet))

# 문제27: 딕셔너리 만들기
# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고, 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어입니다.
# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.

# student_name = input('학생의 이름을 공백으로 구분하여 입력 : ').split(' ')
# student_score = input('학생의 수학 점수를 공백으로 구분하여 입력 : ').split(' ')

# print(student_name, student_score)

# print(type(zip(student_name, student_score)),
#       dict(zip(student_name, student_score)))

# 문제28: 2-gram
# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다.
# 예를 들어 'Python'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다.
# Py yt th ho on

a = input('문자열을 입력하세요. : ')

for idx, i in enumerate(a):
    if idx + 1 < len(a):
        print(i + a[idx + 1])

# 문제29: 대문자만 지나가세요
# 진구는 영어 확원 아르바이트를 하고 있습니다. 반 아이들은 알파벳을 공부하는 학생들인데 오늘은 대문자 쓰기 시험을 봤습니다.
# 알파벳 하나만을 입력하고 그 알파벳이 대문자이면 YES를 아니면 NO를 출력하는 프로그램을 만들어주세요

alphabet = input('알파벳을 입력하세요. : ')

if alphabet.isupper():
    print('YES')
else:
    print('NO')

# 문제30: 문자열 속 문자 찾기
# 문자 pineapple에는 apple이라는 문자가 숨어 있습니다. 원범이는 이렇듯 문자열 속에 숨어 있는 문자를 찾아보려고 합니다.
# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요

string = input('문자열을 입력하세요.')
char = input('찾을 문자를 입력하세요.')

print(string.find(char))
