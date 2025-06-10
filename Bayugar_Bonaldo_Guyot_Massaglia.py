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
        self.afiliacion_politica = afiliacion_politica
        self.lista_votantes = []#lista con los votantes afiliados a un partido
        #METODOS
        
    def agregar_votantes(self,votante):
        self.lista_votantes.append(votante)
        
    def clasificar_votantes(self,dicc_personas):
        clase_baja=[]
        clase_media=[]
        clase_alta=[]
        for clave, valor in dicc_personas.items():
            for votante in self.lista_votantes:
                if clave == votante:
                    clase = valor.nivel_socioeconomico
                    if clase == "Baja":
                        clase_baja.append(votante)
                    elif clase == "Media":
                         clase_media.append(votante)
                    elif clase == "Alta":
                         clase_alta.append(votante)

           
        return clase_baja, clase_media, clase_alta


        
partido_A = Partido("Partido A")
partido_B = Partido("Partido B")
partido_C = Partido("Partido C")

def guardar_partidos(partido_A, partido_B, partido_C):
    A_bajo, A_medio, A_alta = partido_A.clasificar_votantes()
    B_bajo, B_medio, B_alta = partido_B.clasificar_votantes()
    C_bajo, C_medio, C_alta = partido_C.clasificar_votantes()
    print(A_bajo, A_medio, A_alta)
    
    
    

#______________________________________________________________________________
#CÓDIGO PRINCIPAL     

#______________________________________________________________________________

### MENÚ 2

## 1. Agregar Registros

## 2. Modificar Registros

## 3. Promedio Votos

## 4. Máximo de Votos (ganador elecciones)

## 5. Volver al Menú anterior

## FUNCIONES

def cargar_datos(archivo):
    df = pd.read_csv(archivo)
    
    personas = {}
    columnas = list(df.columns)
    
    
    for i, fila in df.iterrows():
        valores = []
        for col in columnas :
            valor = fila[col]  # obtenemos el valor que corresponde a la columna actual
            valores.append(valor)  # lo agregamos a la lista de valores
        nombre = i
        persona = Votante(* valores)
        personas[nombre] = persona
        
        if persona.intencion_voto == "Partido A":
            partido_A.agregar_votantes(nombre)
        elif persona.intencion_voto == "Partido B":
            partido_B.agregar_votantes(nombre)
        
        elif persona.intencion_voto == "Partido C":
            partido_C.agregar_votantes(nombre)
    
    return personas, df


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
                
                'Preocupacion_Economia': votante.preocupacion_economia,
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
        
        if campo == 'fin':
            break
        
        if campo not in columnas:
            print("Campo inválido.")
            continue
        
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        df.at[indice_fila, campo] = nuevo_valor #### ----------> FIJARSE QUÉ ES .at[]

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


archivo = 'Decision_Voto_Elecciones.csv'
participantes, df = cargar_datos(archivo)

participantes = modificar_registro(df, participantes, archivo)
actualizar_datos(archivo, participantes)

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
 
