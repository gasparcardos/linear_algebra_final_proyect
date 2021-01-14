#ENTRADAS:
#Se definen las matrices y las variables que se usarán durante el programa
#A es una matriz de m,n elementos y b una matriz de m,1 elementos
#E representa a la matriz resultante de unir A y b
#C representa la matriz escalonada reducida de E
#tipo almacena en un string el tipo de sistema que tenemos, inconsistente, indeterminado o determinado, inconsistente es una bandera que cambia su valor a True cuando nos  encontramos con ese tipo de sistema
    
def variables(A, b):
    m,n=A.dimensions()
    x,y=b.dimensions()
    if(m == x and y == 1):
        E=A.augment(b,subdivide=true)
        C=E.rref()
        
        tipo=""
        inconsistente = False
        determinado = False
        indeterminado = False
        
        for i in range(m) :
            contador=0
            for j in range(n):
                if(C[i][j]==0):
                    contador=contador+1
            if(contador==n and C[i][n]!=0):
                tipo="El sistema es Inconsistente"
                inconsistente = True
                break
        if(not inconsistente):
            rank = C.rank()
            if(rank == n):
                tipo="El sistema es Determinado"
                determinado = True
            else:
                tipo="El sistema es Indeterminado"
                indeterminado = True
              
        if(inconsistente):
            print(tipo)
            print("****** Escalonada reducida *****")
            print(C)
        else:
            columnas_libres =[]
            columnas_basicas = []
            excepcion=[]
            expresiones=[]

            for i in range(m):
                for j in range(n):
                    if C[i][j] != 0:
                        columnas_basicas.append(j)
                        for k in range(j+1, n):
                            if C[i][k] != 0 and k not in columnas_libres:
                                columnas_libres.append(k)
                            else:
                                if k not in excepcion:
                                    excepcion.append(k)
                        break
            for l in range(len(columnas_basicas)):
                if columnas_basicas[l] in excepcion:
                    excepcion.remove(columnas_basicas[l])



            for i in range(m):
                expAux = ""
                valAux = 0
                for j in range(n):
                    if C[i][j] != 0:
                        if j in columnas_basicas:
                            valAux = j + 1
                            expAux = f'X{valAux} = '
                            for k in range(j+1, n+1):

                                valAux = 0
                                if k in excepcion:
                                    valAux = k + 1
                                    expAux = expAux + f'-({ C[i][k] }X{ valAux })'
                                if k == n:
                                    expAux = expAux + f' + ({C[i][k]})'
                                    if expAux not in expresiones:
                                        expresiones.append(expAux)
                                        break
                                    break
                            break
        #SALIDAS:
        #La función imprime el tipo de sistema según sea el caso, indeterminado, inconsistente, o determinado
        #En caso de que no sea inconsistente imprime, además, las variables básicas, las variables libres, las soluciones del sistema y la matriz escalonada reducida.
            print(tipo)
            print("Variables basicas: ")
            for b in range(len(columnas_basicas)):
                strBAux = columnas_basicas[b] + 1
                print('X' + f'{strBAux}')
            if(determinado):
                print("No existen variables libres")
            else:
                if(indeterminado):
                    print("Variables libres: ")
                    for t in range(len(excepcion)):
                        strLAux = excepcion[t] + 1
                        print('X' + f'{strLAux}')

            print("***** Soluciones *****")
            for e in range(len(expresiones)):
                print(expresiones[e])
                
            print("****** Escalonada reducida *****")
            print(C)
    else:
        print("El sistema no es compatiblle")
#Para que el usuario defina la matriz y el vector 
A=random_matrix(QQ,3,5)
b=random_matrix(QQ,3,1)

variables(A, b)