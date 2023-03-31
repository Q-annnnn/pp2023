from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas as pd

def exit():
    result = messagebox.askyesno("Exit", "Do you want to exit?")
    if result:
        window.destroy()
    else:
        pass

def export_data():
    url = filedialog.asksaveasfilename(defaultextension = ".csv")
    indexing = Printer_table.get_children()
    newlist = []
    for index in indexing:
        content = Printer_table.item(index)
        datalist = content['values']
        newlist.append(datalist)
    
    table = pd.DataFrame(newlist, columns = ["ID", "PrinterName", "Manufacturer", "ManufacturingYear", "FirmwareVersion", "Filament", "MaintenanceCost", "Date", "Time"])
    table.to_csv(url, index = False)
    messagebox.showinfo("Success", "Data is saved")


def toplevel_data(title, button_text, command):
    global idEntry, printernameEntry, manufacturerEntry, manufacturingyearEntry, firmwareversionEntry, filamentEntry, maintenancecostEntry, screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0,0)
    idLabel = Label(screen, text = "ID", font = ("Times New Roman", 20, "bold"))
    idLabel.grid(row = 0, column = 0, padx = 25, pady = 15, sticky = W)
    idEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    idEntry.grid(row = 0, column = 1, padx = 10, pady = 15)

    printernameLabel = Label(screen, text = "Printer Name", font = ("Times New Roman", 20, "bold"))
    printernameLabel.grid(row = 1, column = 0, padx = 25, pady = 15, sticky = W)
    printernameEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    printernameEntry.grid(row = 1, column = 1, padx = 10, pady = 15)

    manufacturerLabel = Label(screen, text = "Manufacturer", font = ("Times New Roman", 20, "bold"))
    manufacturerLabel.grid(row = 2, column = 0, padx = 25, pady = 15, sticky = W)
    manufacturerEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    manufacturerEntry.grid(row = 2, column = 1, padx = 10, pady = 15)    

    manufacturingyearLabel = Label(screen, text = "Manufacturing Year", font = ("Times New Roman", 20, "bold"))
    manufacturingyearLabel.grid(row = 3, column = 0, padx = 25, pady = 15, sticky = W)
    manufacturingyearEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    manufacturingyearEntry.grid(row = 3, column = 1, padx = 10, pady = 15)    
 
    firmwareversionLabel = Label(screen, text = "Firmware Version", font = ("Times New Roman", 20, "bold"))
    firmwareversionLabel.grid(row = 4, column = 0, padx = 25, pady = 15, sticky = W)
    firmwareversionEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    firmwareversionEntry.grid(row = 4, column = 1, padx = 10, pady = 15)    

    filamentLabel = Label(screen, text = "Filament", font = ("Times New Roman", 20, "bold"))
    filamentLabel.grid(row = 5, column = 0, padx = 25, pady = 15, sticky = W)
    filamentEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    filamentEntry.grid(row = 5, column = 1, padx = 10, pady = 15)  

    maintenancecostLabel = Label(screen, text = "Maintenance Cost (K VND)", font = ("Times New Roman", 20, "bold"))
    maintenancecostLabel.grid(row = 6, column = 0, padx = 25, pady = 15, sticky = W)
    maintenancecostEntry = Entry(screen, font = ("Roman", 15, "bold"), width = 24)
    maintenancecostEntry.grid(row = 6, column = 1, padx = 10, pady = 15)  

    Printer_Button = ttk.Button(screen, text = button_text, command = command)
    Printer_Button.grid(row = 7, columnspan = 2, pady =15)
    if title == "Update Printer":
        indexing = Printer_table.focus()

        content = Printer_table.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        printernameEntry.insert(0, listdata[1])
        manufacturerEntry.insert(0, listdata[2])
        manufacturingyearEntry.insert(0, listdata[3])
        firmwareversionEntry.insert(0, listdata[4])
        filamentEntry.insert(0, listdata[5])
        maintenancecostEntry.insert(0, listdata[6])

def update_data():
    currentdate = time.strftime("%d/%m/%Y")
    currenttime = time.strftime("%H:%M:%S")
    query = 'UPDATE printer set printername = %s, manufacturer = %s, manufacturingyear = %s , firmwareversion = %s , filament = %s , maintenancecost = %s, date = %s, time = %s where id = %s'
    mycursor.execute(query, (printernameEntry.get(), manufacturerEntry.get(), manufacturingyearEntry.get(), firmwareversionEntry.get(), filamentEntry.get(), maintenancecostEntry.get(), currentdate, currenttime, idEntry.get()))
    DBcon.commit()
    messagebox.showinfo("Success", f'ID {idEntry.get()} is updated', parent = screen)
    screen.destroy()
    show_printer()

def show_printer():
    query = "SELECT * from printer"
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    Printer_table.delete(*Printer_table.get_children())
    for data in fetched_data:
        Printer_table.insert("", END, values = data)

