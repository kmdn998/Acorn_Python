# Menu: 고정식 메뉴(Pull Down), 이동식 메뉴(Pop up)
# MenuBar, Menu, MenuItem
import wx


class MenuForm(wx.Frame):
    def __init__(self, title=None, size=None):
        super().__init__(None, title=title, size=size)
        self.ui()

    def ui(self):
        menubar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuEdit = wx.Menu()

        menubar.Append(mnuFile, '파일')
        menubar.Append(mnuEdit, '편집')

        # wx.MenuItem(parentMenu, id, text, 도움말)
        mnuFile_new = wx.MenuItem(mnuFile, wx.ID_NEW, 'New', 'New Document')
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, 'Open', '파일 열기')
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, 'Exit', '윈도우 종료')

        mnuFile.Append(mnuFile_new)
        mnuFile.Append(mnuFile_open)
        mnuFile.AppendSeparator()
        mnuFile.Append(mnuFile_exit)

        self.SetMenuBar(menubar)

        self.txtArea= wx.TextCtrl(self, style= wx.TE_MULTILINE)

        self.CreateStatusBar() # 메뉴 도움말 표시

        self.Bind(wx.EVT_MENU, self.onExit, mnuFile_exit) # 메뉴에서 발생한 이벤트
        self.Bind(wx.EVT_MENU, self.onNew, mnuFile_new)
        self.Bind(wx.EVT_MENU, self.onOpen, mnuFile_open)



        # self.Move(50,50)
        self.Center()

    def onExit(self, e):
        self.Close(True)

    def onNew(self, e):
        self.txtArea.SetLabelText('새 문서를 선택하였습니다.')

    def onOpen(self, e):
        # filepath= 'C:\\kim\\python\\pycharm\\windowProject\\contents.txt'

        dig= wx.FileDialog(self, '파일불러오기') # 파일 선택창
        if dig.ShowModal()== wx.ID_OK:
            filepath= print(dig.GetPaths())[0]

        f= open(filepath, 'r', encoding='utf8 ')
        data= f.read()
        self.txtArea.SetLabelText(data)
        f.close()

if __name__ == '__main__':
    app = wx.App()  # 윈도우 프로그래밍 메모리 생성
    MenuForm(title='PullDown Menu', size=(800, 600)).Show(True)  # parent 윈도우가 없음
    app.MainLoop()  # 계속 실행
