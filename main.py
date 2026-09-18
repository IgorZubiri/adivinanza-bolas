import bola
import random
import balanza

#Igorren aldaketa 
bolas = [bola.Bola(1) for _ in range(8)]
posicion_aleatoria = random.randint(0,9)
bolas.insert(posicion_aleatoria, bola.Bola(1.1))  # Bola más pesada

balanza = balanza.Balanza()



if (balanza.pesar(bolas[:3], bolas[3:6])):
    print("La bola se encuentra en los primeros dos múltiplos de tres")
else:
    print("Ultimo múltiplo de 3")
    if (balanza.pesar(bolas[7], bolas[8])):
        if (bolas[7].peso) != 1:
             print(balanza.emaitza(bolas[7]))
        elif (bolas[8].peso) != 1:
             print(balanza.emaitza(bolas[8]))
    else:
        print(balanza.emaitza(bolas[9]))


#print(balanza.pesar(bolas[:4], bolas[4:8]))  # Compara las primeras 4 bolas con las últimas 4

#print(balanza.emaitza(bolas[4]))  # Muestra el resultado de la comparación