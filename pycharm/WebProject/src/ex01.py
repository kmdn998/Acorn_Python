# pip instlal flask

from flask import Flask

app= Flask(__name__)

@app.route('/') # 함수의 확장. 서버에 접속했을 때.
def index():
    return '<h1>hello</h1>'


# listening: 누군가가 서버에 접속 가능한 상태
if __name__=='__main__':
    app.run(host= '0.0.0.0') # 서버를 만들고 인터넷에서 접속할 수 있도록

