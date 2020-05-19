##############################################################################
#  Main program template which uses wxFBfile created by wxFormBuilder
#  wxFBfile should be located in project directory
#  Class created in wxFBfile must be named:  wxFBclass
#  This template is READ ONLY,  save modified file in project directory
#############################################################################

import wx
import wxFBfile


class MainGui(wxFBfile.wxFBclass):
    def __init__(self, parent):
        wxFBfile.wxFBclass.__init__(self, parent)


app = wx.App(False)
frame = MainGui(None)
frame.Show(True)
app.MainLoop()
# this is a comment