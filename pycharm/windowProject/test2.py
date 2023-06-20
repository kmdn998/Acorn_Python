import wx


# 로그인
class LoginForm(wx.Frame):
    def __init__(self, title=None, size=None):
        super().__init__(None, title=title, size=size)
        self.ui()

    def ui(self):
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label='ID: ', pos=(5, 5))
        wx.StaticText(self.panel, label='Pass: ', pos=(5, 40))
        self.m_id = wx.TextCtrl(self.panel, pos=(50, 5), size=(200, -1))
        self.m_pw = wx.TextCtrl(self.panel, pos=(50, 40), size=(200, -1))

        btn1 = wx.Button(self.panel, pos=(5, 100), label='로그인')
        btn2 = wx.Button(self.panel, pos=(90, 100), label='종료')
        btn3 = wx.ToggleButton(self.panel, pos=(180, 100), label='토글버튼')

        btn1.id, btn2.id, btn3.id = 1, 2, 3
        # btn1.Bind(wx.EVT_BUTTON, self.onBtHandler1)
        # btn2.Bind(wx.EVT_BUTTON, self.onBtHandler2)
        # btn3.Bind(wx.EVT_TOGGLEBUTTON, self.onBtHandler3)

        self.Bind(wx.EVT_BUTTON, self.onBtHandler, btn1)
        # btn1.Bind(wx.EVT_BUTTON, self.onBtHandler)
        btn2.Bind(wx.EVT_BUTTON, self.onBtHandler)
        btn3.Bind(wx.EVT_TOGGLEBUTTON, self.onBtHandler)

    def onBtHandler(self, e):
        print(e.GetEventObject().id)
        if e.GetEventObject().id == 1:
            id = self.m_id.GetValue()  # 아이디값받아오기
            pw = self.m_pw.GetValue()

            if id == 'tiger' and pw == '1111':
                msg = '로그인 되었습니다.'
            else:
                msg = '로그인이 거부되었습니다'

            msg_dig = wx.MessageDialog(self, msg, '로그인 정보', wx.OK)
            msg_dig.ShowModal()

        if e.GetEventObject().id == 2:
            self.Close(True)
        else:
            print(e.GetEventObject().GetValue())
            if e.GetEventObject().GetValue():
                self.panel.SetBackgroundColour(wx.Colour(255, 255, 0))
                self.panel.Refresh()
            else:
                self.panel.SetBackgroundColour(wx.Colour(0, 255, 255))
                self.panel.Refresh()

    def onBtHandler1(self, e):
        # print('버튼이 눌렸다')
        id = self.m_id.GetValue()  # 아이디값받아오기
        pw = self.m_pw.GetValue()
        # print(id, pw)

        if id == 'tiger' and pw == '1111':
            msg = '로그인 되었습니다.'
        else:
            msg = '로그인이 거부되었습니다'

        msg_dig = wx.MessageDialog(self, msg, '로그인 정보', wx.OK)
        msg_dig.ShowModal()

    def onBtHandler2(self, e):
        self.Close(True)
        # self는 class 객체. 윈도우 창.

    def onBtHandler3(self, e):
        print(e.GetEventObject().GetValue())
        if e.GetEventObject().GetValue():
            self.panel.SetBackgroundColour(wx.Colour(255, 255, 0))
            self.panel.Refresh()
        else:
            self.panel.SetBackgroundColour(wx.Colour(0, 255, 255))
            self.panel.Refresh()


if __name__ == '__main__':
    app = wx.App()  # 윈도우 프로그래밍 메모리 생성
    LoginForm(title='로그인', size=(300, 200)).Show(True)  # parent 윈도우가 없음
    app.MainLoop()  # 계속 실행
