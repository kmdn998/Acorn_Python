#클래스화

class Manage:
    def __init__(self):
        file = open('고객관리v2.txt', 'r', encoding='utf8')
        self.clist= [i.replace('\n', '') for i in file.readlines()]
        file.close()

        # print('1. 친구 리스트 출력 = show()')
        # print('2. 친구 추가 = append(name)')
        # print('3. 친구 삭제 = remove(name)')
        # print('4. 이름 변경 = change(oldname, newname)')
        # print('9. 종료 = finish()')

    def show(self):
        print(self.clist)

    def append(self):
        name = input('이름을 선택: ')
        self.clist.append(name)
        self.show()

    def delete(self):
        name = input('삭제할 이름 입력: ')
        self.clist.remove(name)
        self.show()

    def change(self):
        name = input('변경할 이름 선택: ')
        newname = input('변경하고 싶은 이름 입력: ')
        self.clist[self.clist.index(name)] = newname
        self.show()

    def finish(self):
        print('종료')
        file = open('고객관리v2.txt', 'w', encoding='utf8')
        for i in self.clist:
            file.write(i + '\n')
        self.show()

    def run(self):
        while True:
            print('1. 친구 리스트 출력')
            print('2. 친구 추가')
            print('3. 친구 삭제')
            print('4. 이름 변경')
            print('9. 종료')
            num = int(input('메뉴를 선택: '))

            if num == 1:
                self.show()
            if num == 2:
                self.append()
            if num == 3:
                self.delete()
            if num == 4:
                self.change()
            if num == 9:
                self.finish()
                break
            print('------------------')

CMS= Manage()
CMS.run()
## 클래스는 꼭 함수와 변수로 이뤄져야하나? 그냥 코드는 X?