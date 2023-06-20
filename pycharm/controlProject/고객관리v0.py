print('친구 관리 프로그램')
print('==========================')

nlist = []
while True:
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 이름 변경')
    print('9. 종료')
    num = int(input('메뉴를 선택: '))

    if num == 1:
        print(nlist)
    if num == 2:
        name = input('이름을 선택: ')
        nlist.append(name)
    if num == 3:
        name = input('삭제할 이름 입력: ')
        nlist.remove(name)
    if num == 4:
        name = input('변경할 이름 선택: ')
        i= nlist.index(name)
        newname = input('변경하고 싶은 이름 입력: ')
        nlist[i]= newname
    if num == 9:
        print('종료')
        break
    print('------------------')