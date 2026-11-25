# Importamos los módulos necesarios.
import mysql.connector
import csv

# Conectamos con la base de datos StarWars.
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="starwars"
)

print("Conexión realizada correctamente")

# Creamos el cursor para ejecutar la consulta.
cursor = conexion.cursor()

# Obtenemos los datos de los episodios y sus personajes.
cursor.execute("""
    SELECT Episodio.idEpisodio,
           Episodio.titulo,
           Episodio.anioEstreno,
           Episodio.director,
           Episodio.duracionMinutos,
           Personaje.nombre,
           Personaje.especie,
           Personaje.planetaOrigen,
           Personaje.afiliacion,
           Personaje.usaFuerza
    FROM Episodio
    INNER JOIN Personaje
    ON Episodio.idEpisodio = Personaje.idEpisodio
""")

# Guardamos el resultado en una lista de tuplas.
datos = cursor.fetchall()

# Cerramos el cursor y la conexión.
cursor.close()
conexion.close()

# Mostramos los datos para comprobar la carga.
print("\nDATOS DE EPISODIOS Y PERSONAJES")
print("Número de filas cargadas:", len(datos))

for fila in datos:
    print(fila)

# Creamos un diccionario vacío para los directores.
directores = {}

# Abrimos el archivo para leerlo.
with open("Directores.txt", "r", encoding="utf-8-sig") as archivo:

    # Los campos del archivo están separados por punto y coma.
    lector = csv.reader(archivo, delimiter=";")

    # Saltamos la cabecera.
    next(lector)

    # Recorremos las filas del archivo.
    for fila in lector:
        nombre = fila[0]

        # Guardamos los datos del director en otro diccionario.
        directores[nombre] = {
            "anioNacimiento": int(fila[1]),
            "pais": fila[2],
            "otraPelicula": fila[3],
            "episodios": 0
        }

# Mostramos los directores para comprobar la carga.
print("DIRECTORES CARGADOS")

for nombre in directores:
    print("Nombre:", nombre)
    print("Año de nacimiento:", directores[nombre]["anioNacimiento"])
    print("País:", directores[nombre]["pais"])
    print("Otra película:", directores[nombre]["otraPelicula"])
    print("Episodios:", directores[nombre]["episodios"])
    print("--------------------")

print("Número de directores:", len(directores))

# Empezamos con una opción vacía para entrar en el bucle.
opcion = ""

# Repetimos el menú hasta que se elija salir.
while opcion != "0":
    print("\nARCHIVO GALÁCTICO")
    print("1. Mostrar los episodios.")
    print("2. Mostrar los personajes de un episodio.")
    print("3. Buscar personajes por su nombre.")
    print("4. Mostrar las especies sin duplicados.")
    print("5. Mostrar las afiliaciones sin duplicados.")
    print("6. Mostrar los planetas de origen sin duplicados.")
    print("7. Mostrar los personajes de una especie.")
    print("8. Contar los personajes que usan la Fuerza y los que no.")
    print("9. Mostrar la información de los directores.")
    print("10. Calcular y mostrar el número de episodios de cada director.")
    print("11. Mostrar los directores que más episodios han dirigido.")
    print("12. Mostrar los episodios y la información de un director.")
    print("0. Salir.")

    opcion = input("Selecciona una opción: ")

