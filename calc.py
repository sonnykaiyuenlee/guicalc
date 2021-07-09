import wx
from wx.core import DefaultPosition, DefaultSize, NullColour, NullFont, TE_MULTILINE, TE_READONLY, TextAttr, ColourDatabase
app = wx.App()

frm = wx.Frame(None, title="Sonny's GUI Calculator")

error_message = "Invalid input! Try again!"

colordb = wx.ColourDatabase()
blue = colordb.Find("BLUE")
green = colordb.Find("GREEN")

#welcome message
pop_message = "Welcome to Sonny's Calculator! Click OK to continue, CANCEL to exit"
pop_caption = "WELCOME"
popup_message = wx.MessageDialog(None, pop_message, pop_caption, wx.OK | wx.CANCEL)
popup_result = popup_message.ShowModal()

if popup_result == wx.ID_CANCEL:
    wx.Exit()

text_entry = ""
expression_style = wx.TE_READONLY | wx.TE_MULTILINE |wx.TE_RICH | wx.TE_PROCESS_ENTER | wx.TE_LEFT
answer_style = wx.TE_READONLY | wx.TE_MULTILINE |wx.TE_RICH | wx.TE_PROCESS_ENTER | wx.TE_RIGHT
display_expression = wx.TextCtrl(frm, -1, text_entry, DefaultPosition, DefaultSize , expression_style)
while 1:
    d_expression = wx.TextAttr(blue, NullColour, NullFont, wx.TEXT_ALIGNMENT_RIGHT)
    display_expression.SetStyle(-1, -1, d_expression)
    style = display_expression.GetWindowStyle()
    display_expression.SetWindowStyle(style & ~wx.TEXT_ALIGNMENT_RIGHT | wx.TEXT_ALIGNMENT_LEFT)
    
    entry_message = "Please Enter the Expression You Are Looking to Solve"
    entry_caption = "ENTER EXPRESSION"
    default_value = ""
    entry = wx.TextEntryDialog(None, entry_message, entry_caption, default_value)
    #fix the display message, it currently cuts off the last word
    entry_result = entry.ShowModal()    

    if entry_result == wx.ID_CANCEL:
        #do we want to double check that the user wants to exit?
        wx.Exit()
    else:
        user_text = entry.GetValue()
        if user_text == default_value:
            #this means nothing was entered
            user_text = error_message

        user_text += '\n'
        #new_line = '\n'

        #display_expression = wx.TextCtrl(frm, -1, text_entry, DefaultPosition, wx.Size(100,100) , wx.TE_MULTILINE | wx.TE_READONLY)
        display_expression.AppendText(user_text)
        display_expression.SetDefaultStyle(TextAttr(green, NullColour, NullFont, wx.TEXT_ALIGNMENT_CENTER))
        #here is where we should pass the text to a parsing function, 
        #and then perform the operation, get the answer, 

        answer = "answer!\n"
        display_expression.AppendText(answer)
        
        
        

        #wx.StaticText(frm, -1, new_line)


    frm.Centre(wx.BOTH)
    frm.Show()

app.MainLoop()