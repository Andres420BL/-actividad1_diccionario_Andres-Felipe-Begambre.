diccionarioRegistros = {}
pendiente = []
import os

def fnt_limpiar():
    os.system('cls')
    print('Registro estudiantil:\n\nBy:Andres Felipe')


def fnt_registro(diccionario,codigo,sexo,nombres,apellidos,contacto,correo,edad,estrato,direccion):

    edad = int(edad)
    estrato = int(estrato)  
    
    if (sexo == 'M' and (edad >= 15 and edad <= 25) and (estrato >= 1 and estrato <= 2)):
        print(f'Estudiante {nombres} {apellidos} código({codigo}) registrado con éxito')
        diccionario[codigo]= {'sexo': sexo, 'nombres': nombres,'apellidos': apellidos,'contacto': contacto, 'edad':edad,'estrato':estrato,'dirección': direccion}
    elif (sexo == 'F' and (edad >= 20 and edad <= 35) and (estrato >= 1 and estrato <= 4)):
        print(f'Estudiante {nombres} {apellidos} código({codigo}) registrado con éxito')
        diccionario[codigo]= {'sexo': sexo, 'nombres': nombres,'apellidos': apellidos,'contacto': contacto, 'edad':edad,'estrato':estrato,'dirección': direccion}
    else:
        print(f'El estudiante {nombres} {apellidos} código({codigo}) no cumple con los requisitos\nEstado: pendiente')
        pendiente.append(contacto)
    enter = input('Enter para continuar...')      
def fnt_selector(op):
    global sw
    global diccionarioRegistros
    
    if op == '0':
        sw = False
    elif op == '1':
        codigo = input('Código: ')
        sexo = input('Sexo [M]masculino [F]femenino: ').upper()[0]
        nombres = input('Nombres: ')
        apellidos = input('Apellidos: ')
        contacto = input('Contacto: ')
        correo = input('Correo: ')
        edad = input('Edad: ')
        estrato = input('Estrato: ')
        direccion = input('Dirección: ')
        fnt_registro(diccionarioRegistros,codigo,sexo,nombres,apellidos,contacto,correo,edad,estrato,direccion)
    elif op == '2':
        os.system('cls')
        while True:
            os.system('cls')
            opcion = input('<< CONSULTAR REGISTRADOS >>\n\n[1]Lista de registrados\n[2]Contactos pendientes\n[0]Salir\n-> ')
            
            if opcion == '0':
                break
            elif opcion == '1':
                print('\nCantidad de registros: ',len(diccionarioRegistros),'\n')
                print('Lista de registrados: ')
                for key, value in diccionarioRegistros.items():
                    print(f"{key}: {value}")
                enter = input('\n\nPresione ENTER para continuar...')
            elif opcion == '2':
                print('\nCantidad de pendientes: ',len(pendiente),'\n')
                print('Contacto de los estudiantes pendientes: ')
                print(pendiente)

                enter = input('\n\nPresione ENTER para continuar...')             
sw = True
while sw == True:
    fnt_limpiar()
    opcion = input('<< MENÚ DE REGISTROS >>\n\n[0]Salir\n[1]Registrar estudiante\n[2]Consultar\n--->')
    fnt_selector(opcion)