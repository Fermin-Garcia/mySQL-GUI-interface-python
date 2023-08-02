'''

Here is another set of notes from the lesson i watched on tkinter here for my reference

'''


import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff= 0)
        self.filemenu.add_command(label= 'force close', command= exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='close', command= self.on_closing)
        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.root.config(menu=self.menubar)
        self.label = tk.Label(self.root, text='Login', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        username_label = tk.Label(self.root, text='Username:', font=('Arial',18))
        username_label.pack()
        username = tk.Entry(self.root)
        username.pack(padx=10, pady=10)
        password = tk.Entry(self.root,show='*')
        password.pack(padx=10, pady=10)
        # self.textbox = tk.Text(self.root, height=5, font=('Arial', 18))
        # self.textbox.bind("<KeyPress>", self.short_cut)
        # self.textbox.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='Submit', font=('Arial', 18), command= self.login)
        self.button.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='New User', font=('Arial', 18))
        self.button.pack(padx=10, pady=10)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    def login(self):
        user_window = tk.Tk()


    # def short_cut(self,event):
    #     if event.state == 8 and event.keysym == 'Return':
    #         self.show_message()
    #





MyGUI()
