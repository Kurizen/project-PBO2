import wx
import controller
import project

app = wx.App()
frame = controller.MyGui(parent=None)
frame.Show()
app.MainLoop()