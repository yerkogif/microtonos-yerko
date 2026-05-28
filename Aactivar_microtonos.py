import winsound #libreria que permite activar sonidos
import time
print("Simulador de microtonos")
maximo_microtonos = 25
microtonos_libre = 25
microtonos_activos = 0
ejecutando = True
while ejecutando :
    print("\n=== panel de microtonos")
    print("1.- ver cuantos microtonos quedan libres")
    print("2.- acticar microtonos (activacion de sonido)")
    print("3.- recuperar microfonos")
    print("4.- monitorier el sonido actual")
    print("5.- salir")
    opcion = int(input("elije una opcion del (1-5):"))
    if opcion == 1:
        print(f"\n[INFO] tienes {microtonos_libre} microtonos disponibles para usar")
    elif opcion == 2:
        print(f"\n ACTIVAR MICROTONOS (disponibles: {microtonos_libre})")
        if microtonos_libre == 0:
            print("ya no se pueden emitir mas microfonos, sonido al limite")
        else:
            try:
                cantidad = int(input("cuantos microtonos quieres activar:"))
                if cantidad <= 0:
                    print("tienes que activar al menos 1 microtono")
                elif cantidad > microtonos_libre:
                    print(f"solo puedes activar hasta {microtonos_libre} microtonos")
                else:
                    microtonos_libre -= cantidad
                    microtonos_activos += cantidad
                    print("reproduciendo microtono") 
                    frecuencias = [440,440,440,587,880,784,740,659]
                    duraciones = [300,300,300,700,700,700,200,200,200]
                    for i in range (1,cantidad +1):
                        nota_actual =frecuencias[(i -1) % len(frecuencias)]
                        duracion_actual = duraciones [(i -1) % len(duraciones)]
                        winsound.Beep(nota_actual, duracion_actual)
                        time.sleep(0.05)

            except ValueError:
                print("error")
    elif opcion == 3:
        try:
            print(f"\n recuperar microtonos, actualmente hay {microtonos_activos} microtonos activos")
            cantidad = int(input("cuantos microtonos quieres recuperar:"))
            if cantidad <= 0:
                print("error, la cantidad de microtonos a rcuperar debe ser mayor a 0")
            elif microtonos_libre + cantidad > maximo_microtonos:
                print(f"error, no puedes apagar tantos microtonos porque el maximo es {maximo_microtonos}")
            else:
                microtonos_libre += cantidad
                microtonos_activos -= cantidad
                print(f"recuperaste {cantidad} de microtonos para ser usados en otro momento")
                winsound.Beep(440,150)
        except ValueError:
            print("error, debes colocar un numero entero")
    elif opcion == 4:
        print(f"hay {microtonos_activos} microtonos activos haciendo vibrar el ambiente")
    elif opcion == 5:
        print("saliendo del sistema")
        ejecutando = False
    else: 
        print("error")