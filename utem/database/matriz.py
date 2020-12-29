def matrizCorrecta(M):
    filas = len(M)
    columnas = len(M[0])
    correcto = True
    i = 1
    while i < filas and correcto:
        correcto = (len(M[i]) == columnas)
        i += 1
        return correcto

M = [[1,2,3], [2,4]]
matrizCorrecta(M)
 
