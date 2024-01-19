#Elaborado por: Emmanuel Naranjo Blanco 
#Fecha de Creación: 22/7/2019 6:45pm                                
#Fecha de última Modificación: 31/7/2019 8:00pm                     
#Versión: 3.7.2                   

#Importacion de librerias
import random
#Definicion de funciones
#----------------------------------------------------------------------------------
def convertir_bina_deci(numero):
    """    
    Funcionamiento: Convertir el valor de binario a decimal.
    Entradas: Numero binario(str).
    Salidas: Valor decimal(int).
    """
    binario=convertir_espejo(numero)
    decimal=0
    n=len(numero)-1
    while n>=0:
        if binario[n]=="1":
            decimal+=(2**(n))
        n-=1
    return decimal
#----------------------------------------------------------------------------------
def saber_palindromo(elemento):
    """
    Funcion: Determinar si una palabra es palindroma.
    Entrada: Elemento(str).
    Salida: Indica si la palabra es palindroma.
    """
    x=str(elemento)
    espejo=convertir_espejo(x)
    if espejo==x:
        return True
    else:
        return False
#----------------------------------------------------------------------------------
def convertir_espejo(elemento):
    """
    Funcion: invertir los caracteres de una palabra.
    Entrada: palabra(str)
    Salida: palabra en espejo(str)
    """
    x=len(str(elemento))-1
    alreves=""
    while 0<=x:
        alreves+=elemento[x]
        x-=1
    return alreves
#----------------------------------------------------------------------------------
def saber_primo(numero):
    """
    Funcion: Determinar si un numero es primo.
    Entrada: Numero(int)
    Salida: True/False
    """
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return True
#----------------------------------------------------------------------------------
def contar_digitos(numero):
    """
    Funcion: Contar la cantidad de digitos de un numero
    Entrada: Numero (int)
    Salida: Cantidad de digitos de un numero
    """
    digitos=0
    while numero!=0:
        numero=numero//10
        digitos+=1
    return digitos
#----------------------------------------------------------------------------------


#-------------------------------------- 1
def numero_abundante(numero):
    """
    Funcion: Determinar si un numero es abundante o no.
    Entrada: Número entero. 
    Salida: Imprime los divisores del número, la suma de estos y si el número es abundante o no.
    """
    divisores=[]
    suma=0
    try:
        while numero>=1:
            for i in range(1,numero+1):
                if numero%i==0:
                    divisores.append(i)
                    suma+=i
            if suma>2*numero:
                determinar="Es un número abundante."
                abundancia=suma-2*numero
            else:
                determinar="No es un número abundante."
                abundancia="No hay abundancia."
            print("Número recibido: ",numero)
            print("Divisores: ",divisores)
            print("Suma de los divisores: ",suma)
            print(determinar)
            print("Abundancia: ",abundancia)
            return ""
        return "El número ingresado debe ser mayor o igual que 1."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
        
#-------------------------------------- 2
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
def encripta_aux(palabra):
    """
    Funcion: Validar los datos para encriptar palabras a partir de las 27 letras del alfabeto.
    Entrada: Recibe una palabra (str).
    Salida: No tiene.
    """
    if palabra.isalpha() and palabra.islower():
        return encripta(palabra)
    for letra in palabra:
        if letra.isalpha()==False or letra not in abecedario:
            return (letra,-1)

def encripta(palabra):
    """
    Funcion: Encriptar palabras a partir de las 27 letras del alfabeto.
    Entrada: Recibe una palabra (str).
    Salida: Retorna el mensaje encriptado (str) y la clave escogida dentro de la funcion (int)
    """
    try:
        encriptado=""
        clave=random.randint(1,25)
        for i in palabra:
            posicion=abecedario.index(i)+clave
            if posicion<len(abecedario):
                encriptado+=abecedario[posicion].upper()
            else:
                posicion=posicion%27
                encriptado+=abecedario[posicion].upper()
        return encriptado,clave
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."

#-------------------------------------- 3
def pares_amigables_aux(lista):
    """
    Funcion: Valida los datos para determinar si un par de números son amgables o no.
    Entrada: Lista de elementos.
    Salida: No tiene
    """
    for elemento in lista:
        if lista.count(elemento)>1:
            return "Los números en la lista no pueden repetirse."
        elif str(elemento).isdigit()==False or elemento<=0:
            return "La lista debe contener solo números mayores que cero."
    return pares_amigables(lista)

