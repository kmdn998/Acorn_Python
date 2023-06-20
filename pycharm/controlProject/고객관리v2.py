#고객 이름, 번호, 주소 받기
#파일로 저장

#함수 실행할 때마다 파일 연결

print('고객 관리 프로그램')
print('==========================')
clist=[]
file=None

def show():
    file = open('고객관리v2.txt', 'r', encoding='utf8')
    for i in file.readlines():
        print(i)
    file.close()

def append():
    file = open('고객관리v2.txt', 'a', encoding='utf8')
    i= input('등록할 고객의 고객아이디, 이름, 번호, 주소를 입력하세요: ')
    id, name, phone, add= i.split(',')
    file.write(f'{id},{name},{phone},{add}\n')
    file.close()
    show()

def delete():
    id = input('삭제할 고객아이디 입력: ')
    file = open('고객관리v2.txt', 'r', encoding='utf8')
    lines = file.readlines()
    file.close()
    newfile = open('고객관리v2.txt', 'w', encoding='utf8')
    for i in range(len(lines)):
        f = lines[i].find(id)
        if f == -1:
            newfile.write(lines[i])
    newfile.close()
    show()

def change():
    id = input('변경할 고객아이디 선택: ')
    file = open('고객관리v2.txt', 'r', encoding='utf8')
    lines = file.readlines()
    file.close()

    newfile = open('고객관리v2.txt', 'w', encoding='utf8')
    i= input('변경할 고객아이디의 이름, 번호, 주소를 입력하세요: ')
    name, phone, add= i.split(',')
    for i in range(len(lines)):
        f = lines[i].find(id)
        if f == -1:
            newfile.write(lines[i])
        else:
            newfile.write(f'{id},{name},{phone},{add}\n')
    show()

def finish():
    print('종료')

while True:
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 이름 변경')
    print('9. 종료')
    num = int(input('메뉴를 선택: '))

    if num == 1:
        show()
    if num == 2:
        append()
    if num == 3:
        delete()
    if num == 4:
        change()
    if num == 9:
        finish()
        for i in clist:
            file.write(i+'\n')
        break
    print('------------------')
