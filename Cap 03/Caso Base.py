# Caso Base
# Pag 60

def regressiva(i):
    print i
    if i <= 1:
        return
    else:
        regressiva(i - 1)