def  pares_amigables(lista):
    """
    Funcion: Determina si un par de números son amgables o no.
    Entrada: Lista de números enteros positivos y diferentes entre si.
    Salida: Retorna una lista con las parejas de números amigables encontrados. 
    """
    try:
        amigables=[]
        divisores=[]
        for numero in lista:
            suma=0
            for i in range(1,numero):
                if numero%i==0:
                    suma+=i
            divisores.append(suma)
        for numero in lista:
            for elemento in divisores:
                if numero==elemento:
                    amigables.append([numero,lista[divisores.index(elemento)]])
                    lista.remove(lista[divisores.index(elemento)])
                    divisores.remove(elemento)
        return amigables
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 4
def fibonacci(terminos):
    """
    Funcion: Realiza la sucesión de Fibnacci.
    Entrada: Número entero mayor o igual que 1.
    Salida: Retorna una tupla con la cantidad de términos de la sucesión indicada anteriormente.
    """
    try:
        sucesion=[0,1]
        if terminos>=1 and str(terminos).isdigit()==True:
            if terminos==1:
                return "(0)"
            else:
                for i in range(2,terminos):
                    numero= sucesion[i-1]+sucesion[i-2]
                    sucesion.append(numero)
                return tuple(sucesion)
        return "Error: la entrada debe ser un entero >= 1"
    except:
        return "Ha ocurrido un error durante la ejecucion del ejercicio."
#-------------------------------------- 5
def serie(num1,num2,salto):
    """
    Funcion: Realiza una variable numerica con números enteros.
    Entrada: Recibe tres números enteros mayores o iguales que 1.
    Salida: Devuelve una serie de números con los números enteros sucesivos que estan en el rango indicado por los dos primeros numeros.
    """
    resultado=0
    try:
        if num1>0 and num2>0 and salto>0 and num1<=num2:
            while num1<=num2:
                potencia=contar_digitos(num1)
                resultado=(resultado*(10**potencia))+num1
                num1+=salto
            return resultado
        return "Los datos ingresados deben ser números enteros positivos. El segundo número debe ser mayor que el primero."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
            
#-------------------------------------- 6
def semiprimos(num1,num2):
    """
    Funcion: Buscar números primos y semiprimos en un intervalo de números dado.
    Entrada: Recibe 2 números enteros. El primero menor que el segundo.
    Salida: Imprime la cantidad de semiprimos, cada número semiprimo en el intervalo y los primos que lo conforman.
    """
    try:
        if num1>=2 and num2>=2 and num1<num2:
            diccionario={}
            cantidad=0
            for i in range(num1,num2+1):
                x=factores_primos(i)
                if x.count("x")==1:
                    diccionario[i]=x
                    cantidad+=1
            if cantidad>0:
                print("Semiprimos:\t","Primos que lo conforman:")
                for llave, valor in diccionario.items():
                    print(llave,"\t","\t",valor)
                return "Cantidad total de primos: "+str(cantidad)
            return "No hay semiprimos en este rango."
        return "Los números deben ser mayores que 2. El primero menor que el segundo."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 7
def matriz_aux_7(matriz,diagonal):
    if matriz:
        i=0
        while i<len(matriz):
            if len(matriz[i])!=len(matriz):
                return "Error: No es una matriz cuadrada."
            j=0
            while j<len(matriz[i]):
                if str(matriz[i][j]).isdigit()==False:
                    return "Existen elementos no válidos."
                else:
                    j+=1
            i+=1
        return suma_diagonal(matriz,diagonal)
    else:
        return "No es una matriz."
