import mysql.connector as my
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
gui = tk.Tk()
gui.configure(background='#17acb3')
gui.title("ASSIGNMENT-4")
gui.geometry("400x200")
gui.resizable(width=False, height=False)
tab_control = ttk.Notebook(gui)
tab_control.pack(fill=BOTH,expand=True)



def connect_to_database():
    # try except is used for successful database connection
    try:    # create and open database connection
        new_user = user.get()
        new_host = hostName.get()
        new_pswd = passwordV.get()
        new_database = databaseNameV.get()
        mydb = my.connect(
                 host=new_host,
                 user=new_user,
                 passwd=new_pswd,
                database=new_database)
        messagebox.showinfo('Connection','Successful')
        print("Connected Successful")
    except my.Error as e:
        messagebox.showerror('Not successful', e)
        print(e)
    except my.ProgrammingError as e:
        print(e)
    except :
        messagebox.showerror('Not successful', 'try again')






















tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Database')

Label(tab1, text="Connect to MySQL Database", font=45).grid(row=0, column=0,padx=5, pady=5, ipadx=5, ipady=5)
#  create label using grid structure
# Database label to fields
userName = Label(tab1, text="User Name")
password = Label(tab1, text="Password Name")
host = Label(tab1, text="Host Name")
databaseName = Label(tab1, text="Database Name")



userName.grid(row=2, column=0, sticky=W)
password.grid(row=3, column=0, sticky=W)
host.grid(row=4, column=0, sticky=W)
databaseName.grid(row=5, column=0, sticky=W)

user = StringVar()
hostName = StringVar()
passwordV = StringVar()
databaseNameV = StringVar()
# database (INPUT)entry field
userName_value = Entry(tab1,textvariable=user).grid(row=2, column=1)
password_value = Entry(tab1, textvariable=passwordV,show="*").grid(row=3, column=1)
host_value = Entry(tab1,textvariable=hostName).grid(row=4, column=1)
databaseName_value = Entry(tab1,textvariable=databaseNameV).grid(row=5, column=1)

# Button to connect to database
submit_button = tk.Button(tab1,text="Connect",command=connect_to_database,width=16, background="white").grid(row=6, column=0)
close_button = tk.Button(tab1,text="Exit",width=16, command = gui.destroy, background="white").grid(row=6, column=1)



























##################################################################################################################################
###########                                                                                                      #################
##################################################################################################################################
# method to add record to Database
def add_data():
    # cheeseId = (input("Enter Cheese ID:\t "))
    # cheeseName = input("Enter Cheese Name:\t ")
    # mName = input("Enter Manufacturer Name:\t")
    # mProvince = input("Enter Province Name:\t")
    # mType = input("Enter Manufacturer Type:\t")

    # values are sent through parameter in query %s to prevent sql injection
    # execute method is use to run sql query
    # mycursor = mydb.cursor()
    # mycursor.execute(sql, val)
    # mydb.commit()
    new_user = user.get()
    new_host = hostName.get()
    new_pswd = passwordV.get()
    new_database = databaseNameV.get()
    mydb = my.connect(
        host=new_host,
        user=new_user,
        passwd=new_pswd,
        database=new_database)
    sql = "INSERT INTO cheese (cheeseID,cheeseName,mName,mProvince,mType) VALUES (%s,%s,%s,%s,%s)"
    val = (cheeseIdV.get(), cheeseNameV.get(), cheeseManufactureV.get(), cheeseProvinceV.get(), manufactureTypeV.get())
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    cheeseId_value.delete(0,END)
    cheeseName_value.delete(0, END)
    cheeseManufacture_value.delete(0,END)
    cheeseProvince_value.delete(0,END)
    manufacture_type.delete(0, END)
    messagebox.showinfo('Insertion', 'Successful')

    print("***************** Record Inserted Successfully ************************")





tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text = 'Add')
# top Header
Label(tab2, text="Add New Cheese to Database", font=45).grid(row=0, column=0,padx=5, pady=5, ipadx=5, ipady=5)
#  create label using grid structure
cheeseId = Label(tab2, text="Cheese ID",)
cheeseName = Label(tab2, text="Cheese Name")
cheeseManufacture = Label(tab2, text="Cheese Manufacture")
cheeseProvince = Label(tab2, text="Manufacture Province")
manufactureType = Label(tab2, text="Manufacture Type")

cheeseId.grid(row=1, column=0,sticky=W)
cheeseName.grid(row=2, column=0,sticky=W)
cheeseProvince.grid(row=3, column=0,sticky=W)
cheeseManufacture.grid(row=4, column=0,sticky=W)
manufactureType.grid(row=5, column=0,sticky=W)

cheeseIdV=StringVar()
cheeseNameV=StringVar()
cheeseProvinceV=StringVar()
cheeseManufactureV=StringVar()
manufactureTypeV=StringVar()

cheeseId_value= Entry(tab2,textvariable=cheeseIdV)
cheeseId_value.grid(row=1,column=1)
cheeseName_value = Entry(tab2,textvariable=cheeseNameV)
cheeseName_value.grid(row=2, column=1)
cheeseManufacture_value = Entry(tab2,textvariable=cheeseManufactureV)
cheeseManufacture_value.grid(row=3, column=1)
cheeseProvince_value= Entry(tab2,textvariable=cheeseProvinceV)
cheeseProvince_value.grid(row=4, column=1)
manufacture_type= Entry(tab2,textvariable=manufactureTypeV)
manufacture_type.grid(row=5, column=1)
add_button = tk.Button(tab2,text="ADD",command=add_data,width=16, background="white").grid(row=6, column=0)
gui.mainloop()