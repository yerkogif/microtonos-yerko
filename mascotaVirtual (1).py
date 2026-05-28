nombre = "Waffle"
energia = 100
felicidad = 100
print(f"Energía inicial de: {nombre}, energía: {energia}, felicidad: {felicidad}")
while energia > 0:
    print("¿Qué quieres hacer:?")
    print("1.- Comer")
    print("2.- Jugar")
    print("3.- Ver estado de salud")
    print("4.- No hacer nada")
    print("5.- Dormir (¡Tu actualización!)")
    opcion = input("Seleccione: ")
    if opcion == "1":
        energia = energia + 20
        energia = energia + 20
        felicidad = felicidad + 1
        print(f"Alimentaste a {nombre}, está muy feliz contigo..")
    elif opcion == "2":
        energia = energia - 15
        felicidad = felicidad + 20
        print(f"{nombre} esta cansado pero feliz de jugar contigo")
    elif opcion == "3":
        print("     /\__                     ")
        print("    (    @\___                ")
        print("    /         O               ")
        print("   /     (____/               ")
        print("   /_____/                    ")
        print(f"Energia: {energia}")
        print(f"Felicidad: {felicidad}")
    elif opcion == "4":
        felicidad = felicidad - 10
        energia = energia - 5
        print(f"{nombre} está muy aburrido....")
    elif opcion == "5":
        energia = 100
        print(f"{nombre} durmió una siesta. ¡Su energía volvió al 100%!")
    else:
        print("error de ingreso")