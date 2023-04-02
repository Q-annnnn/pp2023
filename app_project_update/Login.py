from tkinter import *
import os
from GUI import GUI

class Login:
    def register(self):
        """Designing window for registration"""
        self.register_screen = Toplevel(self.main_screen)
        self.register_screen.title("Register")
        self.register_screen.geometry("640x480")
        self.register_screen.resizable(False,False)

        # Set text variables
        self.username = StringVar()
        self.password = StringVar()

        # Set label for user's instruction
        Label(self.register_screen, text="Please enter details below").pack()
        Label(self.register_screen, text="").pack()

        # Set username label
        username_lable = Label(self.register_screen, text="Username * ")
        username_lable.pack()
        # Set username entry
        self.username_entry = Entry(self.register_screen, textvariable=self.username)
        self.username_entry.pack()
        # Set password label
        password_lable = Label(self.register_screen, text="Password * ")
        password_lable.pack()
        # Set password entry
        self.password_entry = Entry(self.register_screen, textvariable=self.password, show='*')
        self.password_entry.pack()
        Label(self.register_screen, text="").pack()
        Button(self.register_screen, text="Register", width=10, height=1, command = self.register_user).pack()

    def login(self):
        """Designing window for login"""
        self.login_screen = Toplevel(self.main_screen)
        self.login_screen.title("Login")
        self.login_screen.geometry("640x480")
        self.login_screen.resizable(False,False)
        Label(self.login_screen, text="Please enter details below to login").pack()
        Label(self.login_screen, text="").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.login_screen, text="Username * ").pack()
        self.username_login_entry = Entry(self.login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password * ").pack()
        self.password_login_entry = Entry(self.login_screen, textvariable=self.password_verify, show= '*')
        self.password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Button(self.login_screen, text="Login", width=10, height=1, command = self.login_verify).pack()

    def register_user(self):
        """Implementing event on register button"""
        # Get username and password
        username_info = self.username.get()
        password_info = self.password.get()

        # Open file in write mode (\\ for Windows, / for Linux)
        filepath = f'account\\{username_info}.txt'
        file = open(filepath, "w")
        # write username and password information into file
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        # Set a label for showing success information on screen
        Label(self.register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


    def login_verify(self):
        """Implementing event on login button """
        # Get username and password
        self.username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        # This will delete the entry after login button is pressed
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        # The method listdir() returns a list containing the names of the entries in the dir
        list_of_files = os.listdir('account')

        # Defining verification's conditions
        if f'{self.username1}.txt' in list_of_files:
            filepath = f'account/{self.username1}.txt'
            file1 = open(filepath, "r")
            # read the file,
            # as splitlines() actually splits on the newline character,
            # the newline character is not left hanging at the end of each line. if password1 in veri
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()

    def login_sucess(self):
        """Designing popup for login success"""
        self.main_screen.destroy()
        window = Tk()
        obj = GUI(window, self.username1)
        window.mainloop()

    def password_not_recognised(self):
        """Designing popup for login invalid password"""
        self.password_not_recog_screen = Toplevel(self.login_screen)
        self.password_not_recog_screen.title("Success")
        self.password_not_recog_screen.geometry("150x100")
        Label(self.password_not_recog_screen, text="Invalid Password ").pack()
        Button(self.password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()

    def user_not_found(self):
        """Designing popup for user not found"""
        global user_not_found_screen
        self.user_not_found_screen = Toplevel(self.login_screen)
        self.user_not_found_screen.title("Success")
        self.user_not_found_screen.geometry("150x100")
        Label(self.user_not_found_screen, text="User Not Found").pack()
        Button(self.user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()

    # Deleting popups
    def delete_login_success(self):
        self.login_success_screen.destroy()

    def delete_password_not_recognised(self):
        self.password_not_recog_screen.destroy()

    def delete_user_not_found_screen(self):
        self.user_not_found_screen.destroy()

    def on_closing(self):
        quit()

    def exit_program(self):
        quit()

    def main_account_screen(self):
        """Designing Main(first) window"""
        self.main_screen = Tk()
        self.main_screen.geometry("640x480")
        self.main_screen.title("Account Login")
        self.main_screen.resizable(False,False)
        # create a Form label
        Label(text="3D Printer Machine Management System", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        # create Login Button 
        Button(text="Login", height="2", width="30", command=self.login).pack()
        Label(text="").pack()
        # create a register button
        Button(text="Register", height="2", width="30", command=self.register).pack()
        
        Button(text="Quit", height="2", width="30", command=self.exit_program).pack()
        
        self.main_screen.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.main_screen.mainloop()

