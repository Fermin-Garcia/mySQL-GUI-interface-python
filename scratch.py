'''
General Scratch pad, typically cleared after troubleshooting is complete.


'''
import mysql.connector
import env


import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)

entry_1 = tk.Entry(frame)
entry_2 = tk.Entry(frame)
entry_3 = tk.Entry(frame)

entry_1.pack()
entry_2.pack()
entry_3.pack()

frame.pack()

root.mainloop()