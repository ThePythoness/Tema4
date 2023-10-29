# Comparació de llistes

NUM_ELEMENTS = 6

llista_1 = []
print("LLISTA 1")
for i in range(NUM_ELEMENTS):
    llista_1.append(int(input("Introdueix valor a l'índex "+str(i)+" : ")))

llista_2 = []
print("LLISTA 2")
for i in range(NUM_ELEMENTS):
    llista_2.append(int(input("Introdueix valor a l'índex "+str(i)+" : ")))

i = 0
trobat = False
while i < NUM_ELEMENTS and not trobat:
    if llista_1[i] != llista_2[i]:       #Trobat diferència 
        trobat = True
    else:
        i += 1

if trobat == False:   # Hem arribat al final de les llistes sense diferències
    print("IGUALS")
else:
    print("DIFERENTS")
