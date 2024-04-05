while True:
    print("Bienvenido al centro de garantías de ELECTROTECH")
    print("")
    print("Por favor, escoja una opción según su producto:  ")
    print("1. Garantía para un electrodoméstico grande (ej: nevera-lavadora)")
    print("2. Garantía para un dispositivo electrónico (ej: teléfono o computador)")
    print("3. Garantía para un accesorio electrónico (ej: cargador-cable USB)")
    print("4. Otro caso")

    opcion = input("Por favor ingrese el número correspondiente a su opción: ")

    if opcion == "1":
        print("")
        print("Ha seleccionado la opción de garantía para un electrodoméstico grande.")
        meses = int(input("Por favor, ingrese hace cuántos meses realizó la compra: "))
        if meses < 12:
            print("")
            print("La empresa le dará un reemplazo a su producto y un reembolso del 5% de su compra.")
        else:
            print("Disculpe, nuestra empresa no ofrece reemplazo ni reembolso para productos con más de 12 meses de compra.")

    elif opcion == "2":
        print("")
        print("Ha seleccionado la opción de garantía para un dispositivo electrónico.")
        meses = int(input("Por favor, ingrese hace cuántos meses realizó la compra: "))
        if meses < 6:
            print("")
            print("La empresa le dará una reparación gratuita a su producto y un reembolso del 3% de su compra.")
        else:
            print("La empresa no ofrece reparación gratuita ni reembolso para productos con más de 6 meses de compra.")

    elif opcion == "3":
        print("")
        print("Ha seleccionado la opción de garantía para un accesorio electrónico.")
        meses = int(input("Por favor, ingrese hace cuántos meses realizó la compra: "))
        if meses < 3:
            print("")
            print("La empresa le dará un reemplazo directo a su producto y un reembolso del 2% de su compra.")
        else:
            print("La empresa no ofrece reemplazo ni reembolso para accesorios con más de 3 meses de compra.")

    elif opcion == "4":
        print("")
        print("Ha seleccionado otro caso.")

    print("")
    continuar = input("¿Desea realizar otro proceso? (Sí/No): ")
    if continuar.lower() != "si":
        break
    print("")
    print("")