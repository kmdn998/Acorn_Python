#고객 관리를 DB에서

import pymysql


class Manage:
    id=0
    def __init__(self, table):
        # file = open('고객관리v2.txt', 'r', encoding='utf8')
        # self.clist= [i.replace('\n', '') for i in file.readlines()]
        # file.close()

        config = {'host': '127.0.0.1', 'user': 'root', 'password': '1111', 'database': 'testdb'}
        self.conn = pymysql.connect(**config)
        self.cur= self.conn.cursor()
        self.table= table
        self.cur.execute('show tables;')
        if {self.table} not in self.cur:
            self.cur.execute(f'create table if not exists {self.table}(id int, name varchar(10));')
            self.conn.commit()

        print('1. 친구 리스트 출력')
        print('2. 친구 추가')
        print('3. 친구 삭제')
        print('4. 이름 변경')
        print('9. 종료')

    def show(self):
        # print(self.clist)
        q=f'select * from {self.table}'
        self.cur.execute(q)
        for i in self.cur:
            print(i)
        # self.conn.commit()

    def append(self):
        Manage.id+= 1
        name = input('이름을 입력: ')
        # self.clist.append(name)
        q= f'insert into {self.table} values({Manage.id},"{name}")'
        self.cur.execute(q)
        self.conn.commit()
        self.show()


    def delete(self):
        name = input('삭제할 이름 입력: ')
        # self.clist.remove(name)
        q= f'delete from {self.table} where name="{name}"'
        self.cur.execute(q)
        self.show()

    def change(self):
        name = input('변경할 이름 선택: ')
        newname = input('변경하고 싶은 이름 입력: ')
        # self.clist[self.clist.index(name)] = newname
        q=f'update {self.table} set name="{newname}" where name="{name}"'
        self.cur.execute(q)
        self.conn.commit()
        self.show()

    def finish(self):
        print('종료')
        # file = open('고객관리v2.txt', 'w', encoding='utf8')
        # for i in self.clist:
        #     file.write(i + '\n')
        self.show()
        self.conn.close()

    def run(self):
        while True:
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

CMS= Manage('NewJeans')
CMS.run()
