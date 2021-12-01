from tkinter import ttk
try:
    import Tkinter  as tk
except:
    import tkinter as tk

Salario = ""
global radioValueSexo
global radioValueEstadoCivil
global radioValueTabaco 
global Peso 
global Altrura 
global PrecioRenta 
prueba = 0
hola = "15"



A = "Tu edad es la adecuada para iniciar la formación de un patrimonio. Aunque se ve lejos , es tambien una edad indicada para sentar las bases de tu retiro"
B = "Tu edad es la adecuada para iniciar la formación de un patrimonio. Aunque se ve lejos , es tambien una edad indicada para sentar las bases de tu retiro. En tu edad, tu patrimonio debería ya estar en proceso de consolidación"
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
P = "Tu nivel de ingresos está por dentro del promedio para la población en México. Sin embargo debes mantener una alta disciplina en el control de tus gastos."
Q = "Tu nivel de ingresos te permite generar diversas opciones de ahorro e inversión. Explora las mejores posibilidades para ti."
R = "Tu nivel de ingresos es elevado. Es recomendable mantener bajo control tus gastos generar ahorro, invertir tus recusos en la opción que mejor te acomode tu situación"


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def close(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            app.destroy()
        
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Bienvenido al sistema experto que te ayudará conocer mejor tu situación financiera y te dará consejos de como mejorar tu situación actúal.", font=('Helvetica', 18, "bold")).pack(side="top",pady=10,padx=10)
        tk.Button(self, text="Iniciar ahora",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=10,padx=10)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Cuestionario para recabar información", font=('Helvetica', 15, "bold")).pack(side="top", pady=5)

        tk.Label(self,text="Ingresa tu sexo",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)

        radioValueSexo = tk.IntVar() 
        tk.Radiobutton(self,text="Masculino",variable=radioValueSexo,value=0).pack(side="top")
        tk.Radiobutton(self,text="Femenino",variable=radioValueSexo,value=1).pack(side="top")

        tk.Label(self,text="Ingresa tu edad",font=('Helvetica', 15)).pack(side = "top")
        ttk.Combobox(self,values=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]).pack()


        tk.Label(self,text="Ingresa tu estado civil",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
        radioValueEstadoCivil = tk.IntVar() 
        tk.Radiobutton(self,text="Soltero",variable=radioValueEstadoCivil,value=0).pack(side="top")
        tk.Radiobutton(self,text="Casado",variable=radioValueEstadoCivil,value=1).pack(side="top")


        tk.Label(self,text="Ingresa tus ingresos mensuales con números",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10) 
        Salario= tk.StringVar()
        tk.Entry(self,textvariable = Salario).pack()
        hola = Salario.get()
        
        

        tk.Label(self,text="¿Fumas?",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
        radioValueTabaco = tk.IntVar() 
        tk.Radiobutton(self,text="No",variable=radioValueTabaco,value=0).pack(side="top")
        tk.Radiobutton(self,text="Sí",variable=radioValueTabaco,value=1).pack(side="top")

        tk.Label(self,text="Ingresa tus peso en kilogramos",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
        Peso= tk.IntVar()
        tk.Entry(self,textvariable = Peso).pack()

        tk.Label(self,text="Ingresa tus estatura en centimetros",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
        Altura= tk.IntVar()
        tk.Entry(self,textvariable = Altura).pack()

        tk.Label(self,text="Selecciona la opción que describe tu seguridad social",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
        radioValueSegSocial = tk.IntVar() 
        tk.Radiobutton(self,text="No tengo seguridad social de ningún tipo",variable=radioValueSegSocial,value=0).pack(side="top")
        tk.Radiobutton(self,text="Sí tengo seguridad social",variable=radioValueSegSocial,value=1).pack(side="top")


        tk.Label(self,text="Prueba",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
        prueba = tk.IntVar() 
        tk.Radiobutton(self,text="mas",variable=prueba,value=1).pack(side="top")
        tk.Radiobutton(self,text="nah",variable=prueba,value=2).pack(side="top")




        tk.Button(self, text="Enviar",
                  command=lambda: master.switch_frame(PageTwo)).pack(side="bottom", pady=10,padx=10)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        if prueba == 1:
            app.destroy()
            #labelValue = tk.Label(app, textvariable=B)
            #labelValue.grid(column=2,row=2,)
            #tk.Label(self,text="Ingresa el costo de tu renta mensual",font=('Helvetica', 15)).pack(side = "top", pady=10,padx=10)
            #PrecioRenta= tk.IntVar()
            #tk.Entry(self,textvariable = PrecioRenta).pack()
            return




        #tk.Label(self, text="Resultados", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        tk.Button(self, text="Siguiente",
                  command=lambda: master.switch_frame(PageThree)).pack()


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Resultados", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)



        def salariofunt():
            
            Con1 = tk.Label(self, text=B, font=('Helvetica', 15, "bold"),wraplength = 500)
            if int(hola) < 10:
                Con1.pack(side = "top", pady=10,padx=10)
            else: return                

       
     
        salariofunt()       

        tk.Button(self, text="Cerrar",
                  command=lambda: master.close(PageThree)).pack()

        #salariofunt(Salario)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Sistema experto financiero")
    app.resizable(0,0)
    app.iconbitmap("icon.ico")
    app.mainloop()







