import wx 
app = wx.App()

frm = wx.Frame(None, title="Sonny's Calculator")

#welcome message
pop_message = "Welcome to Sonny's Calculator! Click OK to continue, CANCEL to exit"
pop_caption = "WELCOME"
popup_message = wx.MessageDialog(None, pop_message, pop_caption, wx.OK | wx.CANCEL)
popup_result = popup_message.ShowModal()

if popup_result == wx.ID_CANCEL:
    wx.Exit()

entry_message = "Please Enter the Expression You Are Looking to Solve"
entry_caption = "ENTER EXPRESSION"
default_value = ""
entry = wx.TextEntryDialog(None, entry_message, entry_caption, default_value)
entry_result = entry.ShowModal()    

if entry_result == wx.ID_CANCEL:
    #do we want to double check that the user wants to exit?
    wx.Exit()



frm.Centre(wx.BOTH)
frm.Show()

app.MainLoop()