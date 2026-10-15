print("Lista almacen")

almacen = []

while True:

    print("1. Añadir un nuevo producto")
    print("2. Listar todos los productos")
    print("3. Mostrar valor del almacén")
    print("4. Salir del programa")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":

        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad de stock: "))
        precio = float(input("Precio por unidad: "))

        producto = [nombre, cantidad, precio]
        almacen.append(producto)

        print("Producto añadido correctamente.")

    elif opcion == "2":

        for producto in almacen:
            print("Nombre:", producto[0])
            print("Cantidad:", producto[1])
            print("Precio:", producto[2])

    elif opcion == "3":
        total = 0

        for producto in almacen:
            total = total + producto[1] * producto[2]

        print("Valor total del almacén:", total)

    elif opcion == "4":
        print("Programa finalizado.")
        break