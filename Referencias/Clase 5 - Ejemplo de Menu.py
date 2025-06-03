# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:01:24 2025

@author: Sophie
"""
# EJERCICIOS DE COMPLEJIZACIÓN
### EJERCICIO 1

#MODULARIZACIÓN Y FUNCIONES
#registrarse
def signup(usuarios) :
    usuario = input('Nuevo usuario: ')
    contrasenia = input('Contraseña: ')
    
    if usuario in usuarios.keys() :
        print('Este usuario ya existe')
        return usuarios
    
    else :
        usuarios[usuario] = contrasenia #guarda la contraseña
        print('Registro realizado')
        return usuarios #devuelve el dicc de usuarios con el nuevo usuario guardado
    

#iniciar sesión
def login(usuarios) : #usuarios es el dicc con todos los usuarios
    usuario = input('Ingrese nombre de usuario: ')
    contrasenia = input('Ingrese contraseña: ')
    
    if usuario in usuarios.keys() :
        if usuarios[usuario] == contrasenia : #contraseña correcta
            print('Registro válido')
            return usuario
    
    print('Hay un ingreso incorrecto')
    return None


#cerrar sesión
def logout() :
    print('Ha cerrado sesión correctamente')
    return None


#menu principal
def menu_default() :
    pass #no la hicimos todavía

#menu logueado
def main_menu() :
    pass #no la hicimos todavía

#salgo del sistema
def salida() :
    pass #no la hicimos todavía

#cambiar contraseña
def cambiar_pass(usuarios, usuario) :
    contrasenia = input('Contraseña actual: ')  
    
    if usuarios[usuario] == contrasenia :
        contrasenia = input('Ingrese su contraseña nueva')
        usuarios[usuario] == contrasenia
        print('Contraseña actualizada')
        
    else :
        print('Contraseña incorrecta')
    
    return usuarios

#LOGICA DEL MENÚ
'''
opcion = '0' 

while opcion != '3' : 
    if opcion == '1' :
        print('Eligió 1')
    
    elif opcion == '2' :
        print('Eligió 3')
        
    opcion = input('Menu \n 1. Opcion 1\n 1. Opcion 2\n 3. Salir \n') 
'''    
usuario = None
usuarios = {'admin': '1234'}

while True :
    if usuario == None : #cuando el usu no está logueado
        opcion = input('Menu \n 1. Login \n 2. Signup \n 3. Salir \n') 
        
        if opcion == '1' :
            print('Login')
            usuario = login(usuarios)
        
        elif opcion == '2' :
            print('Signup')
            usuarios = signup(usuarios)
        elif opcion == '3' :
            print('Saliste del programa')
            break
        
        else :
            print('Ingreso inválido\n')
    
    else : #cuando el usu está logueado
        opcion = input('Menu \n 1. Cambiar contraseña\n 2. Logout\n 3. Salir \n') 
        
        if opcion == '1' :
            print('Cambiar contraseña')
            usuario = cambiar_pass(usuarios, usuario)
            
        elif opcion == '2' :
            print('Logout')
            usuario = logout(usuario)
            
        elif opcion == '3' :
            print('Saliste del programa')
            break
        
        else :
            print('Ingreso inválido\n')


