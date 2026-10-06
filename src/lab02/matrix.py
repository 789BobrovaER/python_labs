def check(mat):
    ln=len(mat[0])
    if not all(len(mat[x])==ln for x in range(len(mat))):
            raise ValueError('Матрица "рваная"')
    return True

def transpose(mat: list[list[float | int]]) -> list[list]:
    '''Поменять строки и столбцы местами. Пустая матрица [] → [].
Если матрица «рваная» (строки разной длины) — ValueError.'''
    if len(mat)==0:return[] 
    check(mat)

    ln=len(mat[0])
    tr_mat=[]
    for x in range(ln): tr_mat.append([])

    for l in range(ln):
        for m in mat:
            tr_mat[l].append(m[l])
    return tr_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
     '''Сумма по каждой строке.'''
     if mat==[]:return []
     check(mat)
     sum_mat=[sum(m) for m in mat]
     return(sum_mat)



def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''Сумма по каждому столбцу. '''
    if mat==[]:return []
    check(mat)
    col=[]
    for l in range(len(mat[0])):
         s=0
         for m in mat:s+=m[l]
         col.append(s)
    return col


              


     
     
    