def generate_subspace(vectors):
    matx = matrix(vectors)
    echelon_mat = matx.rref()
    rows, columns = echelon_mat.dimensions()
    zero_rows = []
    for row in range(0, rows):
        zero_counter = 0
        for column in range(0, columns):
            if echelon_mat[row][column] == 0:
                zero_counter = zero_counter +1
        if zero_counter == columns:
            zero_rows.append(row)
            
    echelon_mat = echelon_mat.delete_rows(zero_rows, check= True)
    print(echelon_mat)


            
    
def solve_equations(A, b):
    m,n=A.dimensions()
    x,y=b.dimensions()
    if(m == x and y == 1):
        C=generate_rowEchelon(A)

        
        columnas_libres =[]
        columnas_basicas = []
        excepcion=[]
        expresiones=[]
        print(C)
        for row in range(m):
            for column in range(n):
                if C[row][column] != 0:
                    columnas_basicas.append(column)
                    for right_value in range(column+1, n):
                        if C[row][right_value]!=0 and right_value not in columnas_libres:
                            columnas_libres.append(right_value)
                    break
                print(f'libres:{columnas_libres}')       

        print("***** Soluciones *****")
        for e in range(len(expresiones)):
            print(expresiones[e])

#Para que el usuario defina la matriz y el vector 
#A=matrix([[1,2,-1,3],[3,5,-4,7]])
#b=matrix([[0],[0]])
vectors = [(1, 2, 3, 4), (2,3, 1, 4), (2, 3,1, 4), (2, 3, 1 , 4)]
generate_subspace(vectors)
#variablesDefinition(A, b)



##Conjunto generador
