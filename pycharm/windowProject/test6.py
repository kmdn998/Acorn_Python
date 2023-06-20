import wx

class MainForm(wx.Frame):
    def __init__(self, title=None, size=None, pos=None):
        super().__init__(None, title=title, size=size, pos=pos)
        self.ui()
        self.Show(True)

    def ui(self):
        panel1= wx.Panel(self)
        panel1.SetBackgroundColour('Red')

        panel2= wx.Panel(self)
        panel2.SetBackgroundColour('Blue')

        box= wx.BoxSizer(wx.HORIZONTAL)
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(panel2, 2, wx.EXPAND)

        self.SetSizer(box)
if __name__ == '__main__':
    app = wx.App()  # 윈도우 프로그래밍 메모리 생성
    MainForm(title='Layout Manager', size=(600, 600), pos=(1300,100))  # parent 윈도우가 없음
    app.MainLoop()  # 계속 실행