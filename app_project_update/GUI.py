from cProfile import label
from tkinter import *
from tkinter import ttk
from turtle import update
import tkinter.messagebox
import database



class GUI:
    def __init__(self, root, account):
        self.window = root
        self.window.title("3D Printer Machine Management Application")
        self.window.geometry("1024x768")
        self.window.grid()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # This variable to open different accounts
        self.account = account

        # Variable
        self.name = StringVar()
        self.manufacturer = StringVar()
        self.model = StringVar()
        self.serial_num = StringVar()
        self.firmware_vers = StringVar()
        self.calibration =  StringVar()
        self.usage_count = StringVar()

        self.frame_left = Frame(self.window, bg="#e5e5e5")
        self.frame_left.place(x=0, y=0, width=242, height=700, relwidth=1, relheight=1)

        self.frame_right = Frame(self.window, bg="#f2f2f2")
        self.frame_right.place(x=242, y=0, relwidth=1, relheight=1)


        # Button in the left frame
        self.save_printer = Button(self.frame_left, text="Add a new printer ", highlightthickness=0, bg="#fbfbfb", command=self.save_data,bd=0).place(x=33, y=76, width=175, height=36)
        self.update_printer = Button(self.frame_left, text="Update a printer", highlightthickness=0, bg="#fbfbfb", command=self.update_data,bd=0).place(x=33, y=146, width=175, height=36)
        self.delete_printer = Button(self.frame_left, text="Delete a printer", highlightthickness=0, bg="#fbfbfb", command=self.delete_data,bd=0).place(x=33, y=216, width=175, height=36)
        self.maint_check = Button(self.frame_left, text="Maintenance Checking", highlightthickness=0, bg="#fbfbfb", command=self,bd=0).place(x=33, y=286, width=175, height=36)
        self.reset_printer = Button(self.frame_left, text="Reset", highlightthickness=0, fg="#ffffff", bg="#fb5870", command=self.delete_all_data, bd=0).place(x=33, y=356, width=175, height=36)
        Button(self.frame_left, text="Sign out", highlightthickness=0, fg="#ffffff", bg="#fb5870", command=self.signout, bd=0).place(x=33, y=665, width=175, height=36)
        

        # Button in the right frame
        
        #This variable to choose what kind of search do you want to use
        self.type_of_search = StringVar()
        self.search = StringVar()
        
        self.search_printer = Button(self.frame_right, text="Search", highlightthickness=0, bg="#33b249",fg="#ffffff", command=self.search_data,bd=0).place(x=609, y=76, width=93, height=30)
        Button(self.frame_right, text="Show all", highlightthickness=0, bg="#fbfbfb", command=self.display_data,bd=0).place(x=80, y=110, width=70, height=20)
        self.search_printer_text = Entry(self.frame_right, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.search).place(x=80, y=76, width=491, height=30)

        self.search_choose = ttk.Combobox(self.frame_right, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.type_of_search)
        self.search_choose['values'] = ('Option', 'Name', 'Manufacturer', 'Model', 'Serial Number', 'Calibration', "Usage (times)")
        self.search_choose.current(0)
        self.search_choose.place(x=500, y=76, width=100, height=30)


        # Middle Frame that contain input information of the 3D printer machine
        self.mid_frame = Frame(self.frame_right, bg="#e5e5e5")
        self.mid_frame.place(x=80, y=138, width=622, height=303)

        # Widget for the middle frame
        Label(self.frame_right, text="Home", highlightthickness=0, bg="#f2f2f2", font=('Century Gothic', 20)).place(x=80, y=23)
        self.printer_name = Label(self.mid_frame, text="3D Printer Name", highlightthickness=0, bg="#e5e5e5").place(x=15, y=15, width=121, height=21)
        self.printer_manufacturer = Label(self.mid_frame, text="Manufacturer", highlightthickness=0, bg="#e5e5e5").place(x=15, y=55, width=121, height=21)
        self.printer_model = Label(self.mid_frame, text="Model", highlightthickness=0, bg="#e5e5e5").place(x=15, y=95, width=121, height=21)
        self.printer_serial_num = Label(self.mid_frame, text="Serial Number", highlightthickness=0, bg="#e5e5e5").place(x=15, y=135, width=121, height=21)
        self.printer_firmware_vers = Label(self.mid_frame, text="Firmware Version", highlightthickness=0, bg="#e5e5e5").place(x=15, y=175, width=121, height=21)
        self.printer_calibration = Label(self.mid_frame, text="Calibration", highlightthickness=0, bg="#e5e5e5").place(x=15, y=215, width=121, height=21)
        self.usage_count = Label(self.mid_frame, text="Usage (times)", highlightthickness=0, bg="#e5e5e5").place(x=15, y=255, width=121, height=21)
        # Entry for the middle frame
        self.printer_name_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.name)
        self.printer_name_text.place(x=159, y=15, width=400, height=21)

        self.manufacturer_text = Entry(self.mid_frame, font=('arial', 12, 'bold'),  width=404, justify=LEFT, textvariable=self.manufacturer)
        self.manufacturer_text.place(x=159, y=55, width=400, height=21)

        self.model_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.model)
        self.model_text.place(x=159, y=95, width=400, height=21)

        self.serial_num_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.serial_num)
        self.serial_num_text.place(x=159, y=135, width=400, height=21)

        self.firmware_vers_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.firmware_vers)
        self.firmware_vers_text.place(x=159, y=175, width=400, height=21)


        self.calibration_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT).place(x=159, y=215, width=400, height=21)
        self.calibration_choose = ttk.Combobox(self.mid_frame, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.calibration)
        self.calibration_choose['values'] = ('Auto Bed Leveling',
                                        'Manual Bed Leveling')

        self.calibration_choose.current()
        self.calibration_choose.place(x=159, y=215, width=400, height=25)

        self.usage_count_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT).place(x=159, y=255, width=400, height=21)
        self.usage_count_choose = ttk.Combobox(self.mid_frame, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.usage_count)
        self.usage_count_choose['values'] = ('0','1','2','3','4','5','6','7','8','9','10',
                                        'More than 10')

        self.usage_count_choose.current()
        self.usage_count_choose.place(x=159, y=255, width=400, height=25)



        # Bottom Frame that list information of 3D printer
        self.bottom_frame = Frame(self.frame_right, bg="#e5e5e5")
        self.bottom_frame.place(x=80, y=420, width=622, height=301)

        # -------------------------------Treeview-------------------------------
        scroll_x = Scrollbar(self.bottom_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.bottom_frame, orient=VERTICAL)

        columns = ('ID', 'name', 'manufacturer', 'model', 'serial_num', 'firmware_vers', 'calibration', "usage_count")
        self.printer_list = ttk.Treeview(self.bottom_frame, height=12,
                                           columns=columns,
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set,)
        

        scroll_x.config(command = self.printer_list.xview)
        scroll_y.config(command = self.printer_list.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.printer_list.pack(fill = BOTH, expand = 1)

        self.printer_list.heading('ID', text='ID')
        self.printer_list.heading('name', text='Name')
        self.printer_list.heading('manufacturer', text='Manufacturer')
        self.printer_list.heading('model', text='Model')
        self.printer_list.heading('serial_num', text='Serial')
        self.printer_list.heading('firmware_vers', text='Firmware')
        self.printer_list.heading('calibration', text='Calibration')
        self.printer_list.heading('usage_count', text = "Usage (times)")


        self.printer_list['show'] = 'headings'
        self.printer_list.column('ID', width=20)
        self.printer_list.column('name', width=70)
        self.printer_list.column('manufacturer', width=50)
        self.printer_list.column('model', width=30)
        self.printer_list.column('serial_num', width=40)
        self.printer_list.column('firmware_vers', width=20)
        self.printer_list.column('calibration', width=70)
        self.printer_list.column('usage_count', width=60)
        self.printer_list.pack(fill=BOTH, expand=1)

        self.printer_list.bind('<ButtonRelease-1>', self.clicker)
        self.display_data()

        self.choose_row()

    def save_data(self):
        if self.name.get() == "" or self.manufacturer.get() == "" or self.model.get() == "" or self.serial_num.get() == "" or self.firmware_vers.get() == "" or self.calibration.get() == "" or self.usage_count.get() == "":
            tkinter.messagebox.askokcancel(title='Error',
                                           message='Please enter valid data!')
        else:
            try:
                database.add(self.account,
                             self.name.get(),
                             self.manufacturer.get(),
                             self.model.get(),
                             self.serial_num.get(),
                             self.firmware_vers.get(),
                             self.calibration.get(),
                             self.usage_count.get())
                self.display_data()

                tkinter.messagebox.showinfo(title='Message',
                                            message='Sucessful added printer!')
                self.printer_name_text.delete(0, END)
                self.manufacturer_text.delete(0, END)
                self.model_text.delete(0, END)
                self.serial_num_text.delete(0, END)
                self.firmware_vers_text.delete(0, END)

            except Exception as es:
                tkinter.messagebox.showerror(title='Error',
                                             message=f'Because {str(es)}')

    def display_data(self):
        """Display all data by fetch data"""
        data = database.display(account=self.account)
        if len(data) >= 0:
            self.printer_list.delete(*self.printer_list.get_children())
            for i in data:
                self.printer_list.insert("", END, value=i)

    def choose_row(self):
        """Choose a row and return values into entries"""
        self.printer_name_text.delete(0, END)
        self.manufacturer_text.delete(0, END)
        self.model_text.delete(0, END)
        self.serial_num_text.delete(0, END)
        self.firmware_vers_text.delete(0, END)

        # Choose a value of a row
        choose_row = self.printer_list.focus()
        # Grab the value of the chosen row
        self.data = self.printer_list.item(choose_row, 'value')
        try:
            self.id = self.data[0]
            self.name.set(self.data[1])
            self.manufacturer.set(self.data[2])
            self.model.set(self.data[3])
            self.serial_num.set(self.data[4])
            self.firmware_vers.set(self.data[5])
            self.calibration.set(self.data[6])
            self.usage_count.set(self.data[7])
        except:
            pass

    def clicker(self, event):
        """Click handler when you click into a row"""
        self.choose_row()

    def update_data(self):
        if self.name.get() == "" or self.manufacturer.get() == "" or self.model.get() == "" or self.serial_num.get() == "" or self.firmware_vers.get() == "" or self.calibration.get() == "" or self.usage_count.get():
            tkinter.messagebox.askretrycancel(title='Error', message='Please choose a data!')
        else:
            try:
                answer = tkinter.messagebox.askyesno("Confirmation", "Do you want to update information?")
                if answer:
                    database.update(self.account,
                                    self.id,
                                    self.name.get(),
                                    self.manufacturer.get(),
                                    self.model.get(),
                                    self.serial_num.get(), 
                                    self.firmware_vers.get(),
                                    self.calibration.get(),
                                    self.usage_count.get())

                else:
                    if not update:
                        return
                self.display_data()
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Because of {str(e)}")

        # Fill in empty into the entries
        self.printer_name_text.delete(0, END)
        self.manufacturer_text.delete(0, END)
        self.model_text.delete(0, END)
        self.serial_num_text.delete(0, END)
        self.firmware_vers_text.delete(0, END)
        
    def delete_data(self):
        if not self.printer_list.selection():
            tkinter.messagebox.showwarning("Error", "Please choose a data you want to delete!")
        else:
            answer = tkinter.messagebox.askyesno("Delete data", "Are you sure you want to permanently delete this?")
            if answer:
                database.delete(self.account, self.id)
                self.display_data()
                self.printer_name_text.delete(0, END)
                self.manufacturer_text.delete(0, END)
                self.model_text.delete(0, END)
                self.serial_num_text.delete(0, END)
                self.firmware_vers_text.delete(0, END)
                tkinter.messagebox.showinfo("Delete", "You deleted the data")
            
    def delete_all_data(self):
        """A function to delete all data and drop table"""
        answer = tkinter.messagebox.askyesno("Warning", "Are you sure you want to permanently delete ALL data?")
        if answer:
            database.delete_all(self.account)
            self.display_data()
            # Fill in empty into the entries
            self.printer_name_text.delete(0, END)
            self.manufacturer_text.delete(0, END)
            self.model_text.delete(0, END)
            self.serial_num_text.delete(0, END)
            self.firmware_vers_text.delete(0, END)

    def signout(self):
        self.window.destroy()

    def on_closing(self):
        quit()

    def search_data(self):
        if self.type_of_search == "Option" or self.search == "":
            tkinter.messagebox.showwarning("Error", "Please choose the attribute!")
        else:
            try:
                data = database.search(self.account, self.type_of_search.get(), self.search.get())
                if len(data) >= 0:
                    self.printer_list.delete(*self.printer_list.get_children())
                    for i in data:
                        self.printer_list.insert("", END, value=i)
            except:
                tkinter.messagebox.showwarning("Warning", "Please choose the attribute!")

