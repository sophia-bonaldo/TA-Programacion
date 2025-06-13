# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 15:46:29 2025

@author: msosa
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#configurar el working directory en la ruta del archivo
ruta = r"C:\Users\msosa\Documents\ayme\programacion"
os.chdir(ruta)

#verificación de current working directory

#Luego, para trabajar con el archivo se utiliza solamente el nombre
archivo = "Decision_Voto_Elecciones.csv"

#cargar BD
df = pd.read_csv(archivo)

#______________________________________________________________________________

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
        self.afiliacion_politica = afiliacion_politica
        self.lista_votantes = [] # lista con los votantes afiliados a un partido
      
        #METODOS  
    def agregar_votantes(self, votante) :
        self.lista_votantes.append(votante)
        

    def clasificar_votantes(self, dicc_personas) :
        clase_baja = []
        clase_media = []
        clase_alta = []
    
        for votante_id in self.lista_votantes :
            votante = dicc_personas[votante_id]
            clase = votante.nivel_socioeconomico
            if clase == "Bajo" :
                clase_baja.append(votante_id)
            elif clase == "Medio" :
                clase_media.append(votante_id)
            elif clase == "Alto" :
                clase_alta.append(votante_id)
    
        return clase_baja, clase_media, clase_alta
    
    def total_votantes(self) :
        return len(self.lista_votantes)

## FUNCIONES

def cargar_datos(archivo,partido_A,partido_B,partido_C):
    '''
    Clasifica a los votantes en tres partidos políticos.Lee un archivo CSV y los clasifica en tres 
    partidos políticos sacando los datos de la columna 'Intencion_Voto'. Se agregan a los votantes a 
    sus respectivos partidos mediante los métodos de la clase 'Partido'. Devuelve un diccionario con los objetos y un dataframe
    con los datos de los votantes.


    Parameters
    ----------
    archivo : str
        El archivo que contiene las columnas de donde se sacan los datos.
    partido_A : objeto
        Objeto de la clase 'Partido', es el 'Partido A'.
    partido_B : objeto
        Objeto de la clase 'Partido', es el 'Partido B'.
    partido_C : objeto
        Objeto de la clase 'Partido', es el 'Partico C'.

    Returns
    -------
    dicc_personas : dict
        Devuelve un diccionario con los objetos, la clave es un identificador unico (numero del 1 al ultimo)
        y el valor es el objeto 'Votante'.
    df : dataframe
        Devuelve el df con los datos de los votantes.
    '''
    df = pd.read_csv(archivo)
    
    dicc_personas = {}
    columnas = list(df.columns)
    
    identificador = 1
    for i, fila in df.iterrows():
        valores = []
        for col in columnas :
            valor = fila[col]  # obtenemos el valor que corresponde a la columna actual
            valores.append(valor)  # lo agregamos a la lista de valores
        
        nombre = identificador
        persona = Votante(* valores)
        
        dicc_personas[nombre] = persona
        identificador += 1
        
        if persona.intencion_voto == "Partido A":
            partido_A.agregar_votantes(nombre)
        elif persona.intencion_voto == "Partido B":
            partido_B.agregar_votantes(nombre)
        
        elif persona.intencion_voto == "Partido C":
            partido_C.agregar_votantes(nombre)
    
    return dicc_personas, df

