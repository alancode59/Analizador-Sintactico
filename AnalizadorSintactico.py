#Universidad Politècnica de Tlaxcala

#Actividad: Analizador Sintactico en Python.

#Integrantes del equipo:
                         #Alan Zaid Hernandez Cruz
                         #Ana Karen Ramirez Arenas
                         #Ivan de Jesus Ojeda Reyes

#8C

#Fecha de entrega: 21/03/23

import string
import re

print('Analizador Sintactico')

# Diccionario de datos mediante [Reglas de Produccion]
sustantivos = ( 'perro', 'gato', 'casa', 'pájaros', 'Juan', 'calle', 'ciudad', 'libro', 'comida', 'parque', 'amiga',
                'cielo', 'agua', 'vecina', 'cama', 'música', 'ropa', 'coche', 'escuela', 'trabajo', 'amigo', 'árboles',
                'familia', 'guitarra', 'sol', 'lluvia', 'mar', 'montaña', 'oso', 'fiesta',  'árbol', 'aire', 'audífonos', 'vida', 'historia', 'Alan', 'Karen', 'oportunidad', 'fiesta', 'cumpleaños', 'amigo', 'movimientos', 'música',
                'película', 'futuro', 'idea', 'problema', 'país', 'planeta', 'María', 'acción', 'día')

sujeto = ('Ana', 'Karen', 'Alan', 'Ivan', 'Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Sofía', 'Roberto', 'Lucía', 'Carlos', 'Él',
          'Laura', 'Miguel', 'Carmen', 'Javier', 'Isabel', 'Francisco', 'Elena', 'el sol' 'Fernando', 'Silvia', 'Antonio',
          'Raquel', 'sol', 'pájaros', 'nosotros')

verbo = ('corre', 'baila', 'canta', 'come', 'camina', 'duerme', 'mira', 'sigue', 'enseñó',  'suena', 'comprar', 'vende', 'trabaja', 'había querido', 'había tenido', 'sentía', 'decidió', 'seguir', 'intentando', 
         'estudia', 'brilló', 'cantaban', 'caminó', 'ver', 'compramos', 'disfrutamos')

adjetivos = ('alto', 'bajo', 'nublado', 'negro', 'fielmente', 'bonito', 'feo', 'fuerte', 'rápidamente', 'gordo', 'delgado',
             'amable', 'desagradable', 'inteligente', 'tonto', 'fuerte', 'débil', 'rico', 'pobre', 'largo', 'corto', 'incómodo', 'viejo',
             'nuevo', 'feliz', 'triste', 'interesante', 'aburrido', 'divertido', 'serio', 'alegre', 'cansado', 'enérgico',
             'caliente', 'frío', 'rápido', 'lento', 'intensamente', 'alegremente', 'nueva', 'de acción', 'juntos', 'nueva',
             'emocionada', 'alegremente', 'encantó', 'mucho.')


articulos = ('el', 'la', 'los', 'las', 'un', 'mi', 'una', 'unos', 'unas', 'Él')

pronombres = ( 'yo', 'tu', 'él', 'ella', 'usted', 'los' 'nosotros', 'le', 'nos', 'nosotras', 'vosotros', 'vosotras',
               'ellos', 'ellas', 'ustedes', 'mi', 'conmigo', 'ti', 'contigo', 'sí', 'consigo', 'su', 'los dos')

preposiciones = ( 'a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'porque', 'de', 'en', 'hasta',
                  'juntos', 'mediante', 'para', 'por', 'según', 'sin', 'sobre', 'tras')

conjunciones = ('y', 'o', 'no', 'si', 'solo si', 'es', 'no es', 'pero')

# definir patrones de mayusculas
mayuscula = r'^\w*[A-ZÁÉÍÓÚÑ]\w*$'

# definir patrones de signos
puntuacion = r'^[.,;:?!]+$'

# Solicitamos una entrada de usuario
parrafo = input("Ingresa un parrafo: ")

# Separamos la entrada en palabras individuales
palabras = parrafo.split()

# Creamos una cadena vacía donde agregaremos las palabras entre corchetes
palabras_entre_corchetes = ""

# Creamos una lista vacía para las palabras
sustantivos_palabras = []
sujeto_palabras = []
verbo_palabras = []
adjetivo_palabras = []
articulos_palabras = []
pronombres_palabras = []
preposiciones_palabras = []
conjunciones_palabras = []
mayusculas_palabras = []
puntuacion_signos = []


for palabra in palabras:
    palabras_entre_corchetes += "[" + palabra + "] "  # Agregamos cada palabra entre corchetes y un espacio
    if palabra in sujeto:
        sujeto_palabras.append(palabra)

    if palabra in verbo:
        verbo_palabras.append(palabra)

    if palabra in adjetivos:
        adjetivo_palabras.append(palabra)

    if palabra in sustantivos:
        sustantivos_palabras.append(palabra)

    if palabra in articulos:
        articulos_palabras.append(palabra)

    if palabra in pronombres:
        pronombres_palabras.append(palabra)

    if palabra in preposiciones:
        preposiciones_palabras.append(palabra)

    if palabra in conjunciones:
        conjunciones_palabras.append(palabra)

    if re.match(mayuscula, palabra):
        mayusculas_palabras.append(palabra)

    if re.match(puntuacion, palabra):
        puntuacion_signos.append(palabra)

