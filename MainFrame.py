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
        self.SetSize((400, 600))
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
        pass


def main():
    ex = wx.App()
    SimpleToolsMainFrame(None, style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    ex.MainLoop()


if __name__ == '__main__':
    main()
