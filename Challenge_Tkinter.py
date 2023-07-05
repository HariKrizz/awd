
from tkinter import *
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Separator 
from PIL import Image, ImageTk

root = Tk()
root.geometry('780x450')
root.title('Tkinter CRUD Ops ') 

pic = Image.open("C:\\Users\\ASUS\\Downloads\\Goldcoastcity.jpg")
pic = pic.resize((780,450))              
pic = ImageTk.PhotoImage(pic)
imgLabel = Label(root, image=pic, bg="grey").pack() 
label1 = Label(text="Registration", bg="navy", fg="WHITE", font=('Fira Code', 38, 'bold'))
label1.place(x=180,y=15)
sep = Separator(root, orient='horizontal')
sep.place(y=100,relwidth=600)

label2 = Label(text="Name  ", bg="slategray", fg="azure", font=('Fira Code', 16, 'bold'))
label2.place(x=40, y=150)
label3 = Label(text="Age   ", bg="slategray", fg="white", font=('Fira Code', 16, 'bold'))
label3.place(x=40, y=200) 
label4 = Label(text="Post  ", bg="slategray", fg="white", font=('Fira Code', 16, 'bold'))
label4.place(x=40, y=250)
label5 = Label(text="Salary", bg="slategray", fg="white", font=('Fira Code', 16, 'bold'))
label5.place(x=40, y=300)

txtName = Entry()
txtName.place(x=180, y=150, height=28,width=200)

txtAge = Entry() 
txtAge.place(x=180, y=200, height=28,width=200)

txtPost = Entry()w
txtPost.place(x=180, y=250, height=28,width=200)

txtSalary = Entry()
txtSalary.place(x=180, y=300, height=28,width=200)    

sep_ver = Separator(root, orient='vertical')
sep_ver.place(x=450,y=140,height=200)

sc = Scrollbar(root)
sc.pack(side=RIGHT, fill=Y)
    
mytext = scrolledtext.ScrolledText(root, width=30,height=10)
mytext.place(x=480,y=150)
sc.config(command=mytext.yview)

def dbInsert():
        
    name = txtName.get()
    age = txtAge.get()
    post = txtPost.get()
    salary = txtSalary.get()

    import pymysql
    con = pymysql.Connect(host="localhost", user="root", password="root", database="avodha")
    cur = con.cursor()

    if (name =="" or age =="" or post =="" or salary ==""):
        messagebox.showwarning("Message", "Fields cannot be Empty!")
    else:
        cur.execute("insert into employee values(id,%s,%s,%s,%s)",(name,age,post,salary))
        con.commit()
        messagebox.showinfo("Info", "Employee Registration completed!")

regBtn = Button(text="CREATE", bg="orangered", fg="white", font=('Corbel', 14, 'bold'), command=dbInsert)
regBtn.place(x=40, y=400)

def dbUpdate():
    
    name = txtName.get()
    age = txtAge.get()
    post = txtPost.get()
    salary = txtSalary.get()

    import pymysql
    con = pymysql.Connect(host="localhost", user="root", password="root", database="avodha")
    cur = con.cursor()

    if (name =="" or age =="" or post =="" or salary ==""):
        messagebox.showwarning("Message", "Fields cannot be Empty!")
    else:
        cur.execute("update employee set age=%s, post=%s, salary=%s where name=%s", (age,post,salary,name))
        con.commit()
        messagebox.showinfo("Message", "Update Completed")
        con.close()

upBtn = Button(text="UPDATE", bg="darkgreen", fg="white", font=('Corbel', 14, 'bold'), command=dbUpdate)
upBtn.place(x=140, y=400)

def dbDelete():
    
    name = txtName.get()
    
    import pymysql
    con = pymysql.Connect(host="localhost", user="root", password="root", database="avodha")
    cur = con.cursor()

    cur.execute("delete from employee where name=%s", (name))
    con.commit()
    messagebox.showinfo("Message", "Employee Info Deleted")
    con.close()

delBtn = Button(text="DELETE", bg="crimson", fg="white", font=('Corbel', 14, 'bold'), command=dbDelete)
delBtn.place(x=240, y=400)

def dbFetch():
    
    name = txtName.get()

    import pymysql
    con = pymysql.Connect(host="localhost", user="root", password="root", database="avodha")
    cur = con.cursor()

    cur.execute("select * from employee where name=%s", (name))
    data = cur.fetchone()
    
    if cur.rowcount == 0 :
        messagebox.showinfo("Employee Details","No Details Found!")
        con.commit()
        con.close()
    else:
        messagebox.showinfo("Employee Details",data)
        con.commit()
        con.close()
   
searchBtn = Button(text="SEARCH", bg="royalblue", fg="white", font=('Corbel', 14, 'bold'), command=dbFetch)
searchBtn.place(x=340, y=400)

def dbFetchAll():
    
   
    import pymysql
    con = pymysql.Connect(host="localhost", user="root", password="root", database="avodha")
    cur = con.cursor()

    cur.execute("select * from employee")
    data = cur.fetchall()
    datas = [','.join(map(str,val)) for val in data]

   

    if cur.rowcount == 0 :
        messagebox.showinfo("Employee Details","No Details Found!")
        con.commit()
        con.close()
    else:
        mytext.delete('1.0',END)
        for i in datas:
            mytext.insert(INSERT,('%s\n\n' %i))

fetchBtn = Button(text="VIEW ALL", bg="Maroon", fg="white", font=('Corbel', 14, 'bold'), command=dbFetchAll)
fetchBtn.place(x=480, y=400)

def  clearAll():

    txtName.delete(0,'end')
    txtAge.delete(0,'end')
    txtPost.delete(0,'end')
    txtSalary.delete(0,'end')
   
delBtn = Button(text="CLEAR ", bg="navy", fg="white", font=('Corbel', 14, 'bold'), command=clearAll)
delBtn.place(x=648, y=400)

root.mainloop()