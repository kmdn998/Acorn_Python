'''
Dialog(대화상자)
--------------
1. 종류
    (1) Built-in Dialog, Common Dialog, System Dialog
    (2) User Define Dialog

2. 실행방식
    - Modal
    - Modaless


'''

import wx
import os

class DialogForm(wx.Frame):
    def __init__(self, title=None, size=None):
        super().__init__(None, title=title, size=size)
        self.ui()

    def ui(self):
        self.CreateStatusBar()
        menubar= wx.MenuBar()
        menu= wx.Menu()

        item1= wx.MenuItem(menu, 100, 'MessageDialog', '메세지 대화상자 보이기') # 저장
        item2= wx.MenuItem(menu, 101, 'ColorDialog', '색상 대화상자 보이기')
        item3= wx.MenuItem(menu, 102, 'FileDialog', '파일 대화상자 보이기')
        item4= wx.MenuItem(menu, 103, 'LoginDialog', '로그인 대화상자 보이기')

        menu.Append(item1)
        menu.Append(item2)
        menu.Append(item3)
        menu.Append(item4)

        menubar.Append(menu, '다이얼로그') # 파일
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onMessage, id=100)  # item1
        self.Bind(wx.EVT_MENU, self.onColor, item2)  # item2
        self.Bind(wx.EVT_MENU, self.onFile, item3)
        self.Bind(wx.EVT_MENU, self.onLogin, item4)

        self.Show(True)

    def onMessage(self, e):
        self.SetStatusText('메세지 대화 상자 실행중')
        dig= wx.MessageDialog(self,'화이팅(내용)', '이경쓰(제목)', wx.OK|wx.ICON_INFORMATION)
        if dig.ShowModal() == wx.ID_OK:
            self.SetStatusText('...')

    def onColor(self, e):
        self.SetStatusText('메세지 대화 상자 실행중')
        dig= wx.ColourDialog(self) # 색상표
        dig.GetColourData().SetChooseFull(True)
        if dig.ShowModal() == wx.ID_OK:
            print(dig.GetColourData().GetColour().Get())
            color= dig.GetColourData()
            self.SetStatusText('당신이 선택한 색깔: '+str(color.GetColour().Get()))

    def onFile(self, e):
        self.SetStatusText('파일 대화 상자 실행중')
        dig= wx.FileDialog(self, '파일 대화상자', 'c:\\','파일명','*.*', style=wx.ID_OPEN) # 파일 선택창

        # dig.ShowModal()
        if dig.ShowModal() == wx.ID_OK:
            filepath= dig.GetPaths()[0]

        # self.SetStatusText('당신이 선택한 파일은 '+ filepath)
        self.SetStatusText('당신이 선택한 파일은 '+ os.path.basename(filepath))


    def onLogin(self, e):
        self.SetStatusText('로그인 대화상자 실행 중')
        dig= LoginForm('로그인 대화상자', (300,200))
        dig.ShowModal()

class LoginForm(wx.Dialog):    # subwindow
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


if __name__ == '__main__':
    app = wx.App()  # 윈도우 프로그래밍 메모리 생성
    DialogForm(title='공통 대화 상자', size=(800, 600))  # parent 윈도우가 없음
    app.MainLoop()  # 계속 실행