#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test de modificacion de archivo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ejercicio1():
    
    """
    UTILIZAR SOLAMENTE BUCLES WHILE
    1. Crea un array a partir de una lista de números con decimales (los que tu consideres, 4 o
    5 números). Imprime sus valores uno a uno mediante un bucle while y los atributos del array
    (dimensiones, tamaño, tipo de dato, shape).
    """
    import numpy as np
    myarray=np.array([1.2,3.2,5.2,4.9,9.1])
    contador=0
    while contador<myarray.size:
        print ("elemento ",contador+1, "del array es= ",myarray[contador])
        contador=contador+1        
    print ("dimension ",myarray.ndim)
    print ("Número de elementos que contiene ",myarray.size)
    print ("tipo de los elementos ",myarray.dtype)
    return()
    
def ejercicio2():
    
    """
    2. Crear una función “inicializar_array” que reciba por parámetro un array de 1 dimensión de
    tipos enteros y devuelva el array inicializado/modificado con valores introducidos por teclado
    (solamente enteros). Utilizar un while para recorrer el array.
    """

    import numpy as np
    myarray=np.array([1,2,3,4,5,6,7,8])
    print (myarray)


    def inicializar_array (array):
        contador=0
        aux=array.size
        while contador<array.size:
            array[contador]=int(input(f"Introduce un numero que quieras añadir a el array en la posicion {contador+1}:"))
            contador=contador+1  
        return (array)

    myarray=inicializar_array(myarray)
    print (myarray)

def ejercicio3():
    
    """
    Crear las funciones “media”, “máximo”, “mínimo” que reciba un array de valores
    numéricos y devuelva la media aritmética, el valor máximo y el valor mínimo
    respectivamente. Realizar el cálculo manualmente recorriendo el array con un while.
    """

    import numpy as np

    def media (array):
        aux=array.size
        suma=0
        contador=0
        while (contador<aux):
            suma=suma+array[contador]
            contador=contador+1
        return (suma/aux)
    
    def máximo (array):
        aux=array.size
        max=array[0]
        contador=1
        while contador<aux:
            if max<array[contador]:
               max=array[contador]
               contador=contador+1

        return(max)
    
    def minimu (array):
        aux=array.size
        min=array[0]
        contador=1
        while contador<aux:
            if min>array[contador]:
               min=array[contador]
               contador=contador+1
        return(min)
            
    myarray=np.array([1,2,3,4,5,6,7,8])
    print (myarray)
        
    mediarit=media(myarray)
    print(mediarit)

    maximo=máximo(myarray)
    print(maximo)

    minimo=minimu(myarray)
    print(minimo)   
    
def ejercicio4():
    
    """
    4. Crear la función “encontrar” (usando while) que reciba dos parámetros: un array numérico
    y un valor. La función debe buscar en el array si el “valor” se encuentra en él. La función
    debe devolver:
        ○Si valor se encuentra en el array, devolver el índice (primera aparición)
        ○Si el valor no se encuentra en el array, devolver -1.
    """

    import numpy as np

    def encontrar (array,valor):
        aux=array.size
        contador=0
        while (contador<aux):
            if valor==array[contador]:
                print("dentro")
                return(contador)
            contador=contador+1
            print(contador)
        return (-1)
    
    
    myarray=np.array([1,2,3,4,5,6,7,8])
    print (myarray)
        
    testigo=encontrar(myarray,3)
    print(testigo)
    
def ejercicio5():
    
    """
    5. Crear una función “desviación estándar” que reciba por parámetro un array y devuelva la
    desviación estándar. Calcular paso a paso el resultado utilizando un while para recorrer el
    array. También se debe usar la función “media” del ejercicio 2. Para calcular la raíz
    cuadrada podemos usar la función de numpy.sqrt(n). Operador potencia es **
    """

    import numpy as np
    
    def desviación_estándar (array):
        aux=array.size
        suma=0
        contador=0
        while (contador<aux):
            suma=suma+array[contador]
            contador=contador+1
            media=suma/aux
            print(media)
            contador=0
            distancia=0
        while (contador<aux):
            distancia=distancia+(array[contador]-media)**2
            desv=(distancia/aux)**.5
            contador=contador+1
        return(desv)
    
    myarray=np.array([5,5,5,5,5,5,5,5])
    print (myarray)    
    de=desviación_estándar (myarray)
    print(de)

ejercicio3()