def agregar_registro(participantes, partido_A, partido_B, partido_C):
    '''
    Crea una nueve instancia de la clase Votantes, los atributos de la instancia son dados por 
    el usuario (se chequean que estan acorde a los requeridos). Luego esta instancia es
    asignada a la instancia de Partido que pertenece(partido A, partido B o Partido C) en el 
    atributo votantes de la clase Partido.

    Parameters
    ----------
    participantes : diccionario
        el diccionaro contiene las instancias de obajetos de Votantes como valoer y la clave es el id 
    partido_A : objeto
        Objeto de la clase 'Partido', es el 'Partido A'.
    partido_B : objeto
        Objeto de la clase 'Partido', es el 'Partido B'.
    partido_C : objeto
        Objeto de la clase 'Partido', es el 'Partico C'.

    Returns
    -------
     .
    '''
    
    ultimo_id = max(participantes.keys()) + 1 #### COMENTARIO: EXPLICAR QUÉ HACE
    
    genero = input("Ingrese el género (Femenino/Masculino/Otro): ").capitalize()
    while genero not in ["Masculino", "Femenino", "Otro"]:
        genero = input("Ingrese el género (Femenino/Masculino/Otro): ").capitalize()
    
    edad = input("Ingrese la edad: ")
    while not edad.isdigit() or int(edad) <= 0:
        edad = input("Ingrese una edad válida: ")
        
    print('Circunscripción electoral a la que pertenece el votante (Norte/Sur/Este/Oeste/Centro).')
    circuncripcion = input("Ingrese la circuncripcion: ").capitalize()
    
    while circuncripcion not in ["Norte", "Sur", "Este", "Oeste", "Centro"]:
        circuncripcion = input("Ingrese la circuncripcion: ").capitalize()
    
    nivel_socioeconomico = input("Ingrese el nivel socioeconomico (Bajo/Medio/Alto): ").capitalize()
    while nivel_socioeconomico not in ["Bajo", "Medio", "Alto"]:
        nivel_socioeconomico = input("Ingrese el nivel socioeconomico: ").capitalize()
        
    nivel_educativo = input("Ingrese el nivel educativo más alto alcanzado (Secundario/Universitario/Posgrado): ").capitalize()
    while nivel_educativo not in ["Secundario", "Universitario", "Posgrado"]: ##### PREGUNTAR SI PODRÍAMOS DEJAR QUE PONGA 'Primario' u 'Otro'
        nivel_educativo = input("Ingrese el nivel educativo más alto alcanzado: ").capitalize()
    
    afiliacion_politica = input("Ingrese la afilacion politica (Centro/Izquierda/Derecha): ").capitalize()
    while afiliacion_politica not in ["Centro", "Derecha", "Izquierda"]:
        afiliacion_politica = input("Ingrese la afilacion politica (Centro/Izquierda/Derecha): ").capitalize()
        
    interes_politica = input("Ingrse el interés político (rango 1-5): ")
    while not interes_politica.isnumeric() or int(interes_politica) not in [1, 2, 3, 4, 5] :
       interes_politica = input("Ingrse el interés político (rango 1-5): ")
   
    preocupacion_economia = input("Ingrese la preocupación económica (rango 1-5): ")
    while not preocupacion_economia.isnumeric() or int(preocupacion_economia) not in [1, 2, 3, 4, 5]:
       preocupacion_economia = input("Ingrese la preocupación económica (rango 1-5): ")
       
    preocupacion_seguridad = input("Ingrese la preocupación de seguridad (rango 1-5): ")
    while not preocupacion_seguridad.isnumeric() or int(preocupacion_seguridad) not in [1, 2, 3, 4, 5]:
       preocupacion_seguridad = input("Ingrese la preocupación de seguridad (rango 1-5): ")

    opinion_gobierno = input("Ingrese la opinión del gobierno actual (rango 1-5): ")
    while not opinion_gobierno.isnumeric() or int(opinion_gobierno) not in [1, 2, 3, 4, 5]:
       opinion_gobierno = input("Ingrese la opinión del gobierno actual (rango 1-5): ")
   
    percepcion_corrupcion = input("Ingrese la percepción de la corrupción (rango 1-5): ")
    while not percepcion_corrupcion.isnumeric() or int(percepcion_corrupcion) not in [1, 2, 3, 4, 5]:
       percepcion_corrupcion = input("Ingrese la percepcion de la corrupcion (rango 1-5): ")
    
    intencion_voto = input("Ingrese qué partido piensa votar (Partido A/Partido B/Partido C): ").title() ## ALT: INGRESA SÓLO A/B/C y después lo modificamos para que no tenga errores o hacer un manejo de error
    while intencion_voto not in ["Partido A", "Partido B", "Partido C", "Indeciso"]:
        intencion_voto = input("Ingrese qué partido piensa votar (Partido A/Partido B/Partido C): ").title()
    
    disposicion_cambiar = input("Ingrese si hay posibilidad de cambie su intención de voto (Sí/No): ").capitalize()
    while disposicion_cambiar not in ["Sí", "No"] :
        disposicion_cambiar = input("Ingrese si hay posibilidad de cambie su intención de voto (Sí/No): ").capitalize()
    
    participacion_previa_votacion = input("Ingrese si votó en las elecciones anteriores (Sí/No): ").capitalize()
    while participacion_previa_votacion not in ["Sí", "No"]:
        participacion_previa_votacion = input("Ingrese si votó en las elecciones anteriores (Sí/No): ").capitalize()
        

    valores = [ultimo_id, genero, edad, circuncripcion, nivel_socioeconomico, nivel_educativo, afiliacion_politica, interes_politica, preocupacion_economia, preocupacion_seguridad, opinion_gobierno, percepcion_corrupcion, intencion_voto, disposicion_cambiar, participacion_previa_votacion]
    persona = Votante(* valores)
    
    participantes[ultimo_id] = persona
    
    if persona.intencion_voto == "Partido A":
        partido_A.agregar_votantes(ultimo_id + 1)
    
    elif persona.intencion_voto == "Partido B":
        partido_B.agregar_votantes(ultimo_id)
    
    elif persona.intencion_voto == "Partido C":
        partido_C.agregar_votantes(ultimo_id)
     
    
