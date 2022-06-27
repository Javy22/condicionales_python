# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda


#1

if texto_1 > texto_2:
    print('La primer palabra es mayor que la segunda palabra')
else:
    print('La segunda palabra es mayor que la primera')

#2
if len(texto_1) > len(texto_2):
    print('La primer palabra tiene mas caracteres que la segunda')
else:
    print('la segunda palabra tiene más caracteres')
#3
if texto_1[0] > texto_2[0]:
    print('el primer caracter de la primer palabra es mayor a al primer caracter del texto_2') 
else:
    print('Consigna no cumplida')

 # Copia de la variable texto_1
copia_texto_1 = texto_1  

#1
if copia_texto_1 == texto_1:
    print('Palabras iguales')
        
#2
if copia_texto_1 != texto_2:
    print('Palabras distintas')