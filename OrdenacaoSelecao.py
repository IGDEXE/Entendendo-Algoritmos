# Ordenar Selecao
# Pag 54

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr
print ordenacaoporSelecao([5,3,6,2,10])