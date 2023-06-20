import sys
sys.path.append('C:\kim\python\lib')

import lib.game.sound.echo as echo
import lib.game.graphic.screen as screen

def main():
    print('에코:')
    echo.echo_test()

    print('영상:')
    screen.screen_test()

if __name__ == '__main__':               #모듈로 호출된건지, 직접 실행된건지 구분
      print('게임 시작')
      main()



print(__name__)
print(screen.__name__)