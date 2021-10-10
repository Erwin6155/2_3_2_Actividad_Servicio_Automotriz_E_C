Rut=input('Ingrese rut:')
nombre_completo=input('ingrese nombre ompleto:')
marca=input('ingrese marca del aiutomovil:')
modelo=input('ingrese modelo:')

print('los servicios posibles para controlar son los siguientes: ')
print('--------------------------------------------------------')
print('Servicio \t\t\t Tiempo de espera')
print('--------------------------------------------------')
print('|1.-R1evision de 1.000kn \t\t\t 2 horas')
print('|2.-Cambio de aceite \t\t\t 1 hora')
print('|3.-Revison de freno: \t\t\t 0,5 horas ')
print('|4.-Revision de Correas \t\t\t 0,2 horas')
print('|5.-Revision de luces \t\t\t 0,2 horas')
print('|6.-Revision de direccion \t\t\t 0,5 horas')
print('|7.-Lavado de lapiz (sin costo) \t\t\ 0,5 horas ')
print('------------------------------------------')

opcion=0
arreglo=[]
while(opcion !=8):
    opcion=int(input('elija su opcion y presione enter(8 para salir):')
    arreglo.append(opcion)

tiempo=0.0
for op in arreglo:
    if opcion ==1:
        tiempo +=2.0
    elif opcion==2:
        tiempo+=1.0
    elif op ==3:
        tiempo+=5.0
    elif op ==4:
        tiempo+=0.5
    elif op ==5:
        tiempo+=0.2
    elif op ==6:
        tiempo+=0.5
    elif op ==7:
        tiempo+=0.5
print(f'el tiempo total es {tiempo} horas')

print ('tiempo total es  ')
