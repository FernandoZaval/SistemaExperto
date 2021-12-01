from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
	
	app = Tk()
	app.title("Sistema experto financiero")
	app.resizable(0,0)
	app.iconbitmap("icon.ico")
	
	def cambiar_frame(Frame,patrimonio):
		Frame.destroy()
		Frame_2.pack()

		if patrimonio == 0:
			LabelRenta.pack()
			EntryPagoRenta.pack()
			BotonRenta.pack()
		elif patrimonio == 1:
			LabelCasaPropia.pack()
			BotonCasaPropia.pack()
		elif patrimonio == 2:
			LabelHipoteca.pack()
			EntryPagoHipoteca.pack()
			Label_agnos_por_pagar.pack()
			EntryAgniosHipoteca.pack()
			BotonHipo.pack()

		

	def cerrar():
		app.destroy()

	def cambiar_frame_Renta(Frame,sexo,edad,EstCivil,Sueldo,SegSoc,Renta):
		Frame.destroy()
		Frame_3.pack()

		Nivel_de_ingreso = 0
		

		if edad > 17 and edad < 31 :
			Label_Con_0.pack()
		elif edad > 30 and edad < 46:
			Label_Con_1.pack()
		elif edad > 45 and edad < 56:
			Label_Con_2.pack()
		elif edad > 55 and edad < 66:
			Label_Con_3.pack()

		if Sueldo < 4251:
			Label_Con_14.pack()
		elif Sueldo > 4250 and Sueldo < 12753:
			Label_Con_15.pack()
		elif Sueldo > 12752 and Sueldo < 21255:
			Label_Con_16.pack()
		elif Sueldo > 21254 and Sueldo < 21757:
			Nivel_de_ingreso = 1
		elif Sueldo > 21756 and Sueldo < 42510:
			Nivel_de_ingreso = 2
		elif Sueldo > 42509:
			Label_Con_17.pack()


		if EstCivil == 0 and Nivel_de_ingreso != 0:
			Label_Con_7.pack()

		if EstCivil == 1 and Nivel_de_ingreso == 2:
			Label_Con_8.pack()

		if EstCivil == 0 and SegSoc == 0 and Nivel_de_ingreso != 0:
			Label_Con_12.pack()

		if SegSoc == 0 and Nivel_de_ingreso == 0:
			Label_Con_13.pack.pack()

	def cambiar_frame_Hipoteca(Frame,sexo,edad,agniosHip,EstCivil,Sueldo,SegSoc,PagoHipo,):
		Frame.destroy()
		Frame_3.pack()

		Nivel_de_ingreso = 0
		RHI = PagoHipo/Sueldo
		

		if edad > 17 and edad < 31 :
			Label_Con_0.pack()
		elif edad > 30 and edad < 46:
			Label_Con_1.pack()
		elif edad > 45 and edad < 56:
			Label_Con_2.pack()
		elif edad > 55 and edad < 66:
			Label_Con_3.pack()

		if agniosHip < 5:
			Label_Con_4.pack()
		elif agniosHip > 4 and agniosHip < 16:
			Label_Con_5.pack()
		elif agniosHip > 20:
			Label_Con_6.pack()


		if RHI <= .4:
			Label_Con_9.pack()
		elif (.4 < RHI <= .5):
			Label_Con_10.pack()	
		elif RHI >.5:
			Label_Con_10.pack()


		if Sueldo < 4251:
			Label_Con_14.pack()
		elif Sueldo > 4250 and Sueldo < 12753:
			Label_Con_15.pack()
		elif Sueldo > 12752 and Sueldo < 21255:
			Label_Con_16.pack()
		elif Sueldo > 21254 and Sueldo < 21757:
			Nivel_de_ingreso = 1
		elif Sueldo > 21756 and Sueldo < 42510:
			Nivel_de_ingreso = 2
		elif Sueldo > 42509:
			Label_Con_17.pack()

		if EstCivil == 0 and Nivel_de_ingreso != 0:
			Label_Con_7.pack()

		if EstCivil == 1 and Nivel_de_ingreso == 2:
			Label_Con_8.pack()

		if EstCivil == 0 and SegSoc == 0 and Nivel_de_ingreso != 0:
			Label_Con_12.pack()

		if SegSoc == 0 and Nivel_de_ingreso == 0:
			Label_Con_13.pack.pack()

	def cambiar_frame_Casa_propia(Frame,sexo,edad,EstCivil,Sueldo,SegSoc):
		Frame.destroy()
		Frame_3.pack()

		Nivel_de_ingreso = 0
		

		if edad > 17 and edad < 31 :
			Label_Con_0.pack()
		elif edad > 30 and edad < 46:
			Label_Con_1.pack()
		elif edad > 45 and edad < 56:
			Label_Con_2.pack()
		elif edad > 55 and edad < 66:
			Label_Con_3.pack()

		if agniosHip < 5:
			Label_Con_4.pack()
		elif agniosHip > 4 and agniosHip < 16:
			Label_Con_5.pack()
		elif agniosHip > 20:
			Label_Con_6.pack()



		if Sueldo < 4251:
			Label_Con_14.pack()
		elif Sueldo > 4250 and Sueldo < 12753:
			Label_Con_15.pack()
		elif Sueldo > 12752 and Sueldo < 21255:
			Label_Con_16.pack()
		elif Sueldo > 21254 and Sueldo < 21757:
			Nivel_de_ingreso = 1
		elif Sueldo > 21756 and Sueldo < 42510:
			Nivel_de_ingreso = 2
		elif Sueldo > 42509:
			Label_Con_17.pack()

		if EstCivil == 0 and Nivel_de_ingreso != 0:
			Label_Con_7.pack()

		if EstCivil == 1 and Nivel_de_ingreso == 2:
			Label_Con_8.pack()

		if EstCivil == 0 and SegSoc == 0 and Nivel_de_ingreso != 0:
			Label_Con_12.pack()

		if SegSoc == 0 and Nivel_de_ingreso == 0:
			Label_Con_13.pack.pack()


		



	Frame_1 = Frame()
	Frame_1.pack()
	Frame_2 = Frame()
	Frame_3 = Frame()

	#-------------------Preguntas/Frame 1----------------------------------------------------------------------------
	
	Label(Frame_1, text="Bienvenido al sistema experto que te ayudará conocer mejor tu situación financiera y te dará consejos de como mejorar tu situación actúal.", font=('Helvetica', 18, "bold")).pack(side="top",pady=10,padx=10)
	Label(Frame_1, text="Cuestionario para recabar información", font=('Helvetica', 15, "bold")).pack(side="top", pady=5)

	Label(Frame_1,text="Ingresa tu sexo",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	radioValueSexo = IntVar()
	Radiobutton(Frame_1,text="Masculino",variable=radioValueSexo,value=0).pack(side="top")
	Radiobutton(Frame_1,text="Femenino",variable=radioValueSexo,value=1).pack(side="top")

	Label(Frame_1,text="Ingresa tu edad en números",font=('Helvetica', 15)).pack(side = "top")
	Edad = StringVar()
	Entry(Frame_1, textvariable= Edad).pack()

	Label(Frame_1,text="Ingresa tu estado civil",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	radioValueEstadoCivil = IntVar() 
	Radiobutton(Frame_1,text="Soltero",variable=radioValueEstadoCivil,value=0).pack(side="top")
	Radiobutton(Frame_1,text="Casado",variable=radioValueEstadoCivil,value=1).pack(side="top")

	Label(Frame_1,text="Ingresa tus ingresos mensuales netos con números",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	Salario= StringVar()
	Entry(Frame_1,textvariable = Salario).pack()

	Label(Frame_1,text="¿Fumas?",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	radioValueTabaco = IntVar() 
	Radiobutton(Frame_1,text="No",variable=radioValueTabaco,value=0).pack(side="top")
	Radiobutton(Frame_1,text="Sí",variable=radioValueTabaco,value=1).pack(side="top")

	Label(Frame_1,text="Ingresa tus peso en kilogramos",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	Peso = StringVar()
	Entry(Frame_1,textvariable = Peso).pack()

	Label(Frame_1,text="Ingresa tus estatura en centimetros",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	Altura= StringVar()
	Entry(Frame_1,textvariable = Altura).pack()

	Label(Frame_1,text="Selecciona la opción que describe tu seguridad social",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	radioValueSegSocial = IntVar()
	Radiobutton(Frame_1,text="No tengo seguridad social de ningún tipo",variable=radioValueSegSocial,value=0).pack(side="top")
	Radiobutton(Frame_1,text="Sí tengo seguridad social",variable=radioValueSegSocial,value=1).pack(side="top")

	Label(Frame_1,text="Selecciona la opción que describe tu situación",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
	radioValuePatrimonio = IntVar()
	Radiobutton(Frame_1,text="Rento",variable=radioValuePatrimonio,value=0).pack(side="top")
	Radiobutton(Frame_1,text="Tengo casa propia pagada",variable=radioValuePatrimonio,value=1).pack(side="top")
	Radiobutton(Frame_1,text="Pagando mi hipoteca",variable=radioValuePatrimonio,value=2).pack(side="top")






	Button(Frame_1, text="Continuar",command=lambda: cambiar_frame(Frame_1,radioValuePatrimonio.get())).pack(side="bottom", pady=10,padx=10)

	#------------------------Preguntas/Frame 2-----------------------------------------------------------------------------

	LabelRenta = Label(Frame_2, text="Ingresa el costo de tu renta por mes",font=('Helvetica', 15))
	LabelHipoteca = Label(Frame_2, text="Ingresa el costo de tu hipoteca por mes",font=('Helvetica', 15))
	LabelCasaPropia = Label(Frame_2, text="Presiona Enviar para conocertus resultados",font=('Helvetica', 15))
	Label_agnos_por_pagar = Label(Frame_2, text="Introduce los años que te faltan para pagar la hipoteca",font=('Helvetica', 15))

	PagoRenta = StringVar()
	EntryPagoRenta = Entry(Frame_2,textvariable = PagoRenta)
	PagoHipoteca = StringVar()
	EntryPagoHipoteca = Entry(Frame_2,textvariable = PagoHipoteca)
	AgniosHipoteca = StringVar()
	EntryAgniosHipoteca = Entry(Frame_2,textvariable = AgniosHipoteca)



	BotonRenta = Button(Frame_2, text="Enviar",command=lambda: cambiar_frame_Renta(Frame_2,radioValueSexo.get(),int(Edad.get()), radioValueEstadoCivil.get(), int(Salario.get()), radioValueSegSocial.get() , int(PagoRenta.get()) ))
	BotonHipo = Button(Frame_2, text="Enviar",command=lambda: cambiar_frame_Hipoteca(Frame_2,radioValueSexo.get(),int(Edad.get()), int(AgniosHipoteca.get()) ,radioValueEstadoCivil.get(), int(Salario.get()), radioValueSegSocial.get() , int(PagoHipoteca.get()) ))
	BotonCasaPropia = Button(Frame_2, text="Enviar",command=lambda: cambiar_frame_Casa_propia(Frame_2,radioValueSexo.get(),int(Edad.get()), radioValueEstadoCivil.get(), int(Salario.get()), radioValueSegSocial.get() ))
																										




	#---------------------------Resultados/Frame 3------------------------------------------------------------------

	Label(Frame_3, text="Resultados", font=('Helvetica', 15, "bold")).pack(side="top", pady=5)

	A = "Tu edad es la adecuada para iniciar la formación de un patrimonio. Aunque se ve lejos, es tambien una edad indicada para sentar las bases de tu retiro"
	B = "Tu edad es la adecuada para iniciar la formación de un patrimonio. Aunque se ve lejos, es tambien una edad indicada para sentar las bases de tu retiro. En tu edad, tu patrimonio debería ya estar en proceso de consolidación"
	C = "A tu edad tu patrimonio destinado para tu retiro debería estar maduro, incrementándose conforme tus planes financieros."
	D = "A tu edad t patrimonio para el retiro debería estar listo para ser utilizado en el momento de tu jubilación" 
	E = "Estás en la última etapa del pago de tu crédito hipotecario. Es recomendable visualizar el destino que darás a los recursos que hoy destinas al pago de la hipoteca,por ejemplo en inversiones, negocios o un segundo crédito hipotecario."
	F = "Ya superaste los primeros años del pago de tu hipoteca, pero aún falta un largo tramo por recorrer. Es importante la disciplina en el control de tus gastos no endeudarte ni adquirir otros compromisos para no arriesgar tu patrimonio."
	G = "Apenas has cubierto los primeros años de tu crédito hipotecario. Considera que por un tiempo importante, éste será un compromiso importante que deberás atender puntualmente. No lo arriesgues con deuda innecesaria ni gastos superfluos."
	H = "Es recomendable hacer una inversión en un bien inmueble procurando que la proporción de un posible crédito hipotecario no supere el 40%/ de tus ingresos"
	I = "Es recomendable hacer una revisión y ajuste de tus gastos y hacer una inversión inmobiliaria que te permita contar con un bien inmueble, que le dará seguridad a tu patrimionio"
	J = "La proporción de tu pago hipotecario con relación de tus ingresos es adecuada. Es deseable mantenerla en ese nivel para no poner en riesgo tu estabilidad ecónomica."
	K = "La proporción de tu pago hipotecario con relación a tus ingresos es alta. Es recomendable buscar disminuirla y mantener una férrea disciplina en el control de tus gastos"
	L = "La proporción de tu pago hipotecario con relación a tus ingresos es demasiado elevada. Es  urgente que la disminuyas, ya sea renegociando tus pagos o aumentando tus ingresos."
	M = "Para conservar tu tranquilidad financiera en caso de un imprevisto de salud, es recomendable contar con un seguro de gastos médicos mayores. Además de ser deducible de impuestos te dará tranquilidad  ante una enfermedad catastrófica."
	N = "Es recomendable contar con la proteccion de un seguro médico o de gastos médicos mayores para evitar una catástrofe financiera ante un problema de saluda crónico tuyo o de un familiar y contar con una estrategia privada de ahorro para el retiro."
	O = "Tu nivel de ingresos es apenas de un salario mínimo. En estas condiciones el nivel de vida de una persona es muy limitado. Es recomendado buscar una actividad adicional que te genere un segundo ingreso."
	P = "Tu nivel de ingresos está por dentro del promedio para la población en México. Sin embargo debes mantener una alta disciplina en el control de tus gastos"
	Q = "Tu nivel de ingresos te permite generar diversas opciones de ahorro e inversión. Explora las mejores posibilidades para ti."
	R = "Tu nivel de ingresos es elevado. Es recomendable mantener bajo control tus gastos generar ahorro, invertir tus recusos en la opción que mejor te acomode tu situación"


	Label_Con_0 = Label(Frame_3,text= A,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_1 = Label(Frame_3,text= B,font=('Helvetica', 15),wraplength = 500)
	Label_Con_2 = Label(Frame_3,text= C,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_3 = Label(Frame_3,text= D,font=('Helvetica', 15),wraplength = 500)
	Label_Con_4 = Label(Frame_3,text= E,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_5 = Label(Frame_3,text= F,font=('Helvetica', 15),wraplength = 500)
	Label_Con_6 = Label(Frame_3,text= G,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_7 = Label(Frame_3,text= H,font=('Helvetica', 15),wraplength = 500)
	Label_Con_8 = Label(Frame_3,text= I,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_9 = Label(Frame_3,text= J,font=('Helvetica', 15),wraplength = 500)
	Label_Con_10 = Label(Frame_3,text= K,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_11 = Label(Frame_3,text= L,font=('Helvetica', 15),wraplength = 500)
	Label_Con_12 = Label(Frame_3,text= M,font=('Helvetica', 15),wraplength = 500)
	Label_Con_13 = Label(Frame_3,text= N,font=('Helvetica', 15),wraplength = 500) 
	Label_Con_14 = Label(Frame_3,text= O,font=('Helvetica', 15),wraplength = 500)
	Label_Con_15 = Label(Frame_3,text= P,font=('Helvetica', 15),wraplength = 500)
	Label_Con_16 = Label(Frame_3,text= Q,font=('Helvetica', 15),wraplength = 500)
	Label_Con_17 = Label(Frame_3,text= R,font=('Helvetica', 15),wraplength = 500) 
	



	




	Button(Frame_3, text="Cerrar",command=lambda: cerrar()).pack(side="bottom", pady=10,padx=10)

	
	





	app.mainloop()