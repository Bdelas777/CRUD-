from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
#-----Methods-------
"""Aqui se creo la conexion a la base de datos primeros conectamos a la base usuarios por medio de la conexión 
de ahi usamos un try y un except para evitar errores. En el try hacemos la tabl<a con los datos que pondremos 
 en el except mandamos el aviso de que ya se creo la base de datos"""
def CONNECTDATABASE():
	myConnection=sqlite3.connect("Users")
	myCursor=myConnection.cursor()
	try:
		myCursor.execute('''
			CREATE TABLE USERSDATA(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME VARCHAR(50) UNIQUE,
			SURNAME VARCHAR(50),
			PASSWORD VARCHAR(50),
			DIRECTION VARCHAR(100),
			COMMENTARY VARCHAR(100))
			''')
		messagebox.showinfo("Database","Database are create")
	except:
		messagebox.showwarning("Database","¡Database was created!")

"""Salida de la aplicacion aqui se ejecuta ese metodo"""
def EXITAPLICATION():
	value=messagebox.askokcancel("Exit", "¿Do you want to exit?")
	if value :
		root.destroy()

"""Aqui es el metodo para limpiar los campos"""
def CLEANFIELDS():
	MyId.set("")
	MyName.set("")	
	MySurname.set("")
	MyPassword.set("")
	MyDirection.set("")
	Textcommentary.delete(1.0,END)#Nos marca desde donde queremos borrar hasta el final
"""Funcion para insertar datos del usuario"""
def CREATE():
	myConnection=sqlite3.connect("Users")
	myCursor=myConnection.cursor()
	#Consulta parametrica es metodo corto
	data=MyName.get(),MySurname.get(),MyPassword.get(),MyDirection.get(),Textcommentary.get("1.0",END)
	myCursor.execute("INSERT INTO USERSDATA VALUES(NULL,?,?,?,?,?)",(data))
	'''myCursor.execute("INSERT INTO USERSDATA VALUES(NULL,'"+ miNombre.get() + "','" + miPassword.get() + "','"  +
		miApellido.get() + "','" + miDireccion.get() + "','" + textocomentario.get("1.0",END) + "')")'''
	#forma larga o inyeccion sql de otro ejemplo
	myConnection.commit()
	messagebox.showinfo("Database", "This information was added")

"""Este es el metodo de la creacion de la lectura"""
def READ():
	myConnection=sqlite3.connect("Users")
	myCursor=myConnection.cursor()
	myCursor.execute("SELECT * FROM USERSDATA WHERE ID=" + MyId.get())
	TheUser=myCursor.fetchall()
	for User in TheUser:
		MyId.set(User[0])
		MyName.set(User[1])
		MySurname.set(User[2])
		MyPassword.set(User[3])
		MyDirection.set(User[4])
		Textcommentary.insert(1.0, User[5])
	myConnection.commit()

"""Metodo para la actualizacion de informacion"""
def UPDATE():
	myConnection=sqlite3.connect("Users")
	myCursor=myConnection.cursor()
	data=MyName.get(),MySurname.get(),MyPassword.get(),MyDirection.get(),Textcommentary.get("1.0",END)
	'''miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBE_USUARIO='"+ miNombre.get() + "', PASSWORD='" + miPassword.get() + 
		"', APELLIDO='" + miApellido.get() + "', DIRECCION='" + miDireccion.get() + "', COMENTARIOS='" + textocomentario.get("1.0",END) +
		"' WHERE ID=" + miId.get())'''
	myCursor.execute("UPDATE USERSDATA SET NAME=?,SURNAME=?,SURNAME=?,DIRECTION=?,COMMENTARY=? " +
		" WHERE ID=" + MyId.get(),(data))
	myConnection.commit()
	messagebox.showinfo("Database", "The Database was updated")
#se pone insert para texts

"""Metodo que borra a los usuarios"""
def DELETE():
	myConnection=sqlite3.connect("Users")
	myCursor=myConnection.cursor()
	myCursor.execute("DELETE FROM USERSDATA WHERE ID=" + MyId.get())
	myConnection.commit()
	messagebox.showinfo("Database", "This seccion was deleted")

def AdicionalInformation():
	messagebox.showinfo("This Database was created by Bernardo ", "Database: Version 2021")

def License():
	messagebox.showwarning("License"," This product a has GNU license")

#----- menu creation--------
barraMenu=Menu()
root.title("Database")
MyId=StringVar()
MyName=StringVar()
MySurname=StringVar()
MyPassword=StringVar()
MyDirection=StringVar()

root.iconbitmap("favicon.ico")
root.config(menu=barraMenu,width=300, height=300,bg="#82b4e7", cursor="hand2")
BBDDMenu=Menu(barraMenu, tearoff=0)
BBDDMenu.add_cascade(label="Conect",command=CONNECTDATABASE)
BBDDMenu.add_cascade(label="Exit", command=EXITAPLICATION)

ClearMenu=Menu(barraMenu, tearoff=0)
ClearMenu.add_cascade(label="Clear fields", command=CLEANFIELDS)

