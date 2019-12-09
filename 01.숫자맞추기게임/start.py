import random
import os

def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input('몇일까요?'))
            return user_input
        except:
            continue

chance = 10
count = 0

number = random.randint(1, 99)
os.system('cls')
print('1부터 99까지의 숫자를 10번 안에 맞춰 보세요.')

while count < chance:
    count+=1
    user_input = input_check('몇 일까요?')
    # user_input = int(input('몇일까요?'))
    if number == user_input:
        print('정답')
        break
    elif user_input < number:
        print('{} 보다 큰 숫자 입니다.'.format(user_input))
    elif user_input > number:
        print('{} 보다 작은 숫자 입니다.'.format(user_input))
    else:
        print('아닙니다.')

if user_input == number:
    print('성공! {} 이 맞습니다.'.format(number))
else:
    print('실패! 정답은 {} 입니다.'.format(number))
