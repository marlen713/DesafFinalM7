#LO USE PARA TRABAJAR CON LA SHELL Y GENERAR LOS LISTADOS PEDIDOS EN EL HITO 2
from django.db import connection
import os

consulta_sql = """
    SELECT c.nombre AS comuna, i.nombre AS nombre_inmueble, i.descripcion
    FROM app_inmueble i
    JOIN app_comuna c ON i.comuna_id = c.id
    WHERE i.disponible = TRUE
"""

with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

resultados_file = 'listado_inmuebles_comuna.txt'
with open(resultados_file, "w") as file:
    for row in resultados:
        comuna, nombre_inmueble, descripcion = row
        file.write(f"Comuna: {comuna}\n")
        file.write(f"Nombre del inmueble: {nombre_inmueble}\n")
        file.write(f"Descripcion: {descripcion}\n")
        file.write("\n")


#listado de inmuebles Regiones
from django.db import connection
import os

consulta_sql = """
    SELECT r.nombre AS region, i.nombre AS inmueble_nombre, i.descripcion AS inmueble_descripcion
    FROM app_inmueble AS i
    INNER JOIN app_comuna AS c ON i.comuna_id = c.id
    INNER JOIN app_region AS r ON c.region_id = r.id
    WHERE i.disponible = TRUE
    ORDER BY r.nombre
"""

with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

resultados_file = 'listado_inmuebles_regiones.txt'
with open(resultados_file, "w") as file:
    region_actual = None
    for region, inmueble_nombre, inmueble_descripcion in resultados:
        if region != region_actual:
            if region_actual:
                file.write("\n")
            file.write(f"Region: {region}\n")
            region_actual = region
        file.write(f"Inmueble: {inmueble_nombre}\n")
        file.write(f"Descripcion: {inmueble_descripcion}\n")

print("Listado de inmuebles por regiones guardado en el archivo:", resultados_file)
