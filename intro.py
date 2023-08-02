import tkinter
import tkinter as tk

root = tk.Tk()


root.geometry("300x300")
root.title('My first GUI')
# label = tk.Label(root, text='Hello World', font=('Arial', 20))
# label.pack(padx=10, pady=10)
# textbox = tk.Text(root, height=10, width=100, font=('Arial', 20))
# textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tkinter.Button(buttonframe, text='1',font=('Arial',20))
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2 = tkinter.Button(buttonframe, text='2',font=('Arial',20))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

btn3 = tkinter.Button(buttonframe, text='3',font=('Arial',20))
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)

btn4 = tkinter.Button(buttonframe, text='4',font=('Arial',20))
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)

btn5 = tkinter.Button(buttonframe, text='5',font=('Arial',20))
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)

btn6 = tkinter.Button(buttonframe, text='6',font=('Arial',20))
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)

oh_button = tk.Button(root, text='TEST', )
oh_button.place(x=200, y=200, height= 100, width=100)

buttonframe.pack(fill='x')


root.mainloop()



