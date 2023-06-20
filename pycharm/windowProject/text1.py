import wx

app= wx.App() # 윈도우 프로그래밍 메모리 생성
wx.Frame(None, title='윈도우 창').Show(True) # parent 윈도우가 없음
app.MainLoop() # 계속 실행
