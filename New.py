from tkinter import *

from tkinter import messagebox

import json
import os

def raise_frame(frame):
    frame.tkraise()

mydict = {
        "First Name": " ",
        "Last Name":" ",
        "Contact No.":"",
        "Email ID":"",
        "Additional IDs":" ",
        "Address line 1":" ",
        "Address line 2":"",
        "City":" ",
        "State":" ",
        "Zipcode":" ",
        "Country":" ",
        "Availability":" ",
        "Language(s)":" ",
        "Employment status":" "
       
}

root = Tk()

f1 = Frame(root)
f3 = Frame(root)

for frame in (f1, f3):
    frame.grid(row=0, column=0, sticky='news')

#welcome screen
b1 = Button(f1, text='PRESS TO CONTINUE', command=lambda:raise_frame(f3))
b1.pack()
# b1.pack(side='top')

### Screen 3 #####


with open('datatest.json') as f:
    data = json.load(f)
 
# Iteration
global len
len = 0
people_list=[]
for person in data['People']:
    k = (person)
    people_list.append(k)
    len = len+1


print(people_list)
i=0

label_heading = Label(f3, text='Default Data')
label_heading.grid(row = 0, column = 0)

topframe = Frame(f3)
topframe.grid(row = 1, column = 0)

midframe = Frame(f3)
midframe.grid(row = 3, column = 0)

lab1 = Label(midframe, text='First Name: ')
lab2 = Label(midframe, text='Last Name: ')
lab3 = Label(midframe, text='Contact Number: ')
lab4 = Label(midframe, text='Email ID: ')
# lab5 = Label(midframe, text='Additional IDs: ')
# lab6 = Label(midframe, text='Address: ')

lab61 = Label(midframe, text='Address line 1: ')
lab62 = Label(midframe, text='Address line 2: ')
lab63 = Label(midframe, text='City: ')
lab64 = Label(midframe, text='State: ')
lab65 = Label(midframe, text='Zip Code: ')
lab66 = Label(midframe, text='Country: ')


lab7 = Label(midframe, text='Language(s): ')
lab8 = Label(midframe, text='Availability: ')
# lab9 = Label(midframe, text='Date of Birth: ')
lab10 = Label(midframe, text='Employment Status: ')

lab_blank = Label(midframe, text='                          ')
#Use a for loop to keep adding

lab1.grid(row = 0, column = 1)
lab2.grid(row = 1, column = 1)
lab3.grid(row = 2, column = 1)
lab4.grid(row = 3, column = 1)
# lab5.grid(row = 4, column = 1)

# lab6.grid(row = 5, column = 2)

lab61.grid(row = 4, column = 1)
lab62.grid(row = 5, column = 1)
lab63.grid(row = 6, column = 1)
lab64.grid(row = 7, column = 1)
lab65.grid(row = 8, column = 1)
lab66.grid(row = 9, column = 1)

# lab_blank.grid(row = 12, column = 1)

lab7.grid(row = 10, column = 1)
lab8.grid(row = 11, column = 1)
# lab9.grid(row = 12, column = 1)
lab10.grid(row = 12, column = 1)

#Defining input entry variables
f_name = StringVar()
l_name = StringVar()
c_no = StringVar()
e_ID = StringVar()

add_ID1 = StringVar()
add_ID2 = StringVar()

add1 = StringVar()
add2 = StringVar()
cit = StringVar()
stat = StringVar()
zip_cod = StringVar()
count = StringVar()

lang = StringVar()
avail = StringVar()
dob = StringVar()
emp_stat = StringVar()


#Entries can be made here
ent1 = Entry(midframe, textvariable=f_name).grid(row=0, column=2)
ent2 = Entry(midframe, textvariable=l_name).grid(row=1, column=2)
ent3 = Entry(midframe, textvariable=c_no).grid(row=2, column=2)
ent4 = Entry(midframe, textvariable=e_ID).grid(row=3, column=2)

ent51 = Entry(midframe, textvariable=add_ID1).grid(row=4, column=2)
# ent52 = Entry(midframe, textvariable=add_ID2).grid(row=4, column=3)

ent61 = Entry(midframe, textvariable=add1).grid(row=6, column=2)
ent62 = Entry(midframe, textvariable=add2).grid(row=7, column=2)
ent63 = Entry(midframe, textvariable=cit).grid(row=8, column=2)
ent64 = Entry(midframe, textvariable=stat).grid(row=9, column=2)
ent65 = Entry(midframe, textvariable=zip_cod).grid(row=10, column=2)
ent66 = Entry(midframe, textvariable=count).grid(row=11, column=2)

ent7 = Entry(midframe, textvariable=lang).grid(row=12, column=2)
# ent8 = Entry(midframe, textvariable=avail).grid(row=14, column=2)
# ent9 = Entry(midframe, textvariable=dob).grid(row=15, column=2)
# ent10 = Entry(midframe, textvariable=emp_stat).grid(row=16, column=2)

def emailToAll():
    for person in people_list:
        open("data2.json", 'w').write(json.dumps(person))
        os.system("python pdf.py")

def saveAndEmail():
    open("data2.json", 'w').write(json.dumps(people_list[i]))
    os.system("python pdf.py")

def clicked():
    messagebox.showinfo('Check','Button clicked')

