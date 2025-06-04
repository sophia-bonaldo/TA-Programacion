# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 14:20:43 2025

@author: Sophie
"""
import pandas as pd
import matplotlib.pyplot as plt

#cargar BD
df = pd.read_csv('Decision_Voto_Elecciones.csv')

#______________________________________________________________________________

### MENÚ 1

# i. MODELADO DE DATOS

## Clases y Objetos
class Votante :
    def __init__(self, id_votante, genero, edad, circunscripcion, nivel_socioeconomico, nivel_educativo, afiliacion_politica, interes_politica, preocupacion_economica, preocupacion_seguridad, opinion_gobierno_actual, percepcion_corrupcion, intencion_voto, dispocision_cambiar_voto, participacion_voto_anterior) :
        #Genérico
        self.id_votante = id_votante
        self.genero = genero
        self.edad = edad
        
        #Situación individual
        self.circunscripcion = circunscripcion
        self.nivel_socioeconomico = nivel_socioeconomico
        self.nivel_educativo = nivel_educativo
        
        #Partidarios
        self.afiliacion_politica = afiliacion_politica
        self.interes_politica = interes_politica
        
        #Opinión y Preocupación
        self.preocupacion_economica = preocupacion_economica 
        self.preocupacion_seguridad = preocupacion_seguridad
        
        self.opinion_gobierno_actual = opinion_gobierno_actual
        self.percepcion_corrupcion = percepcion_corrupcion
        
        #Sobre el Voto
        self.intencion_voto = intencion_voto
        self.dispocision_cambiar_voto = dispocision_cambiar_voto
        self.participacion_voto_anterior = participacion_voto_anterior
        
        
        #MÉTODOS
        ...
        
        
class Partido :
    def __init__(self, afiliacion_politica) :
        self.afiliacion_politica = afiliacion_politica #preguntar si este es un atributo de Partido

    #MÉTODOS
votantes = {}
for i, fila in df.iterrows():
    id_votantes = fila ['ID_VOTANTES']
    datos_votantes = [fila['Genero'], fila['Edad'], fila ['Circunscripcion'], fila['Nivel_Socioeconomico'], fila['Nivel_Educativo'], fila['Afiliacion_Politica'], fila['Intencion_Voto'], fila['Disposicion_Cambiar_Voto']]
    votantes[id_votantes] = datos_votantes

### MENÚ 2

## 1. Agregar Registros

## 2. Modificar Registros

## 3. Promedio Votos

## 4. Máximo de Votos (ganador elecciones)

## 5. Volver al Menú anterior

## FUNCIONES

def carga_datos(archivo) :
    ...

def actualizar_datos(archivo, ) :
    ...

#______________________________________________________________________________

# ii. ANALIZAR DATOS - VISUALIZACIÓN

### MENÚ 3

## 1. Gráfico de Barras

## 2. Gráfico de Torta

## 3. Mostrar resultados df por consola

#______________________________________________________________________________

##LAMADOS DE DATOS PARA VERIFICAR COSAS
centro = df[df['Afiliacion_Politica'] == 'Centro'] # --> Partido A / Indeciso
izquierda = df[df['Afiliacion_Politica'] == 'Izquierda'] # --> Partido C / Indeciso
derecha = df[df['Afiliacion_Politica'] == 'Derecha'] # --> Partido B / Indeciso
