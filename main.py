import bola
import random
import balanza

#Igorren aldaketa 
bolas = [bola.Bola(1) for _ in range(8)]
posicion_aleatoria = random.randint(0,9)
bolas.insert(posicion_aleatoria, bola.Bola(1.1))  # Bola más pesada

balanza = balanza.Balanza()
balanzaPeso = balanza.pesar(bolas[:3], bolas[3:6])


if (balanzaPeso):
    if (balanzaPeso) == 1:
        balanzaPeso = balanza.pesar(bolas[0:1], bolas[1:2])
        if (balanzaPeso) == 1:
            print(balanza.emaitza(bolas[0]))
        elif (balanzaPeso) == -1:
            print(balanza.emaitza(bolas[1]))
        else:
            print(balanza.emaitza(bolas[2]))
    elif (balanzaPeso) == -1:
        balanzaPeso = balanza.pesar(bolas[3:4], bolas[4:5])
        if (balanzaPeso) == 1:
            print(balanza.emaitza(bolas[3]))
        elif (balanzaPeso) == -1:
            print(balanza.emaitza(bolas[4]))
        else:
            print(balanza.emaitza(bolas[5]))
else:
    balanzaPeso = balanza.pesar(bolas[6:7], bolas[7:8])
    if (balanzaPeso) == 1:
        print(balanza.emaitza(bolas[6]))
    elif (balanzaPeso) == -1:
        print(balanza.emaitza(bolas[7]))
    else:
        print(balanza.emaitza(bolas[8]))
#print(balanza.pesar(bolas[:4], bolas[4:8]))  # Compara las primeras 4 bolas con las últimas 4

#print(balanza.emaitza(bolas[4]))  # Muestra el resultado de la comparación