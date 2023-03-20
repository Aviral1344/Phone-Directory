import mysql.connector as mys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from itertools import count

def new_contact():

    def clear():
        name_ent.delete(0,'end')
        country_ent.delete(0,'end')
        code_ent.delete(0,'end')
        ph_no_ent.delete(0,'end')
        address_ent.delete(0,'end')
        

    def Submit():
        name_=name_ent.get()
        country_=country_ent.get()
        code_=code_ent.get()
        ph_no_=ph_no_ent.get()
        address_=address_ent.get()

        try:
            myconn=mys.connect(host='localhost', user="root",password="satyapr1",database="phonebook")
            
            mycur=myconn.cursor()
            
            if myconn.is_connected():
                print("Connection Successful")
            else:
                print("Connection Unsuccessful")
                
            a="select * from phbook"
            mycur.execute(a)
            
            data=mycur.fetchall()
            for i in data:
                print(i)
            
            n=mycur.rowcount
            indx=n+1
            
            c="insert into phbook values({},'{}','{}','{}','{}','{}')".format(indx, name_, country_, code_, ph_no_, address_)
            mycur.execute(c)
            myconn.commit()
            a="select * from phbook"
            mycur.execute(a)
            
            data=mycur.fetchall()
            for i in data:
                print(i)
            
            mycur.close()
            myconn.close()
            mess="Your index No. is {}".format(indx)
            tk.messagebox.showinfo(title="", message=mess)
            
        except Exception as e:
            print(e)
            
    n_contact=tk.Tk(className="New Contact(Phonebook Management System")
    n_contact.geometry("330x250")
    n_contact.resizable(width=False, height=False)
    
    lb_bg= tk.Label(n_contact, bg="#1dc5ff", width=1000, height=1000)
    lb_bg.place(x=1,y=1)
    
    
    name= tk.Label(n_contact, text="Name-",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    name_ent= tk.Entry(n_contact, width =25, fg="black", font=("Times New Roman Bold", 10))
    name.place(x=20,y=10)
    name_ent.place(x=120,y=10)
    
    country= tk.Label(n_contact, text="Country-",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    country_ent= tk.Entry(n_contact, width =25, fg="black", font=("Times New Roman Bold", 10))
    country.place(x=20,y=40)
    country_ent.place(x=120,y=40)
    
    code= tk.Label(n_contact, text="Country Code-",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    code_ent= tk.Entry(n_contact, width =25, fg="black", font=("Times New Roman Bold", 10))
    code.place(x=20,y=70)
    code_ent.place(x=120,y=70)
    
    ph_no= tk.Label(n_contact, text="Phone no.-",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    ph_no_ent= tk.Entry(n_contact, width =25, fg="black", font=("Times New Roman Bold", 10))
    ph_no.place(x=20,y=100)
    ph_no_ent.place(x=120,y=100)
    
    address= tk.Label(n_contact, text="Address-",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    address_ent= tk.Entry(n_contact, width =25, fg="black", font=("Times New Roman Bold", 10))
    address.place(x=20,y=130)
    address_ent.place(x=120,y=130)
    
    submit= tk.Button(n_contact, text="Submit",width=15,bg="Black",fg="white",activebackground="sky blue", command= Submit)
    submit.place(x=30,y=160)
    
    clear=  tk.Button(n_contact, text="Clear",width=15,bg="Black",fg="white",activebackground="sky blue", command= clear)
    clear.place(x=160,y=160)


def look_up():
    
    def clear():
        indx_ent.delete(0,'end')
        name_ent.delete(0,'end')
        country_ent.delete(0,'end')
        code_ent.delete(0,'end')
        ph_no_ent.delete(0,'end')
        address_ent.delete(0,'end')
    
    def search_em():
        index_no=indx_ent.get()
        try:
            myconn=mys.connect(host='localhost',user="root",password="satyapr1",database="phonebook")
            
            mycur=myconn.cursor()
            
            if myconn.is_connected():
                print("connection successful")
            else:
                print("Connection not made")
            
            
            cmd="select * from phbook where index_no={}".format(index_no)
            print(cmd)
            mycur.execute(cmd)
            data=mycur.fetchone()
            myconn.commit()
            print(data)
            
            name=data[1]
            country=data[2]
            code= data[3]
            ph_no=data[4]
            address=data[5]
            
            name_ent.insert(END,name)
            country_ent.insert(END,country)
            code_ent.insert(END,code)
            ph_no_ent.insert(END,ph_no)
            address_ent.insert(END,address)
            
             
        except Exception as e:
            print(e)
    
    lookup=tk.Tk(className="Search Contact")
    lookup.geometry("350x320")
    lookup.resizable(width=False, height=False)
    
    lb_bg= tk.Label(lookup,bg= "#1dc5ff", width=1000, height=1000)
    lb_bg.place(x=1,y=1)
    
    indx= tk.Label(lookup, text="Index No. -",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    indx_ent= tk.Entry(lookup, width =25, fg="black", font=("Times New Roman Bold", 10))
    indx.place(x=50,y=10)
    indx_ent.place(x=120,y=10)
    
    
    search=tk.Button(lookup,text="Search",width=15,bg="Black",fg="white", activebackground="sky blue",command= search_em)
    search.place(x=100,y=40)
    
    clear= tk.Button(lookup, text="Clear",width=15,bg="Black",fg="white",activebackground="sky blue", command= clear)
    clear.place(x=230,y=40)
    
    info= tk.Label(lookup, text="CONTACT INFORMATION",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    info.place(x=100,y=70)
    
    name= tk.Label(lookup, text="Name",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    name_ent= tk.Entry(lookup, width =25, fg="black",bg= "#1dc5ff", font=("Times New Roman Bold", 10))
    name.place(x=20,y=100)
    name_ent.place(x=120,y=100)
    
    country= tk.Label(lookup, text="Country",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    country_ent= tk.Entry(lookup, width =25, fg="black",bg= "#1dc5ff", font=("Times New Roman Bold", 10))
    country.place(x=20,y=130)
    country_ent.place(x=120,y=130)
    
    code= tk.Label(lookup, text="Country Code",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    code_ent= tk.Entry(lookup, width =25, fg="black",bg= "#1dc5ff", font=("Times New Roman Bold", 10))
    code.place(x=20,y=160)
    code_ent.place(x=120,y=160)
    
    ph_no= tk.Label(lookup, text="Phone no.",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    ph_no_ent= tk.Entry(lookup, width =25, fg="black",bg= "#1dc5ff", font=("Times New Roman Bold", 10))
    ph_no.place(x=20,y=190)
    ph_no_ent.place(x=120,y=190)
    
    address= tk.Label(lookup, text="Address",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    address_ent= tk.Entry(lookup, width =25, fg="black",bg= "#1dc5ff", font=("Times New Roman Bold", 10))
    address.place(x=20,y=220)
    address_ent.place(x=120,y=220)

def delete_contact():
    
    def del_em():
        index_no=indx_ent.get()
        try:
            myconn=mys.connect(host='localhost',
                               user="root",
                               password="satyapr1",
                               database="phonebook")
            
            mycur=myconn.cursor()
            
            if myconn.is_connected():
                print("connection successful")
            else:
                print("Connection not made")
            
            
            cmd="DELETE FROM phbook WHERE index_no={}".format(index_no)
            print(cmd)
            mycur.execute(cmd)
            myconn.commit()
            
            tk.messagebox.showinfo(title="", message="Contact Deleted")
            
        except Exception as e:
            print(e)
        

    del_c=tk.Tk(className="Delete contact")
    del_c.geometry("350x320")
    del_c.resizable(width=False, height=False)
    
    lb_bg= tk.Label(del_c,bg= "#1dc5ff", width=1000, height=1000)
    lb_bg.place(x=1,y=1)
    
    indx= tk.Label(del_c, text="Index No. -",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    indx_ent= tk.Entry(del_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    indx.place(x=50,y=10)
    indx_ent.place(x=120,y=10)
    
    del_it=tk.Button(del_c,text="Delete Contact",
                     width=15,bg="Black",fg="white", activebackground="sky blue",
                     command= del_em)
    del_it.place(x=120,y=40)

def edit_contact():
    
    def clear():
        indx_ent.delete(0,'end')
        name_ent.delete(0,'end')
        country_ent.delete(0,'end')
        code_ent.delete(0,'end')
        ph_no_ent.delete(0,'end')
        address_ent.delete(0,'end')
    
    def srch():
        index_no=indx_ent.get()
        try:
            myconn=mys.connect(host='localhost',
                               user="root",
                               password="satyapr1",
                               database="phonebook")
            
            mycur=myconn.cursor()
            
            if myconn.is_connected():
                print("connection successful")
            else:
                print("Connection not made")
        
            cmd="select * from phbook where index_no={}".format(index_no)
            print(cmd)
            mycur.execute(cmd)
            data=mycur.fetchone()
            myconn.commit()
            print(data)
            
            name=data[1]
            country=data[2]
            code= data[3]
            ph_no=data[4]
            address=data[5]
            
            name_ent.insert(END,name)
            country_ent.insert(END,country)
            code_ent.insert(END,code)
            ph_no_ent.insert(END,ph_no)
            address_ent.insert(END,address)
        
        except Exception as e:
            print(e)
            
    def edit_():
        index_no=indx_ent.get()
        name_=name_ent.get()
        country_=country_ent.get()
        code_=code_ent.get()
        ph_no_=ph_no_ent.get()
        address_=address_ent.get()
        
        try:
            myconn=mys.connect(host='localhost', user="root", password="satyapr1", database="phonebook")
            mycur=myconn.cursor()
            
            if myconn.is_connected():
                print("connection successful")
            else:
                print("Connection not made")
                
            cmd="UPDATE phbook SET name='{}',country='{}',code='{}',ph_no='{}',address='{}' WHERE index_no={}".format(name_,country_,code_,ph_no_,address_,index_no)
            print(cmd)
            mycur.execute(cmd)
            myconn.commit()
            
            tk.messagebox.showinfo(title="", message="Contact Edited")    
        
        except Exception as e:
            print(e)
    
    edit_c=tk.Tk(className="Edit contact")
    edit_c.geometry("350x320")
    edit_c.resizable(width=False, height=False)
    
    lb_bg= tk.Label(edit_c,bg= "#1dc5ff", width=1000, height=1000)
    lb_bg.place(x=1,y=1)
    
    indx= tk.Label(edit_c, text="Index No. -",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    indx_ent= tk.Entry(edit_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    indx.place(x=50,y=10)
    indx_ent.place(x=120,y=10)
    
    srch_it=tk.Button(edit_c,text="Search", width=15,bg="Black",fg="white", activebackground="sky blue", command= srch)
    srch_it.place(x=120,y=40)
    
    name= tk.Label(edit_c, text="Name-",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    name_ent= tk.Entry(edit_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    name.place(x=20,y=70)
    name_ent.place(x=120,y=70)
    
    country= tk.Label(edit_c, text="Country-",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    country_ent= tk.Entry(edit_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    country.place(x=20,y=100)
    country_ent.place(x=120,y=100)
    
    code= tk.Label(edit_c, text="Country Code-",fg="white",font=("Times New Roman Bold", 10), bg= "#1dc5ff")
    code_ent= tk.Entry(edit_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    code.place(x=20,y=130)
    code_ent.place(x=120,y=130)
    
    ph_no= tk.Label(edit_c, text="Phone no.-",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    ph_no_ent= tk.Entry(edit_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    ph_no.place(x=20,y=160)
    ph_no_ent.place(x=120,y=160)
    
    address= tk.Label(edit_c, text="Address-",fg="white",font=("Times New Roman Bold", 10),bg= "#1dc5ff")
    address_ent= tk.Entry(edit_c, width =25, fg="black", font=("Times New Roman Bold", 10))
    address.place(x=20,y=190, height=20)
    address_ent.place(x=120,y=190)
    
    edit= tk.Button(edit_c, text="Edit",width=15,bg="Black",fg="white",activebackground="sky blue",command= edit_)
    edit.place(x=30,y=230)
    
    clear=  tk.Button(edit_c, text="Clear",width=15,bg="Black",fg="white",activebackground="sky blue",command= clear)
    clear.place(x=160,y=230)
    

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open('loading gif.gif')
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def menu():
    menu_GUI=tk.Tk(className="Phonebook Management System",)
    menu_GUI.geometry("586x440")
    menu_GUI.resizable(width=False, height=False)
    
    lbl = ImageLabel(menu_GUI)
    lbl.pack()
    lbl.load('loading gif.gif')
    
    m_info=tk.Label(menu_GUI,text ="Choose An Option",fg="white", bg= "#1dc5ff",font=("Times New Roman Bold", 40) )
    m_info.place(x=10,y=10)
            
    new= tk.Button(menu_GUI, text="New Contact",width=15,bg="white",fg="#1dc5ff",activebackground="#536078", command= new_contact)
    new.place(x=100,y=80)
            
    lookup= tk.Button(menu_GUI, text="Lookup",width=15,bg="white",fg="#1dc5ff",activebackground="#536078", command= look_up)
    lookup.place(x=220,y=80)
            
    delete= tk.Button(menu_GUI, text="Delete contact",width=15,bg="white",fg="#1dc5ff",activebackground="#536078", command= delete_contact)
    delete.place(x=340,y=80)
                
    edit= tk.Button(menu_GUI, text="Edit Contact",width=15,bg="white",fg="#1dc5ff",activebackground="#536078", command=edit_contact)
    edit.place(x=460,y=80)
        
    close= tk.Button(menu_GUI, text = "Close",width=10,bg="white",fg="#1dc5ff",activebackground="#536078", command =  menu_GUI.destroy)
    close.place(x=480,y=400)
    
    menu_GUI.mainloop()
menu()