
def calcular_producto_dos_vectores(A, u, v):
    
    #DESCRIPCION DE LA FUNCION:
    #esta funcion calcula el producto entre dos vectores determinado por la matriz A,
    #solo se generan calculos si la matriz A es positiva definida
    
    #esta funcion recibe como entrada:
    #A matriz generada por matrix(QQ, 2, [1,0,0,1]);
    #u vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    #v vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    
    #esta funcion retorna como salida:
    #None en caso en el cual la matriz A no sea positiva definida
    #un racional resultado del producto de dos vectores determinado por la matriz A
    
    if(A.is_positive_definite()):
        print("*** La matriz es positiva definida ***");
        if type(u) == sage.modules.vector_rational_dense.Vector_rational_dense:
            ut = matrix(u);
        else:
            ut = u.transpose();
            
        if type(v) == sage.modules.vector_rational_dense.Vector_rational_dense:
            vf = matrix(v).transpose();
        else:
            vf = v;

        utAv = ut*A*vf;
        print("*** El resultado del producto es: ***");
        print(utAv);
        return(utAv)
    else:
        print("*** La matriz NO es positiva definida ***");
        return None;
        
    

def coeficiente_fourier(A, u, v):
    
    #DESCRIPCION DE LA FUNCION:
    #esta funcion calcula el coeficiente de fourier(v a lo largo de u)
    
    #esta funcion recibe como entrada:
    #A matriz generada por matrix(QQ, 2, [1,0,0,1]);
    #u vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    #v vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    
    c1 = calcular_producto_dos_vectores(A, u, v);
    c2 = calcular_producto_dos_vectores(A, u, u);
    c = c1/c2;
    return(c)


def proyeccion_ortogonal_u_sobre_v(A, u, v):
    
    #DESCRIPCION DE LA FUNCION:
    #esta funcion calcula la proyeccion ortogonal entre dos vectores(v a lo largo de u) determinado por la matriz A,
    #solo se generan calculos si la matriz A es positiva definida
    
    #esta funcion recibe como entrada:
    #A matriz generada por matrix(QQ, 2, [1,0,0,1]);
    #u vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    #v vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    
    #esta funcion retorna como salida:
    #None en caso en el cual la matriz A no sea positiva definida
    #un racional c resultado de calcular el coeficiente de fourier de dos vectores(v a lo largo de u) determinado por la matriz A
    #un vector cvt resultado de calcular el coeficiente de fourier de dos vectores(v a lo largo de u) determinado por la matriz A por el vector u
    
    if(A.is_positive_definite()):
        print("*** La matriz es positiva definida ***");
        if type(u) == sage.modules.vector_rational_dense.Vector_rational_dense:
            ut = matrix(u).transpose();
        else:
            ut = u;

        if type(v) == sage.modules.vector_rational_dense.Vector_rational_dense:
            vf = matrix(v).transpose();
        else:
            vf = v;

        c = coeficiente_fourier(A, ut, vf);

        print("*** EL coeficiente de fourier es: ***");
        print(c);
        cv = c*ut.transpose();
        cvt = cv.transpose();

        print("*** La proyeccion ortogonal de u sobre v es: ***");
        print(cvt);
        return(c, cvt)
    else:
        print("*** La matriz NO es positiva definida ***");
        return None;

    
def calcular_coeficiente_fourier_lista(A, B, v):
    
    #DESCRIPCION DE LA FUNCION:
    #esta funcion calcula el coeficiente de fourier para una lista de vectores ortogonales entre si por la matriz A,
    #solo se generan calculos si la matriz A es positiva definida
    
    #esta funcion recibe como entrada:
    #A matriz generada por matrix(QQ, 2, [1,0,0,1]);
    #B lista de vectores generados por:
    #u = matrix(QQ, 2, [4,2]), v = matrix(QQ, 2, [1,3]), z = matrix(QQ, 2, [1,1]), es decir [u,v,z];
    #o v1 = vector(QQ, [4,2]), v2 = vector(QQ, [1,3]), v3 = vector(QQ, [1,1]), es decir [v1,v2,v3];
    #o [(4,2),(1,3),(1,1)];
    #v vector generada por matrix(QQ, 2, [1,1]); o vector(QQ, [1,1]);
    
    #esta funcion retorna como salida:
    #None en caso en el cual la matriz A no sea positiva definida
    #una lista de racionales c[i] resultado de calcular el coeficiente de fourier de dos vectores(v a lo largo de u[i]) determinado por la matriz A
    #u[i] es cada vector en la lista B
    
    if(A.is_positive_definite()):
        print("*** La matriz es positiva definida ***");
        coeficientes_fourier = [];
        l= len(B);
        print("[");
        for i in range(l):
            
            if type(B[i]) == tuple:
                u = matrix(B[i]).transpose();
            else:
                u = B[i];
            cf = coeficiente_fourier(A, u, v);
            coeficientes_fourier.append(cf);
            print(f'*** EL coeficiente de fourier [ { i + 1 } ] es: { cf } ***');
        print("]");
        return coeficientes_fourier
    else:
        print("*** La matriz NO es positiva definida ***");
        return None
    
    
#Definimos A
A = matrix(QQ, 2, [3,2,2,4]);

#Definimos u, v y z
u = matrix(QQ, 2, [4,2]);
v = matrix(QQ, 2, [1,3]);
z = matrix(QQ, 2, [1,1]);

#Otra forma para definir vectores
v1 = vector(QQ, [4,2]);
v2 = vector(QQ, [1,3]);
v3 = vector(QQ, [1,1]);

#coleccion de vectores
B1 = [v1,v2,v3];
B2 = [(4,2),(1,3),(1,1)];
B3 = [u,v,z];

#calcular_producto_dos_vectores(A, u, v);

#proyeccion_ortogonal_u_sobre_v(A, v1, v2);

#calcular_coeficiente_fourier_lista(A, B3, v);