CRUDMenu=Menu(barraMenu, tearoff=0)
CRUDMenu.add_cascade(label="Create", command=CREATE)
CRUDMenu.add_cascade(label="Read",command=READ)
CRUDMenu.add_cascade(label="Update", command=UPDATE)
CRUDMenu.add_cascade(label="Delete", command=DELETE)

HelpMenu=Menu(barraMenu, tearoff=0)
HelpMenu.add_cascade(label="License" ,command=License)
HelpMenu.add_cascade(label="About", command=AdicionalInformation)

barraMenu.add_cascade(label="Database", menu=BBDDMenu)
barraMenu.add_cascade(label="Clear", menu=ClearMenu)
barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label="Help", menu=HelpMenu)
#---------------------------field beginnig--------------
Frame1=Frame()
Frame1.pack()
Frame1.config(bg="#700300")
#---------------------------Entry--------------
IDEntry=Entry(Frame1, textvariable=MyId)
IDEntry.grid(row=0,column=1,padx=10,pady=10 )
IDEntry.config(bg="#ffbcca")

NameEntry=Entry(Frame1, textvariable=MyName)
NameEntry.grid(row=1,column=1,padx=10,pady=10)
NameEntry.config(justify="center",fg="gray",bg="#ffbcca")

SurnameEntry=Entry(Frame1, textvariable=MySurname)
SurnameEntry.grid(row=2,column=1,padx=10,pady=10)
SurnameEntry.config(justify="center",fg="gray",bg="#ffbcca")

PasswordEntry=Entry(Frame1, textvariable=MyPassword)
PasswordEntry.grid(row=3,column=1,padx=10,pady=10)
PasswordEntry.config(show="*",justify="right",fg="red")
PasswordEntry.config(bg="#ffbcca")

DirectionEntry=Entry(Frame1, textvariable=MyDirection)
DirectionEntry.grid(row=4,column=1,padx=10,pady=10)
DirectionEntry.config(bg="#ffbcca")

Textcommentary=Text(Frame1,width=16, height=5)
Textcommentary.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(Frame1, command=Textcommentary.yview)
scrollVert.grid(row=5, column=2, sticky="nsew",)#sticky es para ubicar
Textcommentary.config(yscrollcommand=scrollVert.set,bg="#ffbcca")
#-----------Labels------------
IDLabel=Label(Frame1,text="ID: ")
IDLabel.grid(row=0,column=0,padx=10,pady=10,sticky="e")
IDLabel.config(fg="blue",font=("Comic Sans MS",11),bg="#ffbcca")

NameLabel=Label(Frame1,text="Name: ")
NameLabel.grid(row=1,column=0,padx=10,pady=10,sticky="e")
NameLabel.config(fg="blue",font=("Comic Sans MS",11),bg="#ffbcca")

SurnameLabel=Label(Frame1,text="Surname: ")
SurnameLabel.grid(row=2,column=0,padx=10,pady=10,sticky="e")
SurnameLabel.config(fg="blue",font=("Comic Sans MS",11),bg="#ffbcca")

PasswordLabel=Label(Frame1,text="Password: ")
PasswordLabel.grid(row=3,column=0,padx=10,pady=10,sticky="e")
PasswordLabel.config(fg="blue",font=("Comic Sans MS",11),bg="#ffbcca")

DirectionLabel=Label(Frame1,text="Direction: ")
DirectionLabel.grid(row=4,column=0,padx=10,pady=10,sticky="e")
DirectionLabel.config(fg="blue",font=("Comic Sans MS",11),bg="#ffbcca")

CommentaryLabel=Label(Frame1,text="Commentary: ")
CommentaryLabel.grid(row=5,column=0,padx=10,pady=10,sticky="e")
CommentaryLabel.config(fg="blue",font=("Comic Sans MS",11),bg="#ffbcca")
#----------------Buttons------------
Frame2=Frame()
Frame2.pack()
Frame2.config(bg="#700300")
CreateButton=Button(Frame2,text="Create", command=CREATE)
CreateButton.grid(row=0,column=0,padx=10.5,pady=10,sticky="e")
CreateButton.config(fg="blue",font=("Comic Sans MS",10),bg="#ffbcca")

ReadButton=Button(Frame2,text="Read",command=READ)
ReadButton.grid(row=0,column=1,padx=10.5,pady=10,sticky="e")
ReadButton.config(fg="blue",font=("Comic Sans MS",10),bg="#ffbcca")

UpdateButton=Button(Frame2,text="Update",command=UPDATE)
UpdateButton.grid(row=0,column=2,padx=10.5,pady=10,sticky="e")
UpdateButton.config(fg="blue",font=("Comic Sans MS",10),bg="#ffbcca")

DeleteButton=Button(Frame2,text="Delete",command=DELETE)
DeleteButton.grid(row=0,column=3,padx=10.5,pady=10,sticky="e")
DeleteButton.config(fg="blue",font=("Comic Sans MS",10),bg="#ffbcca")
root.mainloop()