def suma_diagonal(matriz,diagonal):
    """
    Funcion: Sumar los números de una diagonal de una matriz dada.
    Entrada: Una matriz mxn donde ambos numeros son positivos y un número entero de diagonal.
    Salida: Retorna la suma de los elementos que estan en el número de diagonal dado.
    """
    try:
        lista=[]
        suma=0
        if diagonal>=0:
            x=0; j=diagonal
            while x<len(matriz) and j<len(matriz[x]):
                lista.append(matriz[x][j])
                suma+=matriz[x][j]
                x+=1; j+=1
            if lista==[]:
                return "Error. No existe la diagonal."
            return suma
        else:
            x=-(len(matriz)); i=-(len(matriz))-(diagonal)
            while i<0 and x<0:
                suma+=matriz[i][x]
                lista.append(matriz[i][x])
                x+=1; i+=1
            if lista==[]:
                return "Error.No existe la diagonal."
            return suma
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 8
def primos_pal_aux(num1,num2):
    """
    Funcionamiento: Validar los datos convertir el valor de binario a decimal.
    Entradas: Número binario(int).
    Salidas: valor decimal de la entrada binaria (int).
    """
    num1=str(num1); num2=str(num2)
    if num1.isdigit() and num2.isdigit():
        if num1.count("1")+num1.count("0")==(len(num1)) and num2.count("1")+num2.count("0")==(len(num2)):
            return primos_pal(num1,num2)
        return "Error: Las entradas deben ser números binarios."
    return 'La cadena ingresada no debe contener letras.'

def primos_pal(num1,num2):
    """
    Funcion: Indicar los números primos y palindromos dentro de un rango. 
    Entrada: Un rango establecido por dos numeros binarios.
    Salida: Imprime los números del rango que sean palindromos y primos.
    """
    lista=[]
    inicio=int(convertir_bina_deci(str(num1)))
    fin=int(convertir_bina_deci(str(num2)))
    num1=int(num1); num2=int(num2)
    try:
        if num1>0 and num2>0 and num2>=num1:
            for i in range(inicio,fin+1):
                x=saber_palindromo(i)
                if x==True:
                    c=saber_primo(i)
                    if c==True:
                        lista.append(i)
            if lista!=[]:
                for numero in lista:
                    print(numero,"es primo y palindromo.")
                return ""
            return "No hay números cuya representación decimal sea un primo y palíndromo a la vez."
        return "Ambos numeros deben ser positivos y el primero debe ser menor al segundo."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 9
def factorial(numero):
    """
    Funcion: Realiza el factorial de un número.
    Entrada: Número entero.
    Salida: El factorial del número ingresado.
    """
    
    try:
        factorial=1
        i=1
        while i in range(1,numero+1):
            factorial*=i
            i+=1
        return factorial
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 10
def  triangulo_de_pascal(fila):
    """
    Funcion: Realiza el triangulo de Pascal a hasta el número de una fila indicada.
    Entrada: Número entero n mayor o igual que 1.
    Salida: Retorna el triángulo de Pascal hasta la fila n.
    """
    try:
        while fila>=1:
            triangulo=[]
            for n in range(1,fila+1):
                elementos=[]
                k=1
                while k<=n:
                    numero=factorial(n-1)//(factorial(k-1)*factorial(((n-1)-(k-1))))
                    elementos.append(numero)
                    k+=1
                triangulo.append(tuple(elementos))
            return triangulo
        return "El número ingresado debe ser mayor o igual que 1."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 11
def triangulo_de_pascal_2(numero):
    """
    Funcion: Realiza el triangulo de Pascal a hasta el número de una fila indicada. Otra forma de obtener este triangulo.
    Entrada: Número entero n mayor o igual que 1.
    Salida: Retorna el triángulo de Pascal hasta la fila n.
    """
    if numero==1:
        return [(1,)]
    try:
        while numero>=1:
            principal=[(1,),(1,1)]
            n=1
            while n<numero-1:
                fila_anterior=[]
                fila_anterior=principal[n]
                i=0; j=1
                fila=[]
                fila.append(1)
                while j<len(fila_anterior):
                    fila.append(fila_anterior[i]+fila_anterior[j])
                    i+=1; j+=1
                fila.append(1)
                principal.append(tuple(fila))
                n+=1
            return principal
        return "El número ingresado debe ser mayor o igual que 1."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 12
