#고객 이름, 번호, 주소 받기
#파일로 저장

#처음과 마지막에만 파일 연결

print('고객 관리 프로그램')
print('==========================')
# clist=[]
def show():
    print(clist)

def append():
    name= input('이름을 선택: ')
    clist.append(name)
    show()

def delete():
    name = input('삭제할 이름 입력: ')
    clist.remove(name)
    show()

def change():
    name = input('변경할 이름 선택: ')
    newname = input('변경하고 싶은 이름 입력: ')
    clist[clist.index(name)] = newname
    show()

def finish():
    print('종료')

file = open('고객관리v2.txt', 'r', encoding='utf8')
clist= [i.replace('\n','') for i in file.readlines()]
file.close()
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
        file = open('고객관리v2.txt', 'w', encoding='utf8')
        for i in clist:
            file.write(i+'\n')
        break
    print('------------------')
