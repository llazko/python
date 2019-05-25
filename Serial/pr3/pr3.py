# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:14:57 2019

@author: lazko
"""


#Muestra los Puertos COM en Python
import serial.tools.list_ports
# Llamamos a la libreria que nos ayudara a buscar
# los puertos habilidatos.


find_com = serial.tools.list_ports

COM = find_com.comports()

#Nos devuelve una lista
# EL primer parametro es el puerto.
print(COM[0]) # Nombre completo del puerto.
print(COM[0][0]) # Solo puerto COM#