def actualizar_datos(archivo, participantes):
    try:
        filas = []
        ids_vistos = set() # set() -> se fija si el id ya apareció antes y si no hay coincidencia lo guarda
        
        for votante in participantes.values():
            if votante.id_votante in ids_vistos :
                raise ValueError(f"ID duplicado encontrado: {votante.id_votante}")
            
            ids_vistos.add(votante.id_votante)
            
            fila = {
                'ID_Votante': votante.id_votante,
                'Genero': votante.genero,
                'Edad': votante.edad,
                
                'Circunscripcion': votante.circunscripcion,
                'Nivel_Socioeconomico': votante.nivel_socioeconomico,
                'Nivel_Educativo': votante.nivel_educativo,
                
                'Afiliacion_Politica': votante.afiliacion_politica,
                'Interes_Politica': votante.interes_politica,
                
                'Preocupacion_Economia': votante.preocupacion_economica,
                'Preocupacion_Seguridad': votante.preocupacion_seguridad,
                
                'Opinion_Gobierno_Actual': votante.opinion_gobierno_actual,
                'Percepcion_Corrupcion': votante.percepcion_corrupcion,
                
                'Intencion_Voto': votante.intencion_voto,
                'Disposicion_Cambiar_Voto': votante.dispocision_cambiar_voto,
                'Participacion_Voto_Anterior': votante.participacion_voto_anterior
            }
            
            filas.append(fila)
        
        df_actualizado = pd.DataFrame(filas)
        df_actualizado.to_csv(archivo, index = False) # el index = False, hace que solo muestre la información del DataFrame, sin el índice que esta función crea.
        print("Archivo CSV actualizado correctamente.")
   
    except ValueError as error:
        print(f"Error de validación de datos: {error}")
    
    except Exception as e:
        print(f"Error al actualizar el archivo: {e}")


def modificar_registro(df, participantes, archivo) :
    try:
        id_modificar = int(input("Ingrese el ID del votante que desea modificar: "))
    
    except ValueError:
        print("Debe ingresar un número válido.")
        return participantes

    if id_modificar not in df['ID_Votante'].values:
        print("Ese ID no se encuentra en el archivo.")
        return participantes

    indice_fila = df[df['ID_Votante'] == id_modificar].index[0]
    
    print("\nDatos actuales del votante: ")
    print(df.loc[indice_fila])

    columnas = list(df.columns)
    columnas.remove('ID_Votante')
    
    print("\nCampos disponibles para modificar: ")
    print(columnas)

    while True :
        campo = input("Ingrese el campo a modificar (o 'fin' para terminar): ")
        
        if campo.lower() == 'fin': #### COMENTARIO: VERIFICAR PORQUE DA ERROR SI UNO NO LO PONE TODO EN MINÚSCULA
            break
        
        if campo not in columnas:
            print("Campo inválido.")
            continue
        
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        df.at[indice_fila, campo] = nuevo_valor #### ----------> AGREGAR QUÉ ES .at[]

    df.to_csv(archivo, index = False)
    
    fila = df.loc[indice_fila]
    
    participantes[id_modificar] = Votante(
        fila['ID_Votante'], fila['Genero'], fila['Edad'], 
        fila['Circunscripcion'], fila['Nivel_Socioeconomico'], 
        fila['Nivel_Educativo'], fila['Afiliacion_Politica'],
        fila['Interes_Politica'], fila['Preocupacion_Economia'], 
        fila['Preocupacion_Seguridad'], fila['Opinion_Gobierno_Actual'], 
        fila['Percepcion_Corrupcion'], fila['Intencion_Voto'],
        fila['Disposicion_Cambiar_Voto'], fila['Participacion_Voto_Anterior']
    )
    
    return participantes


