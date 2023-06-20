import random

class RCP:
    def playRCP(self):
        win, lose, same=0,0,0
        while True:
            me= input('"가위", "바위", "보" 중에서 하나를 입력하세요: ')
            if me in ['x','q']: 
                print(f'{same}무 {win}승 {lose}패')
                break
                
            rand= random.randint(0,2)
            if rand==0: com= '가위'
            elif rand==1: com= '바위'
            else: com= '보'
            
            if me not in ['가위', '바위', '보']: 
                print('잘못 입력하였습니다')
                continue
                
            elif me == com:
                result= 'same'
                same +=1
            else:
                if me== '가위':
                    if com=='바위': 
                        result= 'lose'
                        lose += 1
                    elif com=='보': 
                        result= 'win'
                        win +=1
                elif me=='바위':
                    if com=='가위': 
                        result= 'win'
                        win +=1
                    elif com=='보': 
                        result= 'lose'
                        lose += 1
                elif me=='보':
                    if com=='가위': 
                        result= 'lose'
                        lose += 1
                    elif com=='바위': 
                        result= 'win'
                        win +=1
            print('컴퓨터:',com)
            print('나:',me)
            print('결과:',result,'\n')

class RandomNum:
    #4. 숫자맞추기 1~100. 힌트 세분화. 총 시도 횟수
    def playRNum(self):
        ans= random.randint(1,100)
        total=0

        while True:
            num= int(input('숫자:'))
            if ans> num+20: print('MUCH higher')
            elif ans > num: print('higher')
            elif ans < num-20: print('MUCH lower')
            elif ans < num: print('lower')
            elif ans==num: 
                print('정답입니다')
                break
            total+=1
            print()
            if total >5: print(ans)
        
        print(f'총 시도 횟수:{total}')

class Games(RCP, RandomNum):
    def __init__(self):
        while True:
            pick= input('게임을 시작하시려면 "1" 또는 "2"를 입력하세요: ')
            if pick=="1": RCP.playRCP(self)
            elif pick=="2": RandomNum.playRNum(self)
            else: break
            

# t1=RCP()
# t1.playgame()
# t2=RandomNum()
# t2.playRNum()

t3=Games()