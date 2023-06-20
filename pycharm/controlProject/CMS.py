print('test')

custom_list = []

while True:
    print('''
    친구 관리 프로그램
    ====================

    1.친구 리스트 출력
    2.친구 추가
    3.친구 삭제
    4.이름 변경
    9.종료
    ''')

    no = input('메뉴를 선택: ')

    if no == '9':  # case문으로 처리 가능할듯?
        break

    if no == '2':
        custom_list.append(input('추가할 이름을 입력: '))

    if no == '1':
        print('고객 리스트:', custom_list)

    if no == '3':
        custom_list.remove(input('삭제할 이름: '))

    if no == '4':
        name= input('변경할 이름 입력: ')
        for i in range(len(custom_list)):  # 리스트 개수만큼 반복. i= 인덱스
            if custom_list[i] == name:
                custom_list[i] = input('변경하고 싶은 이름 입력: ')
                break
#       i= custom_list.index(input('변경할 이름 입력: '))
#       custom_list[i]= input('변경하고 싶은 이름 입력: ')