print('Palabras separadas:')
print(palabras_entre_corchetes)  # Imprimimos el resultado
print('\n')

# Si hay palabras del sujeto, las imprimimos [REGLA SUJETO]
if verbo_palabras:
    print("El parrafo contiene los siguientes [Verbos]:", verbo_palabras)
else:
    print("Verbo no valido.")

print('\n')

if adjetivo_palabras:
    print("El parrafo contiene los siguientes [Ajetivos]:", adjetivo_palabras)
else:
    print("Adjetivo no valido.")

print('\n')

if sustantivos_palabras:
    print("El parrafo contiene los siguientes [Sustantivos]:", sustantivos_palabras)
else:
    print("Sustantivo no valido.")

print('\n')

if sujeto_palabras:
    print("El parrafo contiene las siguientes palabras del [Sujeto]:", sujeto_palabras)
else:
    print("El parafo no tiene un sujeto válido.")

print('\n')

if articulos_palabras:
    print("El parrafo contiene las siguientes palabras de [ARTICULOS]:", articulos_palabras)
else:
    print("El parafo no tiene un articulos en este parrafo.")

print('\n')

if pronombres_palabras:
    print("El parrafo contiene las siguientes palabras de [PRONOMBRES]:", pronombres_palabras)
else:
    print("El parafo no tiene pronombres en este parrafo.")

print('\n')
if preposiciones_palabras:
    print("El parrafo contiene las siguientes palabras de [PREPOSICIONES]:", preposiciones_palabras)
else:
    print("El parafo no tiene preposiciones en este parrafo.")

print('\n')

if conjunciones_palabras:
    print("El parrafo contiene las siguientes palabras de [CONJUNCIONES]:", conjunciones_palabras)
else:
    print("El parafo no tiene conjunciones en este parrafo.")

print('\n')

if mayusculas_palabras:
    print("El parrafo contiene las siguientes palabras en [MAYUSCULAS]:", mayusculas_palabras)
else:
    print("El parafo no tiene Mayusculas en este parrafo.")

print('\n')

if puntuacion_signos:
    print("El parrafo contiene los siguientes [SIGNOS DE PUNTUACION]:", puntuacion_signos)
else:
    print("El parafo no tiene Signos de puntuacion en este parrafo.")
print('\n')

while parrafo.startswith(articulos):

    if len(palabras) > 0:
        articulo_encontrado = False
        sustantivos_encontrado = False
        verbo_encontrado = False
        adjetivo_encontrado = False

        for i in range(len(palabras)):
            if palabras[i] in articulos:
                articulo_encontrado = True
            elif palabras[i] in sustantivos:
                sustantivos_encontrado = True
            elif palabras[i] in verbo:
                verbo_encontrado = True
            elif palabras[i] in adjetivos:
                adjetivo_encontrado = True

        if articulo_encontrado and sustantivos_encontrado and verbo_encontrado and adjetivo_encontrado:
            print("El parrafo esta bien porque contiene un Articulo, sustativo, verbo y adjetivo")
            print('\n')
        else:
            print("El parrafo no cumple con la estructura correcta")
            print('\n')

    break

while parrafo.startswith(sujeto):

    if len(palabras) > 0:
        sujeto_encontrado = False
        verbo_encontrado = False
        adjetivo_encontrado = False

        for i in range(len(palabras)):
            if palabras[i] in sujeto:
                sujeto_encontrado = True
            elif palabras[i] in verbo:
                verbo_encontrado = True
            elif palabras[i] in adjetivos:
                adjetivo_encontrado = True

        if sujeto_encontrado and verbo_encontrado and adjetivo_encontrado:
            print("El parrafo esta bien porque contiene un sujeto, verbo y adjetivo")
            print('\n')
        else:
            print("El parrafo no cumple con la estructura correcta")
            print('\n')

    break

while parrafo.startswith(pronombres):

    if len(palabras) > 0:
        puntuacion_emcontrada = False
        pronombre_encontrado = False
        sustantivos_encontrado = False
        verbo_encontrado = False

        for i in range(len(palabras)):
            if palabras[i] in puntuacion:
                puntuacion_emcontrada = True
            elif palabras[i] in pronombres:
                pronombre_encontrado = True
            elif palabras[i] in sustantivos:
                sustantivos_encontrado = True
            elif palabras[i] in verbo:
                verbo_encontrado = True

        if puntuacion_emcontrada and pronombre_encontrado and sustantivos_encontrado and verbo_encontrado:
            print("El parrafo esta bien porque es una pregunta con pronombres, sustantivos verbos y signos de interrogacion")
            print('\n')
        else:
            print("El parrafo no cumple con la estructura correcta")
            print('\n')

    break

































