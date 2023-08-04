# Import Tkinter for gui creation:
import tkinter as tk
from tkinter import messagebox
#
import mysql.connector
import datetime
import numpy as np
import env


class MyGUI:

    def __init__(self):
        # MySql.connect:
        self.patient_result = None
        self.patient_search_query = None
        self.patient_lastname_name_entry = None
        self.patient_first_name_entry = None
        self.patient_profile_page = None
        self.patient_id_entry = None
        self.patient_first_name_label = None
        self.patient_id_label = None
        self.patient_lastname_name_label = None
        self.patient_profile_search = None
        self.patient_profile_button = None
        self.greeting_user = None
        self.greeting = None
        self.greeting_var = None
        self.greetings = None
        self.dashboard_window_access2 = None
        self.login_check = None
        self.login_validation = None
        self.reenter_password_label = None
        self.users_new_password_info = None
        self.new_username_info = None
        self.register_new_user_query = None
        self.confirm_users_new_password_results = None
        self.confirm_users_new_password = None
        self.password_label = None
        self.messagebox = tk.messagebox
        self.emp_search = None
        self.cnx = mysql.connector.connect(user=env.username, password=env.password, host=env.host_name,
                                           database=env.database)
        self.cursor = self.cnx.cursor()
        self.emp_no_results = None
        self.checkbutton = None
        self.check_var = None
        self.result_listbox = None
        self.new_username = None
        self.users_new_password = None
        self.selected_var = None
        self.get_emp_number = None
        self.username_label = None
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
        self.root.title('Log In')
        self.root.geometry('800x800')
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
        self.username_label.pack(padx=10, pady=10)
        self.username = tk.Entry(self.root)
        self.username.pack(padx=10, pady=10)
        self.password_label = tk.Label(self.root, text='password:', font=('Arial', 18))
        self.password_label.pack(padx=10, pady=10)
        self.password = tk.Entry(self.root, show='*')
        self.password.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='Login', font=('Arial', 18), command=self.user_dashboard)
        self.button.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='New User', font=('Arial', 18), command=self.new_user)
        self.button.pack(padx=10, pady=10)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    '''
    end of __init__(). Methods below:
    '''

    # Below are the methods use to create a new user
    # account and update mysql database for employees account information:

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

    def search_emp(self):
        self.emp_search = 'SELECT emp_no, FirstName, LastName,user_name, user_pw FROM employees_login WHERE emp_no = %s'
        self.get_emp_number = self.emp_no_entry.get()
        self.cursor.execute(self.emp_search, (self.get_emp_number,))
        self.results = self.cursor.fetchall()
        if self.results[0][3] is None and self.results[0][4] is None:
            self.username_label = tk.Label(self.register_window, text='Please enter new username', font=(['Arial', 18]))
            self.username_label.pack(padx=10, pady=10)
            self.new_username = tk.Entry(self.register_window, state='normal')
            self.new_username.pack(padx=10, pady=10)
            self.password_label = tk.Label(self.register_window, text='Please enter password', font=(['Arial', 18]))
            self.password_label.pack(padx=10, pady=10)
            self.users_new_password = tk.Entry(self.register_window, show='*', state='normal')
            self.users_new_password.pack(padx=10, pady=10)
            self.new_username.pack(padx=10, pady=10)
            self.reenter_password_label = tk.Label(self.register_window, text='Please re-enter password',
                                                   font=(['Arial', 18]))
            self.reenter_password_label.pack(padx=10, pady=10)
            self.confirm_users_new_password = tk.Entry(self.register_window, show='*', state='normal')
            self.confirm_users_new_password.pack(padx=10, pady=10)
            self.submit_button = tk.Button(self.register_window, text='Submit',
                                           command=self.update_login_information)
            self.submit_button.pack(padx=10, pady=10)

        else:
            self.messagebox.showinfo(title='User Already Registered:',
                                     message='User is already registered. Contact system '
                                             'administrator.')

    def update_login_information(self):
        self.register_new_user_query = 'update employees_login  set user_name = %s, user_pw = %s  where emp_no = %s'
        self.new_username_info = self.new_username.get()
        self.users_new_password_info = self.users_new_password.get()
        self.confirm_users_new_password_results = self.confirm_users_new_password.get()
        if self.users_new_password_info == self.confirm_users_new_password_results:
            self.cursor.execute(self.register_new_user_query, (self.new_username.get(), self.users_new_password.get(),
                                                               self.emp_no_entry.get()))
            self.cnx.commit()
            self.messagebox.showinfo(title='Password Updated!', message='Your Password has been updated successfully')
        elif self.users_new_password_info != self.confirm_users_new_password_results:
            self.messagebox.showerror(title='Password Mismatch', message='Your passwords don\'t match, '
                                                                         'Please try again.')
        else:
            self.messagebox.showerror(title='Unknown ERROR', message='An Error has occurred. Please try you '
                                                                     'request again later. If problem persists '
                                                                     'please contact system administrators ')

        # Below are the methods used to access employee portal.

    def user_dashboard(self):
        self.login_validation = 'select * from employees_login where user_name = %s and user_pw = %s'
        self.cursor.execute(self.login_validation, (self.username.get(), self.password.get()))
        self.login_check = self.cursor.fetchall()
        if self.login_check != [] and self.login_check[0][-1] == 2:
            self.user_dashboards_leve_two()  # insert employee dashboard here
        elif self.login_check == []:
            self.messagebox.showinfo(title='No user found', message='Your username/password is incorrect')
        else:
            self.messagebox.showwarning(title='error occured',
                                        message='an Unknow error has occured, please try your request again. If problems persist,contact system administrator')

    def user_dashboards_leve_two(self):
        self.dashboard_window_access2 = tk.Toplevel(self.root)
        self.dashboard_window_access2.geometry('800x800')

        self.greeting_user = tk.Label(self.dashboard_window_access2,
                                      text=f'Welcome {self.login_check[0][1].title()} {self.login_check[0][2].title()} , What would you like to do today?',
                                      font=('Arial', 20))
        self.greeting_user.pack(padx=40, pady=20)
        self.patient_profile_button = tk.Button(self.dashboard_window_access2, text='Access Patient Profile',
                                                command=self.patient_profile_page_search)
        self.patient_profile_button.pack(padx=10, pady=10)

    def patient_profile_page_search(self):
        self.patient_profile_page = tk.Toplevel(self.dashboard_window_access2)
        self.patient_profile_page.geometry('500x500')
        self.patient_profile_search = tk.Frame(self.patient_profile_page)
        self.patient_id_label = tk.Label(self.patient_profile_search, text='Enter patient\'s ID')
        self.patient_id_entry = tk.Entry(self.patient_profile_search)
        self.patient_first_name_label = tk.Label(self.patient_profile_search, text='Enter patient\'s first name')
        self.patient_first_name_entry = tk.Entry(self.patient_profile_search)
        self.patient_lastname_name_label = tk.Label(self.patient_profile_search, text='Enter patient\'s last name')
        self.patient_lastname_name_entry = tk.Entry(self.patient_profile_search)
        self.patient_id_label.pack()
        self.patient_id_entry.pack()
        self.patient_first_name_label.pack()
        self.patient_first_name_entry.pack()
        self.patient_lastname_name_label.pack()
        self.patient_lastname_name_entry.pack()
        self.patient_search_button = tk.Button(self.patient_profile_search, text='Search for patient',
                                               command=self.search_patient)
        self.patient_search_button.pack(padx=10, pady=10)
        self.patient_result = tk.Listbox(self.patient_profile_search, selectmode='single', height = 10, width = 50)
        self.select_patient = tk.Button(self.patient_profile_search, text= 'Select Patient', command = self.open_patient_profile)
        self.select_patient.pack(padx=10, pady=10)
        self.patient_result.pack(padx=10, pady=10)
        self.patient_profile_search.pack(padx=10, pady=10)

    def open_patient_profile(self):
        self.patient_profile_page_frame = tk.Frame(self.patient_profile_page)
        self.load_patient_information_query ='select * from patient_information where patient_id = %s;'
        self.cursor.execute(self.load_patient_information_query, (self.selected_patient_id,))
        self.patient_information = self.cursor.fetchall()

        # finish writing for loop
        for items in self.patient_information[0]:
            print(len(self.patient_information[0]))
            print(f'here is one item {(items)}')
            self



        '''
        We stopped here, We are trying to load patient information on a screen, in each entry box we haven't ran the
        loop but we still need to go in and disable the buttons so they are not editable.
        
        '''



        print(self.patient_information)
        self.patient_profile_search.destroy()










    def search_patient(self):
        self.patient_search_query = 'select patient_id, patent_FirstName, patient_LastName from patient_information where patient_id like %s or patent_FirstName like %s or patient_LastName like %s'
        self.cursor.execute(self.patient_search_query, (
        self.patient_id_entry.get(), self.patient_first_name_entry.get(), self.patient_lastname_name_entry.get()))
        self.selected_patient_id = None
        # get results
        self.show_patient_results = self.cursor.fetchall()
        if self.patient_result != []:
            for pt_id, first,last in self.show_patient_results:
                self.selected_patient_id = pt_id
                self.patient_result.delete(0,tk.END)
                self.patient_result.insert(tk.END, f'Patient ID : {pt_id} | First Name: {first} | Last Name:{last} ')
        else:
            self.messagebox.showerror(title='No Patient Found', message='No Patient Found Please Try Again! ')



        # self.dashboard_window = tk.Toplevel(self.root)

        # Below are the methods used to close the program
    def on_closing(self):
        self.root.destroy()
        self.cursor.close()
        self.cnx.close()



if __name__ == "__main__":
    MyGUI().root.mainloop()
    # if messagebox.askyesno(title='Goodbye, cruel world', message='Are you sure you want to quit?'):