def mostrar_resultados_elecciones(partido_A, partido_B, partido_C):
    '''
    Muestra los resultados de las elecciones y printea el partido ganador. Esta funcion utiliza el metodo 'total_votantes' del 
    objeto 'Partido'. Devuelve los valores de la cantidad de votos de cada partido.

    Parameters
    ----------
    partido_A : objeto
        Objeto de la  clase 'Partido', es el 'Partido A'.
    partido_B : objeto
        Objeto de la  clase 'Partido', es el 'Partido B'.
    partido_C : objeto
        Objeto de la  clase 'Partido', es el 'Partido C'.

    Returns
    -------
    votos_A : int
        Devuelve un numero entero de los votos del Partido A.
    votos_B : int
        Devuelve un numero entero de los votos del Partido B.
    votos_C : int
        Devuelve un numero entero de los votos del Partido C.
    '''
    votos_A = partido_A.total_votantes()
    votos_B = partido_B.total_votantes()
    votos_C = partido_C.total_votantes()
    
    if votos_A > votos_B and votos_A > votos_C:
        print(f"Partido A ganó con {votos_A} votos.")
    elif votos_B > votos_A and votos_B > votos_C:
        print(f"Partido B ganó con {votos_B} votos.")
    elif votos_C > votos_A and votos_C > votos_B:
        print(f"Partido C ganó con {votos_C} votos.")
    else:
        print("Empate")
    
    return votos_A, votos_B, votos_C


def clasificar_nivel_socioeconomico(partido_A, partido_B, partido_C, diccionario) : #CAMBIAR NOMBRE FUNCION 
    '''
    Clasifica a los votantes de cada partido según su nivel socioeconómico (bajo, medio, alto) y devuelve la cantidad de votantes en cada nivel.
    Utiliza el método 'clasificar_votantes()' de los objetos 'Partido' para la clasificacion de los votantes en cada nivel socioeconomico
    Tambien, calcula la cantidad de votantes en cada nivel para los tres partidos y devuelve estos valores.
    
           
    Parameters
    ----------
    partido_A : objeto
        Objeto de la  clase 'Partido', es el 'Partido A'.
    partido_B : objeto
        Objeto de la  clase 'Partido', es el 'Partido B'.
    partido_C : objeto
        Objeto de la  clase 'Partido', es el 'Partido C'.
    diccionario : dict
        Diccionario con los objetos, la clave es un identificador unico (numero del 1 al ultimo elemento)
        y el valor es el objeto 'Votante'.
    
    Returns
    -------
    cantidad_A_bajo : int
        Votantes de 'Partido A' con nivel socioeconómico bajo.
    cantidad_A_medio : int
        Votantes de 'Partido A' con nivel socioeconómico medio.
    cantidad_A_alto : int
        Votantes de 'Partido A' con nivel socioeconómico alto.
    cantidad_B_bajo : int
        Votantes de 'Partido B' con nivel socioeconómico bajo.
    cantidad_B_medio : int
        Votantes de 'Partido B' con nivel socioeconómico medio.
    cantidad_B_alto : int
        Votantes de 'Partido B' con nivel socioeconómico alto.
    cantidad_C_bajo : int
        Votantes de 'Partido C' con nivel socioeconómico bajo.
    cantidad_C_medio : int
        Votantes de 'Partido C' con nivel socioeconómico medio.
    cantidad_C_alto :int
        Votantes de 'Partido C' con nivel socioeconómico alto.
    
    '''
    A_bajo, A_medio, A_alta = partido_A.clasificar_votantes(diccionario)
    B_bajo, B_medio, B_alta = partido_B.clasificar_votantes(diccionario)
    C_bajo, C_medio, C_alta = partido_C.clasificar_votantes(diccionario)
    
    #Cantidad por condición socioeconomica    
    cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto = len(A_bajo), len(A_medio), len(A_alta)
    cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto = len(B_bajo), len(B_medio), len(B_alta)
    cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto = len(C_bajo), len(C_medio), len(C_alta)
    
    return cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto, cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto, cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto

    
