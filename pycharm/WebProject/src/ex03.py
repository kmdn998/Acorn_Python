# pip instlal flask
###############
# 요청과 응답
# ---------
# GET
# POST
###############
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # 파일 전송

# http://192.168.0.32:5000/profile/   #url 방식
@app.route('/profile/') # get 방식
def get_profile():
    return render_template('profile.html') # 파일 전송

# listening: 누군가가 서버에 접속 가능한 상태
if __name__=='__main__':
    app.run(debug=True) # 서버를 만들고 인터넷에서 접속할 수 있도록
