#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 10 ene. 2020

@author: Angel
'''


'''
                        Módulos

En Python cada archivo es un módulo, cuyo nombre es el del propio archivo.

Para importar un módulo dentro de otro podemos hacerlo:
    Totalmente con: import modulo_a_importar
    Parcialmente con: from modulo_a_importar import funcion_a_importar
    
No es necesario indicar la ruta de acceso al módulo porque Python dispone de una cadena de búsqueda de módulos (ni tampoco la extensión .py):
    Primero busca en la propia carpeta
    Luego en las ubicaciones indicadas en la variable de entorno PYTHONPATH
    Por último en el directorio donde se encuentran las bibliotecas estándar
                        
                        
                        
'''


'''
                        Paquetes

Un paquete es un directorio en el que se guardan varios módulos (archivos .py) 
y en el que incorporamos además un archivo llamado __init__.py (que puede estar simplemente vacío)

Estos directorios suelen tener la inicial en mayúscula para distinguirlos de los módulos estándar (que están todos en minúsculas)

Por ejemplo, podríamos agrupar en un paquete llamado “Matrix” varios módulos diseñados para realizar operaciones matriciales: 
                Producto, Inversa, Determinante, …
                
Para importar uno de estos módulos usaríamos indistintamente:
    import Matrix.Determinante
    from Matrix import Determinante
    
Podríamos importarlos todos con from Matrix import * si en el archivo __init__.py insertamos la siguiente instrucción:
__all__=[“Producto”,”Inversa”,”Determinante”]


'''


from connMySQL import *

sSelect="SELECT * FROM MEDICAMENTOS";
cursor1 = SelectSQL(sSelect)
#cursor1 = connPsotgreeSQL.EjecutarSQL(sSelect)

for fila in cursor1:
    print(fila) 
cursor1.close()


sSelect=("SELECT * FROM MEDICAMENTOS WHERE nombre_medicamento = 'Paracetamol'")
cursor1 = SelectSQL(sSelect)
for fila in cursor1:
    print(fila) 
cursor1.close()


sSQL=("INSERT INTO medicamentos(nombre_medicamento, fcaducidad_medicamento, indicaciones_medicamento) VALUES ('Metamizol', '2023-01-15', 'Ingerir')")
cursor1 = EjecutarSQL(sSQL)
cursor1.close()


sSQL=("UPDATE medicamentos SET nombre_medicamento='Digoxina', fcaducidad_medicamento='2030-01-02' WHERE id_medicamento=13")
cursor1 = EjecutarSQL(sSQL)
cursor1.close()

sSQL=("DELETE FROM medicamentos WHERE id_medicamento=14")
cursor1 = EjecutarSQL(sSQL)
cursor1.close()

