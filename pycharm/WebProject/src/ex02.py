# Flask: Micro FrameWork. 파이썬 프로그래밍을 웹서버로 인터넷에 띄울 수 있도록.
# pip install flask

#######
# 라우터
#######
from flask import Flask, url_for
# url_for: 어떤 요청이 들어왔는지 알아내는 함수

app= Flask(__name__)

@app.route('/') # 함수의 확장. 서버에 접속했을 때. 라우터
def index(): # View 함수
    return 'ehfskanf ancla'

# http://192.168.0.32:5000/hello
@app.route('/hello/')
def hello():
    return '<h2> 쑥갓 </h2>'

# http://192.168.0.32:5000/profile/scott
@app.route('/profile/<username>')
def get_profile(username):
    return f'<h2>당신의 이름은 {username}입니다</h2>'

# http://192.168.0.32:5000/message/100
@app.route('/message/<score>')
def get_message(score):
    return f'<h2>당신의 점수는 {score+10}점입니다</h2>'

# listening: 누군가가 서버에 접속 가능한 상태
# 클라이언트 -> 인터넷 -> 서버(라우터)
if __name__=='__main__':
    # app.run(host= '0.0.0.0', debug=True, port=80) # 서버를 만들고 인터넷에서 접속할 수 있도록
    with app.test_request_context(): # 개발자용. 서버 콘솔창에서 결과 확인
        print(url_for('hello'))
        print(url_for('get_profile', username='hong'))
        print(url_for('get_message', score= 100))