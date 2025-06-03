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
    def __init__(self, id_votante, genero, edad, circunscripcion, nivel_socioeconomico, nivel_educativo, afiliacion_politica, interes_politica) :
        #Genérico
        self.id_votante = id_votante
        self.genero = genero
        self.edad = edad
        
        #Situación individual
        self.circunscripcion
        self.nivel_socioeconomico
        self.nivel_educativo
        
        #Partidarios
        self.afiliacion_politica
        self.interes_politica
        
        #Opinión y Preocupación
        self.preocupacion_economica
        self.preocupacion_seguridad
        
        self.opinion_gobierno_actual
        self.percepcion_corrupcion
        
        #Sobre el Voto
        self.intencion_voto
        self.dispocision_cambiar_voto
        self.participacion_voto_anterior

class Partido :
    ...

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