def predecir_votantes_elecciones(df, umbral = 4.0) :
    '''
    Predice la cantidad de votantes que participarán en las elecciones, basándose en la participación anterior 
    y el interés político de los votantes utilizando el DataFrame. Calcula la cantidad de votantes que cumplen con estos

    Luego calcula cuántos votantes cumplen con estos criterios y estima el porcentaje sobre el total de votantes.

    
    Parameters
    ----------
    df : dataframe
        Datframe que contiene los datos de los votantes
    umbral : float, optional
        Umbral mínimo de interés político. El valor por defecto es 4.0. Los votantes con un valor mayor o igual a este umbral
        serán considerados para el cálculo. 

    Returns
    -------
    total_votantes_estimado : int
        Número total estimado de votantes que participarán en las elecciones
    porcentaje_redondeado : float
        Porcentaje de votantes estimados con respecto al total de votantes en el DataFrame, redondeado a dos decimales.


    '''
    #Filtramos los votantes que votaron antes y que tienen un alto interés político
    df_filtrado = df[(df['Participacion_Voto_Anterior'] == 'Sí') & (df['Interes_Politica'] >= umbral)]
    
    #Calculamos el total
    total_votantes_estimado = len(df_filtrado)
    
    #Lo convertimos en porcentaje
    porcentaje = 100 * total_votantes_estimado / len(df)
    porcentaje_redondeado = round(porcentaje, 2)

    print(f'Se estima que votarán en las elecciones {total_votantes_estimado} personas o el {porcentaje_redondeado}% del total.')

    return total_votantes_estimado, porcentaje_redondeado


#______________________________________________________________________________

# ii. ANALIZAR DATOS - VISUALIZACIÓN

### MENÚ 3

## 1. Gráfico de Barras
def graficar_barras(cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto, cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto, cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto):
    '''
    Grafica un diagrama de barras comparando los niveles socioeconómicos (bajo, medio y alto) para tres partidos (A, B y C).
    Muestra el gráfico en la parte de visualización de variables.

    Parameters
    ----------
    cantidad_A_bajo : int
        Cantidad de votantes de nivel socioeconómico bajo en el Partido A.
    cantidad_A_medio : int
        Cantidad de votantes de nivel socioeconómico medio en el Partido A.
    cantidad_A_alto : int
        Cantidad de votantes de nivel socioeconómico alto en el Partido A.
    cantidad_B_bajo : int
        Cantidad de votantes de nivel socioeconómico bajo en el Partido B.
    cantidad_B_medio : int
        Cantidad de votantes de nivel socioeconómico medio en el Partido B.
    cantidad_B_alto : int
        Cantidad de votantes de nivel socioeconómico alto en el Partido B.
    cantidad_C_bajo : int
        Cantidad de votantes de nivel socioeconómico bajo en el Partido C.
    cantidad_C_medio : int
        Cantidad de votantes de nivel socioeconómico medio en el Partido C.
    cantidad_C_alto : int
        Cantidad de votantes de nivel socioeconómico alto en el Partido C.

   '''
    # Datos utilizados (reemplazá estos con los valores reales obtenidos de la función)
    partidos = ("Partido A", "Partido B", "Partido C")
    nivel_socioeconomico = {
        'Bajo': (cantidad_A_bajo, cantidad_B_bajo, cantidad_C_bajo),
        'Medio': (cantidad_A_medio, cantidad_B_medio, cantidad_C_medio),
        'Alto': (cantidad_A_alto, cantidad_B_alto, cantidad_C_alto),
    }
    
    x = np.arange(len(partidos))  # posiciones para las barras
    width = 0.25  # ancho de cada barra
    multiplier = 0
    
    fig, ax = plt.subplots(layout='constrained')
    
    # Dibujar barras para cada nivel socioeconómico
    for nivel, valores in nivel_socioeconomico.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, valores, width, label=nivel)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    
    # Etiquetas y estética
    ax.set_ylabel('Cantidad de votantes')
    ax.set_title('Resultado de las elecciones (clasificado por sector socioeconómico)')
    ax.set_xticks(x + width, partidos)
    ax.legend(title='Nivel socioeconómico', loc='upper left', ncols=3)
    ax.set_ylim(0, max(map(max, nivel_socioeconomico.values())) + 5)
    
    plt.show()


