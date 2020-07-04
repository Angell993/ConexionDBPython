#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Created on 10 ene. 2020

@author: Angel
'''

'''
Previo instalar PyMySQL
Desde cmd con derechos de administrador:

pip install PyMySQL

'''

import pymysql

def LeerParametrosConexion():
    ruta = "confBBDD.ini"
    dCadenaConexion={}
    with open(ruta, mode='r', encoding="utf-8") as fichero:
        for sLinea in fichero:
            if "host=" in sLinea:
                 dCadenaConexion['host'] = sLinea[5:len(sLinea)-1]
            elif "database=" in sLinea:
                 dCadenaConexion['database'] = sLinea[9:len(sLinea)-1]
            elif "user=" in sLinea:
                dCadenaConexion['user'] = sLinea[5:len(sLinea)-1]
            elif "password=" in sLinea:
                dCadenaConexion['password'] = sLinea[9:len(sLinea)-1]
    
    return dCadenaConexion


def EjecutarSQL(sSQL):
    
    try:
        '''
        dConexion = LeerParametrosConexion() 
        conexion = pymysql.connect(dConexion.get('host'),  
                                    user=dConexion.get('user'), 
                                    password=dConexion.get('password'),
                                    dConexion.get('database'))
        '''
        conexion = pymysql.connect("localhost","root","root","farmacia")
        
        print('Conectando a la base de datos PostgreSQL...')
  
        cur = conexion.cursor()
        cur.execute(sSQL)
        conexion.commit()
        print("La instrucción SQL se ha realizado con éxito.")
        return cur
    

    except (Exception, pymysql.DatabaseError) as error:
        print(error)
 
    
def SelectSQL(sSQL):
    
    try:        
        conexion = pymysql.connect("localhost","root","root","farmacia")
        
        print('Conectando a la base de datos PostgreSQL...')
  
        cur = conexion.cursor()
        cur.execute(sSQL)
        return cur
    

    except (Exception, pymysql.DatabaseError) as error:
        print(error)