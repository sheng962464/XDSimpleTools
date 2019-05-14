#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


# SimpleTools主界面
class SimpleToolsMainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SimpleToolsMainFrame, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.MenuBarInit()  # 菜单栏初始化
        self.ToolBarInit()  # 工具栏初始化
        self.StatusBarInit()  # 状态栏初始化
        self.PanelInit()  # 布局管理初始化

        # 窗口样式
        self.SetSize((600, 600))
        self.SetTitle('XDSimpleTools')
        self.Centre()
        self.Show(True)

    '''菜单栏初始化函数'''
    def MenuBarInit(self):
        self.MenuBar = wx.MenuBar()
        # 一级菜单定义
        FileMenu = wx.Menu()
        EditMenu = wx.Menu()
        HelpMenu = wx.Menu()
        # 一级菜单加入到菜单栏
        self.MenuBar.Append(FileMenu, '&文件')
        self.MenuBar.Append(EditMenu, '&编辑')
        self.MenuBar.Append(HelpMenu, '&帮助')

        # 创建子菜单项
        OpenItem = wx.MenuItem(FileMenu, wx.ID_OPEN, '&打开', '打开文件')
        SaveItem = wx.MenuItem(FileMenu, wx.ID_SAVE, '&保存', '保存文件')
        QuitItem = wx.MenuItem(FileMenu, wx.ID_EXIT, '&退出', '退出')
        HelpItem = wx.MenuItem(HelpMenu, wx.ID_ANY, '&帮助', '骗你的,根本没有帮助')
        # 事件绑定

        # 菜单项或二级菜单加入到一级菜单里
        FileMenu.Append(OpenItem)
        FileMenu.Append(SaveItem)
        FileMenu.AppendSeparator()  # 菜单分隔符
        FileMenu.Append(QuitItem)
        HelpMenu.Append(HelpItem)

    '''工具栏初始化函数'''
    def ToolBarInit(self):
        self.ToolBar = self.CreateToolBar()
        self.ToolBar.Realize()

    '''状态栏初始化函数'''
    def StatusBarInit(self):
        self.StatusBar = self.CreateStatusBar()
        self.StatusBar.SetStatusText('启动完成')

    '''布局管理初始化函数'''
    def PanelInit(self):
        MainPanel = wx.Panel(self)
        # 定义MainBox
        PanelFont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        MainBox = wx.BoxSizer(wx.VERTICAL)

        # 定义Box_ReadData
        Box_ReadData = wx.BoxSizer(wx.HORIZONTAL)
        String_ReadDataPath = wx.StaticText(MainPanel, label='点云路径')
        String_ReadDataPath.SetFont(PanelFont)
        Box_ReadData.Add(String_ReadDataPath, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=10)
        TextCtrl_ReadDataPathString = wx.TextCtrl(MainPanel, value='输入点云文件夹(文件夹中不要有多余文件)')
        Box_ReadData.Add(TextCtrl_ReadDataPathString, proportion=1)
        MainBox.Add(Box_ReadData, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        MainBox.Add((-1, 10))

        # 定义Box_DataCheck
        Box_DataFormat = wx.BoxSizer(wx.HORIZONTAL)
        String_DataFormat = wx.StaticText(MainPanel, label='数据格式')
        String_DataFormat.SetFont(PanelFont)
        List_Of_Data_Format = ['阵列数据', '散点数据']
        List_Of_Data_Column_Num = ['3列', '4列']
        ComboBox_Of_Data_Format = wx.ComboBox(MainPanel, -1, value='阵列数据', choices=List_Of_Data_Format, style=wx.CB_SORT)
        ComboBox_Of_Data_Column_Num = wx.ComboBox(MainPanel, -1, value='3列', choices=List_Of_Data_Column_Num, style=wx.CB_SORT)
        Box_DataFormat.Add(String_DataFormat, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=10)
        Box_DataFormat.Add(ComboBox_Of_Data_Format, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=10)
        Box_DataFormat.Add(ComboBox_Of_Data_Column_Num, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=10)

        Button_DataRead = wx.Button(MainPanel, label='读取', size=(80, 25))
        Box_DataFormat.Add(Button_DataRead, flag=wx.RIGHT, border=10)
        Button_ArrayDataToScatterData = wx.Button(MainPanel, label='阵列转散点', size=(80, 25))
        Box_DataFormat.Add(Button_ArrayDataToScatterData, flag=wx.RIGHT, border=10)
        Button_DataSampling = wx.Button(MainPanel, label='采样', size=(80, 25))
        Box_DataFormat.Add(Button_DataSampling, flag=wx.RIGHT, border=10)
        Button_DataSave = wx.Button(MainPanel, label='保存', size=(80, 25))
        Box_DataFormat.Add(Button_DataSave, flag=wx.RIGHT, border=10)

        MainBox.Add(Box_DataFormat, flag=wx.ALIGN_LEFT | wx.LEFT, border=10)
        MainBox.Add((-1, 10))

        # 定义Box_Gauge
        Box_Gauge = wx.BoxSizer(wx.HORIZONTAL)
        Gauge = wx.Gauge(MainPanel, -1, 100, size=(-1, 25))
        Box_Gauge.Add(Gauge, proportion=1)
        MainBox.Add(Box_Gauge, flag=wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        MainBox.Add(-1, 10)

        MainPanel.SetSizer(MainBox)


def main():
    ex = wx.App()
    SimpleToolsMainFrame(None, style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    ex.MainLoop()


if __name__ == '__main__':
    main()