def  cuenta_palabras(tupla1,tupla2):
    """
    Funcion: Cuenta la cantidad de palabras a buscar en una frase.
    Entrada: Recibe dos tuplas cuyo contenido es tipo string.
    Salida: Retorna un diccionario que indica la cantidad de palabras encontradas en una frase.
    """
    try:
        diccionario={}
        tuplado=[]
        i=0
        while i<len(tupla2):
            tuplado+=tupla2[i].split()
            i+=1
        for elemento in tupla1:
            diccionario[elemento]=tuplado.count(elemento)
        return diccionario
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 13
def rombo(lineas):
    """
    Funcion: Imprime un rombo del tamaño establecido anteriormente.
    Entrada: Número entero mayor o igual que 2.
    Salida: Imprime un rombo del tamaño establecido anteriormente.
    """
    if lineas<2:
        return "El numero ingresado debe ser mayor o igual que 2."
    try:
        while lineas>=2:
            if lineas%2!=0:
                i=1; n=1
                while i<lineas:
                    a="*"*n
                    print(a.center(lineas*2," "))
                    i+=1; n+=2
                    if i==lineas:
                        n=(lineas*2)-1
                        i=lineas
                        while i>0:
                            a="*"*n
                            print(a.center(lineas*2," "))
                            i-=1; n-=2
                        return ""
            return "El número debe ser impar para realizar un rombo perfecto."
        return "El número ingresado debe ser mayor o igual que 2."
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."
#-------------------------------------- 14
def  factores_primos(numero):
    """
    Funcion: Factorizar un numero entero.
    Entrada: Numero entero a factorizar.
    Salida: Devuelve la factorizacion.
    """
    if numero<2:
        return "El numero ingresado debe ser mayor o igual que 2."
    try:
        factor=""
        while numero>=2:
            i=2
            while i in range(2,numero+1):
                if numero%i==0:
                    factor+=str(i)+"x"
                    numero//=i
                    i=0
                i+=1
        return factor.rstrip("x")
    except:
        return "Ha ocurrido un error durante la ejecucion del ejercicio."
#-------------------------------------- 15
def matriz_aux_15(matriz):
    if matriz:
        i=0
        while i<len(matriz):
            if len(matriz[i])!=len(matriz):
                return "Error: No es una matriz cuadrada."
            j=0
            while j<len(matriz[i]):
                if str(matriz[i][j]).isdigit()==False:
                    return "Existen elementos no válidos."
                else:
                    j+=1
            i+=1
        return es_identidad(matriz)
    else:
        return "No es una matriz."
def  es_identidad(matriz):
    """
    Funcion: Determina si una matriz es identidad o no.
    Entrada: Matriz de números.
    Salida: Booleano True o False.
    """
    try:
            i=0
            while i<len(matriz):
                j=0
                while j<len(matriz[i]):
                    if i==j:
                        if matriz[i][j]!=1:
                            return False
                    elif matriz[i][j]!=0:
                        return False
                    j+=1
                i+=1
            return True
    except:
        return "Ha ocurrido un error durante la ejecución del ejercicio."

#programa
print("1".center(26,"-"))
print(numero_abundante(24))
print("\n\n2".center(26,"-"))
print(encripta_aux("Hoy es martes"))
print("3".center(26,"-"))
print(pares_amigables_aux([100, 1184, 220, 15, 18, 1, 1210, 284, 25]))
print("4".center(26,"-"))
print(fibonacci(8))
print("5".center(26,"-"))
print(serie(98, 101,1))
print("6".center(26,"-"))
print(semiprimos(14,24))
print("7".center(26,"-"))
print(matriz_aux_7([[1,2,3],[4,5,6],[7,8,9]],-1))
print("8".center(26,"-"))
print(primos_pal_aux(101101001, 1011101110))
print("9".center(26,"-"))
print(factorial(5))
print("10".center(26,"-"))
print(triangulo_de_pascal(4))
print("11".center(26,"-"))
print(triangulo_de_pascal_2(4))
print("12".center(26,"-"))
print(cuenta_palabras(("calor", "ayer", "el", "mañana"),  ("ayer hizo bastante calor", "en el laboratorio hace calor")))
print("13".center(26,"-"))
print(rombo(5))
print("14".center(26,"-"))
print(factores_primos(33))
print("15".center(26,"-"))
print(matriz_aux_15([[1, 0, ],[0, 1, ]]))
