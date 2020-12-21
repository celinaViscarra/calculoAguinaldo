#Celina Alfaro Viscarra

from tkinter import *
from tkinter import messagebox

#Creación y configuración de ventana
ventana = Tk()
ventana.title("Asignación de Aguinaldo")
ventana.geometry("650x650+350+0") #dimensiones
ventana.configure(background="white")

#Creamos la imagen
image = PhotoImage(file="1.gif")
image = image.subsample(6, 6)
label = Label(image=image)
label.pack()

#etiqueta nombre empleado
nombre = Label(ventana, text="Nombre del empleado: ", bg="dark gray", fg="white", font="14")
nombre.pack(fill=X)
nombre.place(x=50, y=200, width=550, height=30)

name=Entry(ventana, font="Arial 14")
name.pack(padx=5,pady=5,ipady=5,fill=X)
name.place(x=50, y=235, width=550, height=30)

#etiqueta DUI empleado
duiEmpleado = Label(ventana, text="DUI del empleado: ", bg="dark gray", fg="white", font="14")
duiEmpleado.pack(padx=5,pady=5,ipady=5,fill=X)
duiEmpleado.place(x=50, y=270, width=550, height=30)

dui=Entry(ventana, font="Arial 14")
dui.pack(padx=5,pady=5,ipady=5,fill=X)
dui.place(x=50, y=305, width=550, height=30)

#etiqueta NIT empleado
nitEmpleado = Label(ventana, text="NIT del empleado: ", bg="dark gray", fg="white", font="14")
nitEmpleado.pack(padx=5,pady=5,ipady=5,fill=X)
nitEmpleado.place(x=50, y=340, width=550, height=30)

nit=Entry(ventana, font="Arial 14")
nit.pack(padx=5,pady=5,ipady=5,fill=X)
nit.place(x=50, y=375, width=550, height=30)

#etiqueta sueldo empleado
sueldoEmpleado = Label(ventana, text="Sueldo Neto del empleado: ", bg="dark gray", fg="white", font="14")
sueldoEmpleado.pack(padx=5,pady=5,ipady=5,fill=X)
sueldoEmpleado.place(x=50, y=410, width=550, height=30)

sueldo=Entry(ventana, font="Arial 14")
sueldo.pack(padx=5,pady=5,ipady=5,fill=X)
sueldo.place(x=50, y=445, width=550, height=30)


#etiqueta meses trabajdno empleado
mesesT = Label(ventana, text="Meses trabajando del empleado: ", bg="dark gray", fg="white", font="14")
mesesT.pack(padx=5,pady=5,ipady=5,fill=X)
mesesT.place(x=50, y=480, width=550, height=30)

meses=Entry(ventana, font="Arial 14")
meses.pack(padx=5,pady=5,ipady=5,fill=X)
meses.place(x=50, y=515, width=550, height=30)

#ejecucion
def calculo():
	sa=sueldo.get()
	s=int(sa)
	salarioDiario = (s)/30

	if (int(meses.get())) >= 1 and (int(meses.get())) <= 12:
		calculoA = ((salarioDiario)*15)
	elif (int(meses.get())) >= 12 and (int(meses.get())) <= 36:
		calculoA = ((salarioDiario)*15)
	elif (int(meses.get())) >= 36 and (int(meses.get())) <=120:
		calculoA = ((salarioDiario)*19)
	elif int(meses.get())>120:
		calculoA = ((salarioDiario)*21)
	else:
		calculoA = calculoA
	messagebox.showinfo(message="Calculo de aguinaldo:{}".format(calculoA), title="Resultado")

#calculo
aguinaldo = Button(ventana, text="Calcular Aguinaldo", command=calculo,bg="dark gray", fg="white", font="14")
aguinaldo.pack(padx=5,pady=5,ipady=5,fill=X)
aguinaldo.place(x=50, y=575, width=550, height=30)

ventana.mainloop()
