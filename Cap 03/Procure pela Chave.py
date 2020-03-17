# Procure pela Chave
# Pag 59

def procure_pela_chave(caixa_principal):
    pilha = main.box.crie_uma_pilha_para_buscar()
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print "Achei a chave!!"