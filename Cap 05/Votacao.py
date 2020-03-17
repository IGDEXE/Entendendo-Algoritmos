# Votacao usando hash
# Pag 101

voted = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print "Manda embora!"
    else:
        voted[nome] = True
        print "Deixa votar!"