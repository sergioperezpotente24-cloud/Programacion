
talleres = [
    (
        "Fotografía",
        ["Ana", "Luis"],
        {"aula": 12, "plazas": 4},
        {"cámara", "tarjeta de memoria"}
    ),
    (
        "Robótica",
        ["Marta"],
        {"aula": 15, "plazas": 3},
        {"portátil", "cable USB"}
    ),
    (
        "Pintura",
        [],
        {"aula": 8, "plazas": 5},
        {"pinceles", "acuarelas", "papel"}
    )
]


def buscar_taller(nombre):
    for taller in talleres:
        if taller[0].lower() == nombre.lower():
            return taller
    return None


while True:
    print("\n--- GESTIÓN DE TALLERES ---")
    print("1. Mostrar talleres")
    print("2. Inscribir a un alumno")
    print("3. Cancelar una inscripción")
    print("4. Cambiar el aula")
    print("5. Añadir un material")
    print("6. Terminar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for taller in talleres:
            nombre = taller[0]
            alumnos = taller[1]
            informacion = taller[2]
            materiales = taller[3]

            libres = informacion["plazas"] - len(alumnos)

            print("\nTaller:", nombre)
            print("Aula:", informacion["aula"])
            print("Alumnos inscritos:", alumnos)
            print("Plazas libres:", libres)
            print("Materiales:", sorted(materiales))

    elif opcion == "2":
        nombre_taller = input("Nombre del taller: ")
        taller = buscar_taller(nombre_taller)

        if taller is None:
            print("El taller no existe.")
        else:
            nombre_alumno = input("Nombre del alumno: ")

            if nombre_alumno in taller[1]:
                print("El alumno ya está inscrito.")
            elif len(taller[1]) < taller[2]["plazas"]:
                taller[1].append(nombre_alumno)
                print("Alumno inscrito correctamente.")
            else:
                print("No quedan plazas libres.")

    elif opcion == "3":
        nombre_taller = input("Nombre del taller: ")
        taller = buscar_taller(nombre_taller)

        if taller is None:
            print("El taller no existe.")
        else:
            nombre_alumno = input("Nombre del alumno: ")

            if nombre_alumno in taller[1]:
                taller[1].remove(nombre_alumno)
                print("Inscripción cancelada.")
            else:
                print("El alumno no está inscrito.")

    elif opcion == "4":
        nombre_taller = input("Nombre del taller: ")
        taller = buscar_taller(nombre_taller)

        if taller is None:
            print("El taller no existe.")
        else:
            try:
                nueva_aula = int(input("Nuevo número de aula: "))

                if nueva_aula > 0:
                    taller[2]["aula"] = nueva_aula
                    print("Aula cambiada correctamente.")
                else:
                    print("El aula debe ser un número positivo.")

            except ValueError:
                print("Introduce un número entero válido.")

    elif opcion == "5":
        nombre_taller = input("Nombre del taller: ")
        taller = buscar_taller(nombre_taller)

        if taller is None:
            print("El taller no existe.")
        else:
            material = input("Nombre del material: ").strip()

            if material == "":
                print("El material no puede estar vacío.")
            elif material in taller[3]:
                print("Ese material ya existe.")
            else:
                taller[3].add(material)
                print("Material añadido correctamente.")

    elif opcion == "6":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida. Elige del 1 al 6.")
