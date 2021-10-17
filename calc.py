import wx
import string
from wx.core import DefaultPosition, DefaultSize, NullColour, NullFont, TE_MULTILINE, TE_READONLY, TextAttr, ColourDatabase, VERTICAL
app = wx.App()

operations = ['-', '+', '/', 'x']


def char_to_num(lst):
    for i, char in enumerate(lst):
        try:
            lst[i] = float(char)
        except ValueError:
            return None 
    return lst


def add(lst):
    total = 0
    for num in lst:
        total += num
    return total

def sub(lst):
    total = 0 
    for i, num in enumerate(lst):
        if i == 0:
            total = num
        else:
            total -= num
    return total

def mult(lst):
    total = 0
    for i, num in enumerate(lst):
        if i == 0:
            total = num
        else:
            total *= num
    return total

def div(lst):
    total = 0
    for i, num in enumerate(lst):
        if i == 0:
            total = num
        else:
            total /= num
    return total        




def execute(user_text):
    
    print("user_text before removing white spaces = ", user_text)
    user_text.replace(" ", "")
    print("user_text after removing white spaces = ", user_text)

    print("len(user_text) =", len(user_text))
    lst_expression = []
    total = 0
    long_num = False
    mult_digit_number = None
    for index, variable in enumerate(user_text):
        print("index =", index)
        #if variable == ' ' or variable == '\n':
          #  continue 
        if (index + 1) < len(user_text):

            if (user_text[index + 1] not in operations) and (user_text[index] not in operations):
                if long_num == False:
                    mult_digit_number = variable + user_text[index + 1]
                    long_num = True
                else:
                    mult_digit_number += user_text[index + 1] 

                print("multi digit = ", mult_digit_number)
                continue
        #print(type(user_text))
        print("variable = ", variable)
        print("variable type = ", type(variable))
        print(lst_expression)
        
        for i, op in enumerate(operations):
            op_present = False
            if variable == op:
                if i == 0:
                    lst_expression.append("MINUS")
                elif i == 1:
                    lst_expression.append("PLUS")
                elif i == 2:
                    lst_expression.append("DIV")
                else:
                    lst_expression.append("MULT") 
                op_present = True
                break 
        if op_present: 
            continue  
        #elif variable == ' ':
          #  continue                  
        try:
            #if variable == '' or variable == None:
             #   continue
            if long_num == True:
                try:
                    num = float(mult_digit_number)
                    lst_expression.append(num)
                    mult_digit_number = None
                    long_num = False
                    continue 
                except ValueError:
                   return None     
            num = float(variable)
            lst_expression.append(num)
        except ValueError:
            return None

    for index, expression in enumerate(lst_expression):
        
        if expression == None:
            continue
        else:
            if expression == "MULT" or expression == "DIV":

                if expression == "MULT":
                    soln = lst_expression[index - 1] * lst_expression[index + 1]
                    lst_expression[index - 1] = None
                    lst_expression[index] = None
                    lst_expression[index + 1] = soln
                else:
                    #DIV    
                    soln = lst_expression[index - 1] / lst_expression[index + 1]
                    lst_expression[index - 1] = None
                    lst_expression[index] = None
                    lst_expression[index + 1] = soln 

    lst_expression = [i for i in lst_expression if i != None]


    for index, expression in enumerate(lst_expression):

        if index == 0:
            total = expression
        elif expression == None:
            continue
        else:
            if expression == "PLUS" or expression == "MINUS":

                if expression == "PLUS":
                    total += lst_expression[index + 1]
                    lst_expression[index] = None
                    lst_expression[index + 1] = None
                else:
                    total -= lst_expression[index + 1] 
                    lst_expression[index] = None
                    lst_expression[index + 1] = None

    return total 


                                 



screen_width, screen_height = wx.DisplaySize()
def_width, def_height = DefaultSize
ex_frm = wx.Frame(None, title="Your expressions", pos = wx.Point(((screen_width/2) - 400),0))
entry_frm = wx.Frame(None, title = "Enter Expression", pos = wx.Point(0, (screen_height/2) + 130))

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
display_expression = wx.TextCtrl(ex_frm, -1, text_entry, DefaultPosition, DefaultSize , style = expression_style)
answer_expression = wx.TextCtrl(ans_frm, -1, text_entry, DefaultPosition, DefaultSize , style = answer_style)

#help frame
help_message = "This calculator can compute basic subtraction (-), addition (+), multiplication (x), and division (/). \
Currently, we can only support two numbers and one operation"
help_caption = "What can I compute?"
help_popup_message = wx.MessageDialog(helper_frm, help_message, help_caption, wx.OK)
help_popup_result = help_popup_message.ShowModal()
while 1:
    a_expression = wx.TextAttr(green, NullColour, NullFont, wx.TEXT_ALIGNMENT_RIGHT)
    a_expression.SetFontSize(25)
    answer_expression.SetStyle(-1, -1, a_expression)
    d_expression = wx.TextAttr(blue, NullColour, NullFont, wx.TEXT_ALIGNMENT_RIGHT)
    d_expression.SetFontSize(25)
    display_expression.SetStyle(-1, -1, d_expression)
    
    entry_message = "Enter the Expression You Are Looking to Solve"
    entry_caption = "ENTER EXPRESSION"
    default_value = ""
    entry = wx.TextEntryDialog(entry_frm, entry_message, entry_caption, default_value, pos = wx.Point(0,0))
    #fix the display message, it currently cuts off the last word
    entry_result = entry.ShowModal()    

    if entry_result == wx.ID_CANCEL:

        wx.Exit()
    else:
        user_text = entry.GetValue()
        if user_text == default_value:
            #this means nothing was entered
            user_text = error_message

        user_text += '\n'
        display_expression.AppendText(user_text)
        display_expression.SetDefaultStyle(TextAttr(green, NullColour, NullFont, wx.TEXT_ALIGNMENT_CENTER))
        #here is where we should pass the text to a parsing function, 
        #and then perform the operation, get the answer 
        
        answer = execute(user_text)
        if answer is None:
            answer = error_message
        else:
            answer = str(answer)
        answer += '\n'
        answer_expression.AppendText(answer)

    
    ex_frm.Centre(wx.VERTICAL)
    ans_frm.Centre(wx.VERTICAL)
    entry_frm.Centre(wx.HORIZONTAL)
    entry_frm.Show()
    ex_frm.Show()
    ans_frm.Show()

app.MainLoop()