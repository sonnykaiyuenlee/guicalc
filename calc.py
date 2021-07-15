import wx
from wx.core import DefaultPosition, DefaultSize, NullColour, NullFont, TE_MULTILINE, TE_READONLY, TextAttr, ColourDatabase, VERTICAL
app = wx.App()

screen_width, screen_height = wx.DisplaySize()
def_width, def_height = DefaultSize
entry_frm = wx.Frame(None, title = "Enter Expression", pos = wx.Point(0, (screen_height/2) + 130))
ex_frm = wx.Frame(None, title="Your expressions", pos = wx.Point(((screen_width/2) - 400),0))
ans_frm = wx.Frame(None, title ="Sonny's answers", pos = wx.Point((screen_width/2),0))


helper_frm = wx.Frame(None, title = "What can I compute?", size = DefaultSize)

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
display_expression = wx.TextCtrl(ex_frm, -1, text_entry, DefaultPosition, DefaultSize , expression_style)
answer_expression = wx.TextCtrl(ans_frm, -1, text_entry, DefaultPosition, DefaultSize , answer_style)

#help frame
help_message = "This calculator can compute basic subtraction, addition, multiplication, and division. \
Currently, we can only support two numbers and one operation"
help_caption = "What can I compute?"
help_popup_message = wx.MessageDialog(helper_frm, help_message, help_caption, wx.OK)
help_popup_result = help_popup_message.ShowModal()
while 1:
    a_expression = wx.TextAttr(green, NullColour, NullFont, wx.TEXT_ALIGNMENT_RIGHT)
    answer_expression.SetStyle(-1, -1, a_expression)
    d_expression = wx.TextAttr(blue, NullColour, NullFont, wx.TEXT_ALIGNMENT_RIGHT)
    display_expression.SetStyle(-1, -1, d_expression)
    #style = display_expression.GetWindowStyle()
    #display_expression.SetWindowStyle(style & ~wx.TEXT_ALIGNMENT_RIGHT | wx.TEXT_ALIGNMENT_LEFT)
    
    entry_message = "Please Enter the Expression You Are Looking to Solve"
    entry_caption = "ENTER EXPRESSION"
    default_value = ""
    entry = wx.TextEntryDialog(entry_frm, entry_message, entry_caption, default_value, pos = wx.Point(0,0))
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
        answer_expression.AppendText(answer)
        
        
        

        #wx.StaticText(frm, -1, new_line)

    
    ex_frm.Centre(wx.VERTICAL)
    ans_frm.Centre(wx.VERTICAL)
    entry_frm.Centre(wx.HORIZONTAL)
    entry_frm.Show()
    ex_frm.Show()
    ans_frm.Show()

app.MainLoop()