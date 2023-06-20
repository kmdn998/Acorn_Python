import wx

class MainForm(wx.Frame):
    def __init__(self, title=None, size=None, pos=None):
        super().__init__(None, title=title, size=size, pos=pos)
        self.ui()
        self.Show(True)

    def ui(self):
        self.panel= wx.Panel(self)

        wx.StaticText(self.panel, label= '********기타 컴포넌트*********', pos=(20,50))

    # Text Control
        wx.StaticText(self.panel, label='너의 이름은', pos=(20,70))
        self.txtName= wx.TextCtrl(self.panel,pos=(100,70))
        # self.Bind(wx.EVT_TEXT, self.onText, self.txtName)
        # self.txtName.Bind(wx.EVT_KEY_DOWN, self.onKeyCode) # 키를 누를때. 키보드에 눌린 값을 e로 전달

    # 윈도우에서 esc눌렀을때 프로그램 종료
        self.panel.Bind(wx.EVT_CHAR_HOOK, self.onKeyCode) # hook: 이벤트 뺏어오기


    # CheckBox
        self.chk= wx.CheckBox(self.panel, label='결혼여부', pos=(20, 120))
        self.Bind(wx.EVT_CHECKBOX, self.onCheck, self.chk)

    # RadioBox
        cboData= 'Red','Yellow','Blue'
        self.radio= wx.RadioBox(self.panel, label='좋아하는 색상은?', pos=(20,180),
                                choices=cboData)
        self.Bind(wx.EVT_RADIOBOX, self.onRadio)
    # ComboBox
        self.combo= wx.ComboBox(self.panel, pos=(20,260), choices=cboData)
        self.combo.Bind(wx.EVT_COMBOBOX, self.onCombo)

    # 결과값 확인. 고정아님
        self.txtShow = wx.TextCtrl(self.panel, pos=(20, 400), size=(320, 150), style=wx.TE_MULTILINE | wx.TE_READONLY)

    # txtName에 입력되는 것 자체가 이벤트 소스. 키보드 입력이 이벤트 클래스.
    def onText(self,e):
        # self.txtShow.AppendText('TextCtrl에 이벤트 발생: {}\n'.format(self.txtName.GetValue()))
        self.txtShow.AppendText('TextCtrl에 이벤트 발생: {}\n'.format(chr(e.GetKeyCode())))

    def onKeyCode(self,e):
        # self.txtShow.AppendText('TextCtrl에 이벤트 발생: {}\n'.format(chr(e.GetKeyCode()))
        if e.GetKeyCode()==wx.WXK_ESCAPE:
            self.Close(True)
        elif e.GetKeyCode()==wx.WXK_RETURN:
            self.txtShow.AppendText('TextCtrl에 이벤트 발생: {}\n'.format(self.txtName.GetValue()))
        e.Skip() # 키보드 이벤트를 스킵하고 onText에 넘겨줌

    def onCheck(self, e):
        self.txtShow.AppendText('CheckBox에 이벤트 발생: {}\n'.format(e.IsChecked()))

    def onRadio(self, e):
        self.txtShow.AppendText('RadioBox에 이벤트 발생: {},{}\n'.format(e.GetString(), e.GetInt()))

    def onCombo(self, e):
        self.txtShow.AppendText('ComboBox에 이벤트 발생: {}, {}\n'.format(e.GetString(), e.GetInt()))

if __name__ == '__main__':
    app = wx.App()  # 윈도우 프로그래밍 메모리 생성
    MainForm(title='여러가지 컨트롤', size=(400, 600), pos=(1300,100))  # parent 윈도우가 없음
    app.MainLoop()  # 계속 실행