# Cadena

cadena = input("Introdueix una cadena de caràcters: ")

pos = int(input("Introdueix la posició a canviar: "))

while pos >= 0 and pos < len(cadena):
    caracter = input("Introdueix el caràcter nou: ")
    cadena = cadena[0:pos] + caracter + cadena[pos+1:]
    pos = int(input("Introdueix la posició a canviar: "))
print(cadena)

