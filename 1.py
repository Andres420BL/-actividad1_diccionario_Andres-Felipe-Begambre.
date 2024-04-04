#elaborar un programa en python qye capture la siguiente informaion codigo,nombre,apellidos,contacto,correo,edad.
#SOLO SE REGISTRA LOS ESTUDIANTES QUE CUMPLAN LOS SIGUIENTES CRITERIOS 
#SEXO MACULINO.EDAD:15-25,estrato socio economico 1 y 2
#sexo femenino 20-35 estrato 1 y 4 en caso que no aplique guardar su contacto en una lista guardar el contacto en una lista llamada pendiente
import os
diccionario = {}
ls_lista=[]
def fnt_pantalla():
    os.system('cls')
def fnt_agregar(Nombrestr,Apelliodstr,contactoint,correo,edadint):
    if  Nombrestr == '' or Apelliodstr == '' or contactoint == '' or correo == '' or edadint == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[Nombrestr] = {'nombre': Nombrestr, 'Apellidos': Apelliodstr, 'Contacto': contactoint,'correo': correo,'edadint': edadint}
        enter = input(f'\nLa persona {Nombrestr} ha sido registrada con éxito <ENTER>')
     
def fnt_sexom():
    estrato=input('Ingrese el estrato socioeconomico')
    if estrato == '1' or '2':
        fnt_agregar()
        
    

sw = True

def fnt_mmm():
    if opcion == '1':
        Nombrestr = input('Ingrese sus Nombres:')
        Apellidostr =input('Ingrese sus Apellidos:')
        Contactoint=int(input('Ingrese el numero de Contacto'))
        correo=input('Ingrese su correo Electronico')
        edadint=int(input('Ingrese su edad'))
        
    
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_mmm()
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(diccionario),'\n')
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False

            
       

        
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
       
            
    