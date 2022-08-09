import tkinter

window = tkinter.Tk()
window.title("Мой калькулятор")
window.geometry("300x300")

def add():
    print("Выполняем сложение")
    num1 = text_num1.get()
    #print(num1)
    num1 = int(num1)
    num2 = text_num2.get()
    #print(num2)
    num2 = int(num2)
    result = num1 + num2
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, result)


def sub():
    print("Выполняем вычитание")
    num1 = text_num1.get()
    num1 = int(num1)
    num2 = text_num2.get()
    num2 = int(num2)
    result = num1 - num2
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, result)
    # text_answer.insert(0, f"{num1} - {num2} = {result}")   доп. задание
button_add = tkinter.Button(window, text="+", command=add)
button_sub = tkinter.Button(window, text="-", command=sub)

text_num1 = tkinter.Entry(window, width=20, bg = "white")
text_num2 = tkinter.Entry(window, width=20, bg = "white")
text_answer = tkinter.Entry(window, width=20, bg = "white")

def start_calculator():


    text_num1.place(x=95, y=40)
    text_num2.place(x=95, y=81)

    button_add.place(x=95, y=110)
    button_sub.place(x=160, y=110)

    text_answer.place(x=95, y=221)
    window.mainloop()

start_calculator()