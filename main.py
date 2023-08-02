import tkinter as tk
from tkinter import messagebox
import mysql.connector
import env


class MyGUI:

    def __init__(self):
        self.cnx = mysql.connector.connect(user=env.username, password=env.password, host=env.host_name,
                                           database=env.database)
        self.cursor = self.cnx.cursor()
        self.checkbutton = None
        self.check_var = None
        self.result_listbox = None
        self.selected_var = None
        self.emp_number = None
        self.search_button = None
        self.register_window = None
        self.emp_no_entry = None
        self.emp_password = None
        self.emp_username = None
        self.update_login_data = None
        self.submit_button = None
        self.emp_password_entry = None
        self.emp_username_entry = None
        self.emp_inital_cred = None
        self.results = None
        self.emp_search_query = None
        self.root = tk.Tk()
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='force close', command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='close', command=self.on_closing)
        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.root.config(menu=self.menubar)
        self.label = tk.Label(self.root, text='Login', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        self.username_label = tk.Label(self.root, text='Username:', font=('Arial', 18))
        self.username_label.pack()
        self.username = tk.Entry(self.root)
        self.username.pack(padx=10, pady=10)
        self.password = tk.Entry(self.root, show='*')
        self.password.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='Submit', font=('Arial', 18))  # , command= self.login)
        self.button.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='New User', font=('Arial', 18), command=self.new_user)
        self.button.pack(padx=10, pady=10)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def send_query(self, query):
        try:
            self.cursor.execute(query)
            self.results = self.cursor.fetchall()
            return self.results
        except mysql.connector.Error as err:
            print("An error occurred: {}".format(err))
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.cnx is not None:
                self.cnx.close()

    def create_login(self):
        # Make the window
        self.emp_inital_cred = tk.Tk()
        # Make the title
        self.emp_inital_cred.title('Create User Account')
        # Create entry block
        self.emp_username_entry = tk.Entry(self.emp_inital_cred)
        # post it on the page
        self.emp_username_entry.pack(padx=10, pady=10)
        # Make the password text block. Additionally, we are making the password show * when it is typed
        self.emp_password_entry = tk.Entry(self.emp_inital_cred, show='*')
        # Post it on the page
        self.emp_password_entry.pack(padx=10, pady=10)
        # Make a button that runs query_database
        self.submit_button = tk.Button(self.emp_inital_cred, text='Submit', command=self.update_user_name_and_pw)

    def update_user_name_and_pw(self):
        # Use parameterized query
        self.update_login_data = 'UPDATE employees_login SET user_name = %s, user_pw = %s'
        # Pass the values as a tuple to the query_request method
        self.query_request(data=(self.update_login_data, (self.emp_username_entry.get(), self.emp_password_entry.get())))

    def new_user(self):
        self.register_window = tk.Toplevel(self.root)
        self.register_window.geometry('800x800')
        self.register_window.title("Register")
        self.label = tk.Label(self.register_window, text="Register for Access", font=('Arial', 18))
        self.label.pack()
        self.emp_no_entry = tk.Entry(self.register_window)
        self.emp_no_entry.pack(padx=10, pady=10)
        self.search_button = tk.Button(self.register_window, text="Search", command=self.search_emp)
        self.search_button.pack()
        self.result_listbox = tk.Listbox(self.register_window, selectmode='SINGLE', height=20, width=50)
        self.result_listbox.pack(padx=10, pady=10)

    def search_emp(self):
        self.emp_number = self.emp_no_entry.get()
        self.emp_search_query = 'SELECT emp_no, FirstName, LastName FROM employees_login WHERE emp_no = %s'
        self.results = self.send_query(query=(self.emp_search_query, (self.emp_number,)))
        self.result_listbox.delete(0, tk.END)
        for emp in self.results:
            emp_no, first_name, last_name = emp
            self.result_listbox.insert(tk.END, f"Emp No: {emp_no}, First Name: {first_name}, Last Name: {last_name}")

    def on_closing(self):
        if messagebox.askyesno(title='Goodbye, cruel world', message='Are you sure you want to quit?'):
            self.root.destroy()


if __name__ == "__main__":
    MyGUI().root.mainloop()