def delete_printer():
    indexing = Printer_table.focus()
    content = Printer_table.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE from printer where id = %s '
    mycursor.execute(query, content_id)
    DBcon.commit()
    messagebox.showinfo("Deleted", f'This ID {content_id} is deleted successfully')
    query = "SELECT * from printer"
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    Printer_table.delete(*Printer_table.get_children())
    for data in fetched_data:
        Printer_table.insert("", END, values = data)

def search_data():
    query = "SELECT * from printer where id = %s or printername = %s or manufacturer = %s or manufacturingyear = %s or firmwareversion = %s or filament = %s or maintenancecost = %s"
    mycursor.execute(query,(idEntry.get(), printernameEntry.get(), manufacturerEntry.get(), manufacturingyearEntry.get(), firmwareversionEntry.get(), filamentEntry.get(), maintenancecostEntry.get()))
    Printer_table.delete(*Printer_table.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        Printer_table.insert('', END, values = data)

def add_data():
    if idEntry.get() == '' or printernameEntry.get == '' or manufacturerEntry.get() == '' or manufacturingyearEntry.get() == '' or firmwareversionEntry.get() == '' or filamentEntry.get() == '' or maintenancecostEntry.get() =='':
        messagebox.showerror("Error", "You must enter all fields", parent = screen)
    else:            
        currentdate = time.strftime("%d/%m/%Y")
        currenttime = time.strftime("%H:%M:%S")
        try:
            query = 'INSERT INTO printer values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(query, (idEntry.get(), printernameEntry.get(), manufacturerEntry.get(), manufacturingyearEntry.get(), firmwareversionEntry.get(), filamentEntry.get(), maintenancecostEntry.get(), currentdate, currenttime))
            DBcon.commit()
            result = messagebox.askyesno("Data added successfully", "Clean the form?", parent = screen)
            if result:
                idEntry.delete(0, END)
                printernameEntry.delete(0, END)
                manufacturerEntry.delete(0, END)
                manufacturingyearEntry.delete(0, END)
                firmwareversionEntry.delete(0, END)
                filamentEntry.delete(0, END)
                maintenancecostEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror("Error", "ID cannot be duplicated", parent = screen)
                
        query = "SELECT *FROM printer"
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        Printer_table.delete(*Printer_table.get_children())
        for data in fetched_data:
            datalist = list(data)
            Printer_table.insert('', END, values = datalist)
        
def clock():
    date = time.strftime("%d/%m/%Y")
    current_time = time.strftime("%H:%M:%S")
    datetimeLabel.config(text = f'   Date: {date}\nTime: {current_time}')
    datetimeLabel.after(1000,clock)

count = 0
text = ""
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ""
    text = text + s[count]
    sliderLabel.config(text = text)
    sliderLabel.after(250, slider)
    count += 1

def connect_database():
    def connect():
        global mycursor, DBcon
        try:
            DBcon = pymysql.connect(host = hostEntry.get(), user = usernameEntry.get(), password = passwordEntry.get())
            mycursor = DBcon.cursor()

        except:
            messagebox.showerror('Error', "Invalid Details")
            return
        try:    
            query = 'CREATE database 3dprintermanagementsystem'
            mycursor.execute(query)
            query = 'USE 3dprintermanagementsystem'
            mycursor.execute(query)
        except:
            query = 'USE 3dprintermanagementsystem'
            mycursor.execute(query)
        try:
            query = 'CREATE table printer(id int not null primary key, printername varchar(25), manufacturer varchar(25), manufacturingyear varchar(4) , firmwareversion int not null , filament varchar(20), maintenancecost varchar(20), date varchar(20), time varchar(20))'
            mycursor.execute(query)  
        except:
            pass
        messagebox.showinfo("Success", "Database Connection is Successful", parent = DBconnect_window)
        DBconnect_window.destroy()
        add_Printer_Button.config(state = NORMAL)
        search_Printer_Button.config(state = NORMAL)
        delete_Printer_Button.config(state = NORMAL)
        update_Printer_Button.config(state = NORMAL)
        show_Printer_Button.config(state = NORMAL)
        export_Printer_Button.config(state = NORMAL)

    DBconnect_window = Toplevel()
    DBconnect_window.geometry("470x250+730+230")
    DBconnect_window.title("Database Connection")
    DBconnect_window.resizable(0,0)

    hostnameLabel = Label(DBconnect_window, text = "Host Name", font = ("arial", 20, "bold"))
    hostnameLabel.grid(row = 0, column = 0, padx = 20)

    hostEntry = Entry(DBconnect_window, font = ("arial", 15, "bold"), bd = 2)
    hostEntry.grid(row = 0, column = 1, padx = 40, pady = 20)
    
    usernameLabel = Label(DBconnect_window, text = "User Name", font = ("arial", 20, "bold"))
    usernameLabel.grid(row = 1, column = 0, padx = 20)

    usernameEntry = Entry(DBconnect_window, font = ("arial", 15, "bold"), bd = 2)
    usernameEntry.grid(row = 1, column = 1, padx = 40, pady = 20)

    passwordLabel = Label(DBconnect_window, text = "Password", font = ("arial", 20, "bold"))
    passwordLabel.grid(row = 2, column = 0, padx = 20)

    passwordEntry = Entry(DBconnect_window, font = ("arial", 15, "bold"), bd = 2)
    passwordEntry.grid(row = 2, column = 1, padx = 40, pady = 20)

    DBconnectButton = ttk.Button(DBconnect_window, text = "CONNECT", command = connect)
    DBconnectButton.grid(row = 3, columnspan = 2)
window = ttkthemes.ThemedTk()

window.get_themes()

window.set_theme("plastik")

window.geometry("1174x680+50+20")
window.resizable(0,0)
window.title("3D Printer Information Management System")


datetimeLabel = Label(window, text = "Hello", font = ("Time New Romans", 18, "bold"))
datetimeLabel.place(x = 5, y = 5)
clock()
s = "3D Printer Information Management System"
sliderLabel = Label(window, text = s, font = ("Arial", 28, "italic bold"), width = 35)
sliderLabel.place(x = 225, y = 0)
slider()

connectButton = ttk.Button(window, text = "Connect to DB", command = connect_database)
connectButton.place(x = 1050, y = 20)

methods_Frame = Frame(window)
methods_Frame.place(x = 50, y = 80, width = 300, height = 600)

logo_image = PhotoImage(file = "3D-printer.png")
logo_Label = Label(methods_Frame, image = logo_image)
logo_Label.grid(row = 0, column = 0)

add_Printer_Button = ttk.Button(methods_Frame, text = "Add Printer", width = 25, state = DISABLED, command = lambda: toplevel_data("Add Printer", "Add Printer", add_data))
add_Printer_Button.grid(row = 1, column = 0, pady = 20)

search_Printer_Button = ttk.Button(methods_Frame, text = "Search Printer", width = 25, state = DISABLED, command = lambda: toplevel_data("Search Printer", "Search", search_data))
search_Printer_Button.grid(row = 2, column = 0, pady = 20)

delete_Printer_Button = ttk.Button(methods_Frame, text = "Delete Printer", width = 25, state = DISABLED, command = delete_printer)
delete_Printer_Button.grid(row = 3, column = 0, pady = 20)

update_Printer_Button = ttk.Button(methods_Frame, text = "Update Printer", width = 25, state = DISABLED, command = lambda: toplevel_data("Update Printer", "Update", update_data))
update_Printer_Button.grid(row = 4, column = 0, pady = 20)

show_Printer_Button = ttk.Button(methods_Frame, text = "Show Printer", width = 25, state = DISABLED, command = show_printer)
show_Printer_Button.grid(row = 5, column = 0, pady = 20)

export_Printer_Button = ttk.Button(methods_Frame, text = "Export Data",width = 25, state = DISABLED, command = export_data)
export_Printer_Button.grid(row = 6, column = 0, pady = 20)

exit_Button = ttk.Button(methods_Frame, text = "Exit",width = 25, command = exit)
exit_Button.grid(row = 7, column = 0, pady = 20)

data_Frame = Frame(window)
data_Frame.place(x = 350, y = 80, width = 820, height = 600)

scrollbar_hor = Scrollbar(data_Frame, orient = HORIZONTAL)
scrollbar_ver = Scrollbar(data_Frame, orient = VERTICAL)

Printer_table = ttk.Treeview(data_Frame, columns = ("ID","Printer Name", "Manufacturer", "Manufacturing Year", "Firmware Version", "Filament", "Maintenance Cost")
                             ,xscrollcommand = scrollbar_hor.set, yscrollcommand = scrollbar_ver.set)


scrollbar_hor.config(command = Printer_table.xview) 
scrollbar_ver.config(command = Printer_table.yview)

scrollbar_hor.pack(side = BOTTOM, fill = X)
scrollbar_ver.pack(side = RIGHT, fill = Y)

Printer_table.pack(fill = BOTH, expand = 1)

Printer_table.heading('ID', text = "ID")
Printer_table.heading("Printer Name", text = "Printer Name")
Printer_table.heading("Manufacturer", text = "Manufacturer")
Printer_table.heading("Manufacturing Year", text = "Manufacturing Year")
Printer_table.heading("Firmware Version", text = "Firmware Version")
Printer_table.heading("Filament", text = "Filament")
Printer_table.heading("Maintenance Cost", text = "Maintenance Cost (K VND)")
Printer_table.config(show = "headings")

window.mainloop()