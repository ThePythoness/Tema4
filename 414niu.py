# Niu estudiants

num_estudiants = int(input("Introdueix quants estudiants hi ha a classe: "))

llista_apr = []
llista_susp = []

for i in range (0,num_estudiants):
    niu = int(input("Introdueix el NIU de l'estudiant: "))
    nota = float(input("Introdueix la nota de l'estudiant: "))
    if nota >= 5:
        llista_apr.append(niu)
    else:
        llista_susp.append(niu)
        

print("Aprovats:",str(len(llista_apr)),llista_apr)
print("Suspesos:",str(len(llista_susp)),llista_susp)

