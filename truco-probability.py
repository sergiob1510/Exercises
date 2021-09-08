import random
from collections import defaultdict
#En un mazo de naipes españoles, cada carta tiene un palo y un valor. 
#El mazo tiene 40 naipes. Los palos son oro, copa, espada y basto y
#los valores van del 1 al 7 y de del 10 al 12. Usaremos una comprensión
#doble de listas para generar los naipes (todas las combinaciones posibles
#de valores y palos)

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

#En este caso tenemos que usar elecciones múltiples sin reposición. Para eso usamos
#la función sample del módulo random: random.sample(naipes,k=3)

#Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 31, 32 o 33
#puntos de envido en una mano. ¿Son iguales estas tres probabilidades? ¿Por qué?

#Observación: como corresponde, en esta materia jugamos al truco sin flor. Si no conocés
#las reglas del Truco y no te dan ganas de aprenderlo ahora, simplemente salteá este ejercicio.

def probabileitor(manos_simuladas):
    
    tantos_31 = 0
    tantos_32 = 0
    tantos_33 = 0

    for i in range(manos_simuladas):
        #Saco 3 cartas al azar
        mano = random.sample(naipes,k=3)
        #Ordeno la mano por palo y cartas, quedando {palo: [cartas]}
        mano_iterable = defaultdict(list)
        for carta, palo in mano:
            mano_iterable[palo].append(carta)
        for palo, cartas in mano_iterable.items():
            #Ordeno de menor a mayor las cartas del mismo palo, reemplazando las figuras por 0
            cartas = sorted(([x if x < 10 else 0 for x in cartas]))
            tanto = [20 + sum(cartas[-2:]) if len(cartas) > 1 else 0]
            if tanto[0] == 31:
                tantos_31 = tantos_31 + 1
            if tanto[0] == 32:
                tantos_32 = tantos_32 + 1
            if tanto[0] == 33:
                tantos_33 = tantos_33 + 1

    probabilidad_de_sacar_31 = tantos_31/manos_simuladas
    probabilidad_de_sacar_32 = tantos_32/manos_simuladas
    probabilidad_de_sacar_33 = tantos_33/manos_simuladas
    probabilidad_de_cualquiera = (tantos_31 + tantos_32 + tantos_33)/manos_simuladas
    
    return(f'''    Manos simuladas: {manos_simuladas}\n
    Veces que sacaste 31: {tantos_31}\n
    Las probabilidades de sacar 31 son: {probabilidad_de_sacar_31} \n
    Veces que sacaste 32: {tantos_32} \n
    Las probabilidades de sacar 32 son: {probabilidad_de_sacar_32} \n
    Veces que sacaste 33: {tantos_33} \n
    Las probabilidades de sacar 33 son: {probabilidad_de_sacar_33} \n
    Las probabilidades de sacar 31, 32 o 33 son: {probabilidad_de_cualquiera}''')




