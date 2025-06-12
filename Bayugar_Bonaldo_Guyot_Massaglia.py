import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
        

    def clasificar_votantes(self, dicc_personas):
        clase_baja = []
        clase_media = []
        clase_alta = []
    
        for votante_id in self.lista_votantes:
            votante = dicc_personas[votante_id]
            clase = votante.nivel_socioeconomico
            if clase == "Bajo":
                clase_baja.append(votante_id)
            elif clase == "Medio":
                clase_media.append(votante_id)
            elif clase == "Alto":
                clase_alta.append(votante_id)
    
        return clase_baja, clase_media, clase_alta
    
    
    def total_votantes(self):
        return len(self.lista_votantes)
     
archivo = 'Decision_Voto_Elecciones.csv'

#Instancias de Objetos        
partido_A = Partido("Partido A")
partido_B = Partido("Partido B")
partido_C = Partido("Partido C")

#______________________________________________________________________________

### MENÚ 2

## 1. Agregar Registros

## 2. Modificar Registros

## 3. Promedio Votos

## 4. Máximo de Votos (ganador elecciones)

## 5. Volver al Menú anterior
#______________________________________________________________________________

## FUNCIONES

def cargar_datos(archivo):
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

    while True : #CAMBIAR PARA QUE ESTO NO PASE POR DEFAULT
        campo = input("Ingrese el campo a modificar (o 'fin' para terminar): ")
        
        if campo.lower() == 'fin':
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


def mostrar_resultados_elecciones(partido_A, partido_B, partido_C):
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
    A_bajo, A_medio, A_alta = partido_A.clasificar_votantes(diccionario)
    B_bajo, B_medio, B_alta = partido_B.clasificar_votantes(diccionario)
    C_bajo, C_medio, C_alta = partido_C.clasificar_votantes(diccionario)
    
    #Cantidad por condición socioeconomica    
    cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto = len(A_bajo), len(A_medio), len(A_alta)
    cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto = len(B_bajo), len(B_medio), len(B_alta)
    cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto = len(C_bajo), len(C_medio), len(C_alta)
    
    return cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto, cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto, cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto

    
def predecir_votantes_elecciones(df, umbral = 4.0) :
    #Filtramos los votantes que votaron antes y que tienen un alto interés político
    df_filtrado = df[(df['Participacion_Voto_Anterior'] == 'Sí') & (df['Interes_Politica'] >= umbral)]
    
    #Calculamos el total
    total_votantes_estimado = len(df_filtrado)
    
    #Lo convertimos en porcentaje
    porcentaje = 100 * total_votantes_estimado / len(df)
    porcentaje_redondeado = round(porcentaje, 2)

    print(f'Se estima que votarán en las elecciones {total_votantes_estimado} personas o el {porcentaje_redondeado}% del total.')

    return total_votantes_estimado, porcentaje_redondeado
   

#CÓDIGO PRINCIPAL
participantes, df = cargar_datos(archivo)    
participantes = modificar_registro(df, participantes, archivo)
actualizar_datos(archivo, participantes)

cantidad_A_bajo, cantidad_A_medio, cantidad_A_alto, cantidad_B_bajo, cantidad_B_medio, cantidad_B_alto, cantidad_C_bajo, cantidad_C_medio, cantidad_C_alto = clasificar_nivel_socioeconomico(partido_A, partido_B, partido_C, participantes)

#______________________________________________________________________________

# ii. ANALIZAR DATOS - VISUALIZACIÓN

### MENÚ 3

## 1. Gráfico de Barras
def graficar_barras() :
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

def graficar_torta() :
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

#Llamamos a los gráficos
graficar_barras()
graficar_torta()

## 3. Mostrar resultados df por consola
mostrar_resultados_elecciones(partido_A, partido_B, partido_C)
#______________________________________________________________________________

##LAMADOS DE DATOS PARA VERIFICAR COSAS
centro = df[df['Afiliacion_Politica'] == 'Centro'] # --> Partido A / Indeciso
izquierda = df[df['Afiliacion_Politica'] == 'Izquierda'] # --> Partido C / Indeciso
derecha = df[df['Afiliacion_Politica'] == 'Derecha'] # --> Partido B / Indeciso
 
