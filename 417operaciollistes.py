# Menú d'operaciones sobre llistes


llista_valors = []

n_elements = int(input("Introdueix els la quantitat d'elements: "))

for i in range (0,n_elements):
    valors = int(input("Introdueix un valor: "))
    llista_valors.append(valors)

print("   QUÈ VOLS FER?\n  ")
print("1-Afegir element al final de la llista")
print("2-Afegir element en una posició de la llista")
print("3-Eliminar el darrer element de la llista")
print("4-Eliminar l'element d'una posició de la llista")
print("5-Eliminar la primera aparició d'un valor de la llista")
print("6-Sortir")
opcio = int(input("Prem la opció que desitjis: "))



while opcio == 1:
    afegir = int(input("Afegeix l'element que vulguis: "))
    llista_valors.append(afegir)
    print("La llista és:",llista_valors)
    print("   QUÈ VOLS FER?\n  ")
    print("1-Afegir element al final de la llista")
    print("2-Afegir element en una posició de la llista")
    print("3-Eliminar el darrer element de la llista")
    print("4-Eliminar l'element d'una posició de la llista")
    print("5-Eliminar la primera aparició d'un valor de la llista")
    print("6-Sortir")
    opcio = int(input("Prem la opció que desitjis: "))

while opcio == 2:
    opcio2_1 = int(input("Introdueix l'element que vulguis afegir: "))
    opcio2_2 = int(input("Introdueix la posició on vols afegir l'element: "))
    if opcio2_2 > len(llista_valors):
        print("Error: Llista buida")
        print("La llista és:",llista_valors)
        print("   QUÈ VOLS FER?\n  ")
        print("1-Afegir element al final de la llista")
        print("2-Afegir element en una posició de la llista")
        print("3-Eliminar el darrer element de la llista")
        print("4-Eliminar l'element d'una posició de la llista")
        print("5-Eliminar la primera aparició d'un valor de la llista")
        print("6-Sortir")
        opcio = int(input("Prem la opció que desitjis: "))
    else:
        llista_valors.insert(opcio2_2,opcio2_1)
        print("La llista és:",llista_valors)
        print("   QUÈ VOLS FER?\n  ")
        print("1-Afegir element al final de la llista")
        print("2-Afegir element en una posició de la llista")
        print("3-Eliminar el darrer element de la llista")
        print("4-Eliminar l'element d'una posició de la llista")
        print("5-Eliminar la primera aparició d'un valor de la llista")
        print("6-Sortir")
        opcio = int(input("Prem la opció que desitjis: "))

while opcio == 3:
    llista_valors.pop()
    print("La llista és:",llista_valors)
    print("   QUÈ VOLS FER?\n  ")
    print("1-Afegir element al final de la llista")
    print("2-Afegir element en una posició de la llista")
    print("3-Eliminar el darrer element de la llista")
    print("4-Eliminar l'element d'una posició de la llista")
    print("5-Eliminar la primera aparició d'un valor de la llista")
    print("6-Sortir")
    opcio = int(input("Prem la opció que desitjis: "))

while opcio == 4:
    pos_elim = int(input("Introdueix la posició que vols eliminar: "))
    if pos_elim > len(llista_valors):
        print("Error: Llista buida")
        print("   QUÈ VOLS FER?\n  ")
        print("1-Afegir element al final de la llista")
        print("2-Afegir element en una posició de la llista")
        print("3-Eliminar el darrer element de la llista")
        print("4-Eliminar l'element d'una posició de la llista")
        print("5-Eliminar la primera aparició d'un valor de la llista")
        print("6-Sortir")
        opcio = int(input("Prem la opció que desitjis: "))
    else:
        del(llista_valors[pos_elim])
        print("La llista és:",llista_valors)
        print("   QUÈ VOLS FER?\n  ")
        print("1-Afegir element al final de la llista")
        print("2-Afegir element en una posició de la llista")
        print("3-Eliminar el darrer element de la llista")
        print("4-Eliminar l'element d'una posició de la llista")
        print("5-Eliminar la primera aparició d'un valor de la llista")
        print("6-Sortir")
        opcio = int(input("Prem la opció que desitjis: "))

while opcio == 5:
    elim_elem = int(input("Introdueix l'element que vulguis eliminar: "))
    llista_valors.remove(elim_elem)
    print("La llista és:",llista_valors)
    print("   QUÈ VOLS FER?\n  ")
    print("1-Afegir element al final de la llista")
    print("2-Afegir element en una posició de la llista")
    print("3-Eliminar el darrer element de la llista")
    print("4-Eliminar l'element d'una posició de la llista")
    print("5-Eliminar la primera aparició d'un valor de la llista")
    print("6-Sortir")
    opcio = int(input("Prem la opció que desitjis: "))

if opcio == 6:
    print()
    exit()

print(llista_valors)
    


        

