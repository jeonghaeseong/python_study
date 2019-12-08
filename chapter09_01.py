# Chapter09-1
# 파일 읽기 쓰기

# 읽기모드 : r, 쓰기모드 :  w, 추가모드 : a, 텍스트 모드 : t, 바이너리모드 : b
# 상대경로, 절대경로

# 파일 읽기(Read)
# 예제1
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

# 속성확인
print(dir(f))
# 인코딩확인
print(f.encoding)
# 파일이름
print(f.name)
# 모드확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체읽기, read(10) : 10Byte
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(5)
    print(c)
    f.seek(0, 0)
    c = f.read(5)
    print(c)

print()

# 예제4
# readLine : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

# 예제5
# readLines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

# 파일쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python1\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# 예제3
# writelines : 리스트->파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
with open('./resource/contents2.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