## 2. Gráfico de Torta - DOCUMENTAR MEJOR LO QUE HICIMOS

def graficar_torta(partido_A, partido_B, partido_C) :
    ''' REVISAR DOC
    Genera un gráfico de torta con los resultados de voto para tres partidos y los votos indecisos. Luego lo muestra en 
    visualizacion de variables.
    

    
    partido_A : str
        Nombre o identificador del Partido A, que se pasa a
        `mostrar_resultados_elecciones` para obtener su recuento de votos.
    partido_B : str
        Nombre o identificador del Partido B, que se pasa a
        `mostrar_resultados_elecciones` para obtener su recuento de votos.
    partido_C : str
        Nombre o identificador del Partido C, que se pasa a
        `mostrar_resultados_elecciones` para obtener su recuento de votos.

    Parameters
    ----------
    partido_A : int
        
    partido_B : int
        
    partido_C : int
        

    '''
    # Llamamos a la función mostrar_resultados_elecciones y obtenemos los votos
    votos_A, votos_B, votos_C = mostrar_resultados_elecciones(partido_A, partido_B, partido_C)
    
    # Contamos los votos indecisos de la columna 'Intencion_Voto'
    votos_indecisos = df[df['Intencion_Voto'] == 'Indeciso'].shape[0]
    
    #Creamos el gráfico
    plt.style.use('_mpl-gallery-nogrid')
    
    labels = ['Partido A', 'Partido B', 'Partido C', 'Indecisos']
    sizes = [votos_A, votos_B, votos_C, votos_indecisos] #PREGUNTAR QUE ES
    colors = plt.get_cmap('Blues')(np.linspace(0.3, 0.7, len(sizes)))
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    wedges, texts, autotexts = ax.pie(sizes, autopct ='%1.1f%%', colors = colors, startangle = 90, 
           wedgeprops = {"linewidth": 1, "edgecolor": "white"})
    
    for text in autotexts:
        text.set_color('white')           # Color del texto interno
        text.set_fontsize(12)             # Tamaño de fuente
        text.set_fontweight('bold')       # Negrita (opcional)
        text.set_fontfamily('sans-serif') # Tipo de fuente (opcional)
     
    # Agregar leyenda en esquina inferior derecha
    ax.legend(wedges, labels, loc='lower right')
    
    ax.set_title('Resultados de las Elecciones')
    
    # Aseguramos que el gráfico sea circular
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


#_____________________________________________________________________________

### MENUS (FUNCIONES)

def menu_2(archivo):
    '''
    Ejecuta el ciclo del submenú de modelar datos.

    Este menú permite al usuario:
      1. Agregar registro de voto.
      2. Modificar un registro existente.
      3. Mostrar el partido ganador de las elecciones.
      4. Clasificar a los votantes según su nivel socioeconómico.
      5. Volver al MENU 1.

    
    Parameters
    ----------
    archivo : str
        Ruta del archivo para acceder a la informacion

    Raises
    ------
    ValueError
        Si el usuario ingresa una opción que no puede convertirse a entero o que no corresponde a 
        ninguna de las opciones disponibles (1–5).

    Returns
    -------
    None.

    '''
    
    #Instancias de Objetos        
    partido_A = Partido("Partido A")
    partido_B = Partido("Partido B")
    partido_C = Partido("Partido C")
    participantes, df = cargar_datos(archivo,partido_A,partido_B,partido_C)
    
    while True:
        print("\nMENU 2:")
        print("1 - Agregar registro")
        print("2 - Modificar registro")
        print("3 - Mostrar partido ganador")
        print("4 - Clasificación según nivel socioeconómico")
        print("5 - Volver a MENU 1")

        try:
            opcion = int(input("Ingrese el número de la opción que desea elegir: "))
            if opcion == 1:
                agregar_registro(participantes, partido_A, partido_B, partido_C)
            elif opcion == 2:
                participantes = modificar_registro(df, participantes, archivo)
                actualizar_datos(archivo, participantes)
            elif opcion == 3:
                mostrar_resultados_elecciones(partido_A, partido_B, partido_C)
            elif opcion == 4:
                clasificar_nivel_socioeconomico(partido_A, partido_B, partido_C, participantes)
            elif opcion == 5:
                menu(df)  # volver al menú principal
                break
            else:
                print("Esa Opción no es válida.")
        except ValueError:
            print("ingrese una de las opciones ofrecidad")
    
    
        
    
        # llamo a la funcion de clasificar nivel socio economico


