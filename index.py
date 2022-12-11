from tkinter import *
from tkinter import messagebox
import math


def add_digit(digit):
    value = calc.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or'*' in value or'/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + operation)

def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value+value[:-1]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
        calc.insert(0, 0)

def add_sqrt():
    value = calc.get()
    value = float(value)
    value = math.sqrt(value)
    calc.delete(0, END)
    calc.insert(0, value)
    
def add_log10():
    value = calc.get()    
    value = math.log10(value)
    calc.delete(0, END)
    calc.insert(0, value)

        
def clear():
    calc.delete(0, END)
    calc.insert(0, 0)

def make_calc_button(operation):
    return Button(text=operation, bd=5, font=('Calibri', 13),
                     command=calculate)

def make_clear_button(operation):
    return Button(text=operation, bd=5, font=('Calibri', 13),
                     command=clear)

def make_operation_button(operation):
    return Button(text=operation, bd=5, font=('Calibri', 13),
                     command=lambda : add_operation(operation))

def make_sqrt_button(operation):
    return Button(text=operation, bd=5, font=('Calibri', 13),
                     command=add_sqrt)

def make_log10_button(operation):
    return Button(text=operation, bd=5, font=('Calibri', 13),
                     command=add_log10)

def make_digit_button(digit):
    return Button(text=digit, bd=5, font=('Calibri', 13),
                     command=lambda : add_digit(digit))

tk=Tk()
tk.geometry('260x360+100+200')
tk.resizable(0,0)
tk.title("Калькулятор")
tk['bg']='#FFF'

calc = Entry(tk, justify=RIGHT, font=('Calibri', 15), width=15)
calc.insert(0, '0')
calc.place(x=15, y=20, width=220, height=30)
#Числа от 1 до 9 и точка
make_digit_button('1').place(x=20, y=250, width=40, height=40)
make_digit_button('2').place(x=80, y=250, width=40, height=40)
make_digit_button('3').place(x=140, y=250, width=40, height=40)
make_digit_button('4').place(x=20, y=190, width=40, height=40)
make_digit_button('5').place(x=80, y=190, width=40, height=40)
make_digit_button('6').place(x=140, y=190, width=40, height=40)
make_digit_button('7').place(x=20, y=130, width=40, height=40)
make_digit_button('8').place(x=80, y=130, width=40, height=40)
make_digit_button('9').place(x=140, y=130, width=40, height=40)
make_digit_button('0').place(x=20, y=310, width=100, height=40)
make_digit_button('.').place(x=140, y=310, width=40, height=40)

#Основные математические действия
make_operation_button('+').place(x=200, y=310, width=40, height=40)
make_operation_button('-').place(x=200, y=250, width=40, height=40)
make_operation_button('*').place(x=200, y=190, width=40, height=40)
make_operation_button('/').place(x=200, y=130, width=40, height=40)

#Корень
#img=PhotoImage(file='radical.png')
make_sqrt_button('√').place(x=80, y=70, width=40, height=40)

#Модуль
make_log10_button('log10').place(x=125, y=70, width=70, height=40)

#Кнопка очистки
make_clear_button('C').place(x=20, y=70, width=40, height=40)

#Равно
make_calc_button('=').place(x=200, y=70, width=40, height=40)

tk.mainloop()