def update(i):
    f_name = StringVar(midframe, people_list[i]['First Name'])
    global ent1
    ent1 = Entry(midframe, textvariable=f_name)
    ent1.grid(row=0, column=2)

    global ent2
    l_name = StringVar(midframe, people_list[i]['Last Name'])
    ent2 = Entry(midframe, textvariable=l_name)
    ent2.grid(row=1, column=2)

    global ent3
    c_no = StringVar(midframe, people_list[i]["Contact No."])
    ent3 = Entry(midframe, textvariable=c_no)
    ent3.grid(row=2, column=2)

    global ent4
    e_ID = StringVar(midframe, people_list[i]["Email ID"])
    ent4 = Entry(midframe, textvariable=e_ID)
    ent4.grid(row=3, column=2)

    global ent5
    add_ID1 = StringVar(midframe, people_list[i]["Address line 1"])
    ent5 = Entry(midframe, textvariable=add_ID1)
    ent5.grid(row=4, column=2)

    global ent6
    add_ID2 = StringVar(midframe, people_list[i]["Address line 2"])
    ent6 = Entry(midframe, textvariable=add_ID2)
    ent6.grid(row=5, column=2)

    global ent7
    cit = StringVar(midframe, people_list[i]["City"])
    ent7 = Entry(midframe, textvariable=cit)
    ent7.grid(row=6, column=2)
   
    global ent8
    stat = StringVar(midframe, people_list[i]["State"])
    ent8 = Entry(midframe, textvariable=stat)
    ent8.grid(row=7, column=2)

    global ent9
    zip_cod = StringVar(midframe, people_list[i]["Zipcode"])
    ent9 = Entry(midframe, textvariable=zip_cod)
    ent9.grid(row=8, column=2)

    global ent10
    count = StringVar(midframe, people_list[i]["Country"])
    ent10 = Entry(midframe, textvariable=count)
    ent10.grid(row=9, column=2)

    global ent11
    lang = StringVar(midframe, people_list[i]["Language(s)"])
    ent11 = Entry(midframe, textvariable=lang)
    ent11.grid(row=10, column=2)

    global ent12
    avail = StringVar(midframe, people_list[i]["Availability"])
    ent12 = Entry(midframe, textvariable=avail)
    ent12.grid(row=11, column=2)

    global ent13
    emp_stat = StringVar(midframe, people_list[i]["Employment status"])
    ent13 = Entry(midframe, textvariable=emp_stat)
    ent13.grid(row=12, column=2)

def change():
    global i

    if ent1.get():
        people_list[i]['First Name'] = ent1.get()

    if ent2.get():
#    else:
        people_list[i]['Last Name'] = ent2.get()

    if ent3.get():
#   else:    
        people_list[i]["Contact No."] = ent3.get()

    if ent4.get():
#    else:
        people_list[i]["Email ID"] = ent4.get()

    if ent5.get():
#    else:
        people_list[i]["Address line 1"] = ent5.get()

    if ent6.get():
#    else:
        people_list[i]["Address line 2"] = ent6.get()

    if ent7.get():
#    else:
        people_list[i]["City"] = ent7.get()
   
    if ent8.get():
#    else:
        people_list[i]["State"] = ent8.get()

    if ent9.get():
#    else:
        people_list[i]["Zipcode"] = ent9.get()

    if ent10.get():
#    else:
        people_list[i]["Country"] = ent10.get()

    if ent11.get():
#    else:
        people_list[i]["Language(s)"] = ent11.get()

    if ent12.get():
#    else:
        people_list[i]["Availability"] = ent12.get()

    if ent13.get():
#    else:
        people_list[i]["Employment status"] = ent13.get()


def next():
    global i
    global len
    if (i < len-1):
        i= i+1
    else:
        messagebox.showinfo('Error','Last element reached')
    update(i)
    print('next called')
    print(i)

def previous():
    global i
    if i>=1:
        i=i-1
    else:
        i=0
        messagebox.showinfo('Error','Already on first element')
    update(i)
    print('previous called')
    print(i)

def new():
    print('new called')
    global i
    global people_list
    global len
    if len>1:
        new_list = people_list[0:i+1]+[mydict]+people_list[i+1:]
    else:
        new_list = people_list[0:i+1] + [mydict]
    print(new_list)
    len = len +1
    people_list = new_list
    i = i+1
    update(i)
    print('new executed')

#def save():


def delete():
    print('delete called')
    global i
    global people_list
    global len
    if (i == len - 1):
        new_list = people_list[0:i]
        i = i-1
    else:
        new_list = people_list[0:i]+people_list[i+1:]
    print(new_list)
    people_list = new_list
    update(i)
    len = len-1
    print('delete executed')

update(i)

b_prev = Button(topframe, text='Previous', command = previous)
b_prev.pack(side = LEFT)

b_next = Button(topframe, text='Next', command = next)
b_next.pack(side = LEFT)

b_new = Button(topframe, text='New', command = new)
b_new.pack(side = RIGHT)

b_remove = Button(topframe, text='Delete', command = delete)
b_remove.pack(side = RIGHT)

##midframe = Frame

botframe = Frame(f3)
botframe.grid(row = 4, column = 0)

b_exit = Button(botframe, text='Exit and restart', command=lambda:raise_frame(f1))
b_exit.pack(side = LEFT)

b_save = Button(botframe, text='Save', command = change)
b_save.pack(side = LEFT)

b_sem = Button(botframe, text='Email personally', command = saveAndEmail)
b_sem.pack(side = LEFT)

b_sal = Button(botframe, text='Email to all', command = emailToAll)
b_sal.pack(side = LEFT)

raise_frame(f1)
root.mainloop()