def menu_3(participantes, df,partido_A,partido_B,partido_C ):
    ''' FALTA EL VALUE ERROR EN EL DOC Y EN LA FUNCION
    
    Muestra el menú que genera reportes gráficos e imprime datos de los resultados electorales. También predice
    el número de votantes.

    Parameters
    ----------
    participantes : list
        Lista con información del nivel socioeconómico y participación previa.
    df : dataframe
        DataFrame con los datos de los votantes para realizar la predicción.
    partido_A : objeto
        Contiene los resultados y datos del Partido A.
    partido_B : objeto
        Contiene los resultados y datos del Partido A.
    partido_C : objeto
        Contiene los resultados y datos del Partido A.

    Raises
    ------
    ValueError
        

    Returns
    -------
    None.

    '''
    while True:
        print("\nMENU 3:  \n1 - Gráfico de barras, \n2 - Gráfico de torta, \n3 - Imprimir datos, \n4 - Volver a MENU 1")
        try:
            opcion = int(input("Ingrese el número de la opción que desea elegir: "))
            if opcion == 1:
                cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto, cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto, cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto = clasificar_nivel_socioeconomico(partido_A, partido_B, partido_C, participantes)
                graficar_barras(cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto, cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto, cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto)
            elif opcion == 2:
                mostrar_resultados_elecciones(partido_A, partido_B, partido_C)
                graficar_torta(partido_A, partido_B, partido_C)
                    # funcion de la barra de torta
                    # los de el menu 2        
            elif opcion == 3:
                mostrar_resultados_elecciones(partido_A, partido_B, partido_C)
                predecir_votantes_elecciones(df, umbral = 4.0)
            elif opcion == 4:
                menu(df)
                break
            else:
                print("Esa opcion no es valida")
        except ValueError:
            print("ingrese una de las opciones ofrecidad")

     
        
def validar_carga_datos(df,archivo):
    '''
    La funcion evalua si el df esta vacio

    Parameters
    ----------
    df : dataframe
        Devuelve el df con los datos de los votantes.
    archivo : str
        El archivo que contiene los datos 

    Returns
    -------
    bool
        
    '''
    
    if df.empty:
        return False
    
    else:
        return True


def menu(df):
    '''
    Muestra el menú principal para modelar o analizar datos electorales.Se usa el DataFrame para validar y
    cargar la información antes de pasar a los submenús.

    Parameters
    ----------
    df : dataframe
        DataFrame con la información de los votantes.
        
    Raises
    ------
    ValueError
        Si se ingresa una opción fuera del rango válido (1, 2 o 3).

    Returns
    -------
    None.

    '''
    
    try:
        print("\nMENU 1: \n1 - Modelar datos, \n2 - Analizar datos, \n3 - Fin")
        opcion = int(input("Ingrese el número de la opción que desea elegir: "))
        if opcion == 1:
            menu_2(archivo)
        elif opcion == 2:
            # Instancias de Objetos        
                partido_A = Partido("Partido A")
                partido_B = Partido("Partido B")
                partido_C = Partido("Partido C")
            
                validacion = validar_carga_datos(df, archivo)
                
                if not validacion:
                      participantes, df = cargar_datos(archivo, partido_A, partido_B, partido_C)
                else:
                    participantes, _ = cargar_datos(archivo, partido_A, partido_B, partido_C)  # Volvés a cargar aunque ya esté validado

                menu_3(participantes, df, partido_A, partido_B, partido_C)
                
        elif opcion == 3:
                print("SE HA TERMINADO EL PROGRAMA.")
        else:
            print("Esa opcion no es valida")
    except ValueError:
        print("ingrese una de las opciones ofrecidad")
        
            
    
    
    

#Llamamos al MENU 1
menu(df)
