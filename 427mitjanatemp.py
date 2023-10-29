# Mitjana temperatura dotze mesos

NUM_MESOS = 12

llista_temp = []
#ENTRADA DE DADES
for i in range(NUM_MESOS):
    temp = int(input("Introdueix la temperatura del mes "+str(i+1)+": "))
    llista_temp.append(temp)
    #llista_temp.append(int(input("Introdueix temperatura del mes "+str(i+1)+" : ")))

#CALCUL MAXIM I MINIM
maxim = llista_temp[0]
pos_max = 0 #la temp comença en 0
minim = llista_temp[0]
pos_min = 0 #la temp comença en 0
suma = llista_temp[0]

for i in range(1,NUM_MESOS):   #S'agafa la 1 perquè ja comença llegint la posició 0
    suma+= llista_temp[i]
    if llista_temp[i] > maxim:
        maxim = llista_temp[i]
        pos_max = i
    elif llista_temp[i] < minim:
        minim = llista_temp[i]
        pos_min = i
mitjana = suma / NUM_MESOS

print("Mes amb temperatura màxima:",pos_max+1)
print("Mes amb temperatura mínima",pos_min+1)
print("Temperatura mitjana:",mitjana)

for i in range(NUM_MESOS):
    if llista_temp[i] > mitjana:
        print("El mes",i+1,"ha tingut temperatura superior a la mitjana anual.")
    elif llista_temp[i] < mitjana:
        print("El mes",i+1,"ha tingut temperatura inferior a la mitjana anual.")        
    else:
        print("El mes",i+1,"ha tingut temperatura igual a la mitjana anual.")