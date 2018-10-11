

import tkinter as tk  # importing tkinter as tk for easier
from functools import partial  # this is a math like tool I am using
import numbers

import unittestingdoc


def is_number(label_result, numberTester):  # To check if letter or other non numbers in there
    #if isinstance(numberTester, numbers.Real):
    if numberTester.isdigit():
        #float(numberTester)
        return True
    elif float(numberTester):
        return True
    else:
        label_result.config(text="Please enter number")  # displaying result for user
        return False


def is_blank(label_result, number_chack):  # to check if the input section is blank
        if number_chack is "":
            label_result.config(text="Please enter number")  # displaying result for user
            return False
        else:
            return True


def call_plus_result(label_result, n1, n2):  # first method is used for adding
    if is_number(label_result, n1.get()) and is_number(label_result, n2.get()) is True:
        if is_blank(label_result, n1.get()) and is_blank(label_result, n2.get()) is True:
            num1 = (n1.get())  # getting the imput numbers from user
            num2 = (n2.get())
            result = float(num1)+float(num2)  # math formula done here
            label_result.config(text="Result is %f" % result)  # displaying result for user
            return
        else:
            pass
    else:
        pass


def call_minus_result(label_result, n1, n2):
    if is_number(label_result, n1.get()) and is_number(label_result, n2.get()) is True:
        if is_blank(label_result, n1.get()) and is_blank(label_result, n2.get()) is True:
            num1 = (n1.get())
            num2 = (n2.get())
            result = float(num1) - float(num2)
            label_result.config(text="Result is %f" % result)
            return
        else:
            pass
    else:
        pass


def call_multi_result(label_result, n1, n2):
    if is_number(label_result, n1.get()) and is_number(label_result, n2.get()) is True:
        if is_blank(label_result, n1.get()) and is_blank(label_result, n2.get()) is True:
            num1 = (n1.get())
            num2 = (n2.get())
            result = float(num1) * float(num2)
            label_result.config(text="Result is %f" % result)
            return
        else:
            pass
    else:
        pass


def call_divide_result(label_result, n1, n2) :
    if is_number(label_result, n1.get()) and is_number(label_result, n2.get()) is True:
        if is_blank(label_result, n1.get()) and is_blank(label_result, n2.get()) is True:
            num1 = (n1.get())
            num2 = (n2.get())
            result = float(num1) / float(num2)
            label_result.config(text="Result is %f" % result)
            return
        else:
            pass
    else:
        pass


root = tk.Tk()  # the master 'root' from which all the tk gui flowers grows
root.geometry('400x300+100+200')  # size of window, decided not to use pack()
root.title('Calculator')  # This goes at the very top, next to minimize, maximized, exit
number1 = tk.StringVar()  # getting the user entered numbers in string form, put in variable
number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Calculator").grid(row=0, column=2) # Title on gui, could remove if need be
labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)  # labels giving user instruction
labelNum2 = tk.Label(root, text="Enter second number").grid(row=2, column=0)
labelResult = tk.Label(root)  # blank label to put answer into, will be used later
labelResult.grid(row=7, column=2)  # place where the answer label goes.
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  # used for getting user entry
print(entryNum1)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

unittestingdoc.MyTest()

call_result = partial(call_plus_result, labelResult, number1, number2)  # used to figure out answer by starting function
buttonPLUS = tk.Button(root, text="  +  ", command=call_result).grid(row=3, column=0)  # button for adding

call_minus_result = partial(call_minus_result, labelResult, number1, number2)
buttonMinus = tk.Button(root, text="  -  ", command=call_minus_result).grid(row=4, column=0)

call_multi_result = partial(call_multi_result, labelResult, number1, number2)
buttonMulitply = tk.Button(root, text="  *  ", command=call_multi_result).grid(row=5, column=0)

call_divide_result = partial(call_divide_result, labelResult, number1, number2)
buttonDivide = tk.Button(root, text="  /  ", command=call_divide_result).grid(row=6, column=0)




root.mainloop()  # meant to continuously show screen, till user is done with it.



