#-------------------------------------------------------------------------#
#Pregunta el nombre de una ciudad y muestra el monumento mas famoso de esa ciudad
# Ciudad		Monumento
#Delhi			Red Fort
#Paris			Torre Eifel
#Nueva York		Estatua de la Libertad
#Rio de Janeiro	Cristo Redentor
ent = input("ingresa la ciudad")
trabajo = {
    "paris":"torre eifel",
    "delhi":"red fort",
    "nueva york":"estatua de la libertad",
    "rio de janeiro":"cristo redentor"
}
    
if ent in trabajo:
    print(trabajo[ent])
else:
    print("no esta")
#-------------------------------------------------------------------------#
#Escriba un programa para verificar si una persona puede votar o no
ent = int(input("ingresa tu edad"))
if ent >= 18 and ent <= 120:
    print("puede votar")
elif ent > 120:
    print("ingresa una edad coherente")
else:
    print("no puede votar")
#-------------------------------------------------------------------------#
#Escriba un programa que identifique entre dos numeros cual es el menor
enable = True
lista = []
while(enable):
    num = int(input("pon un numero"))
    lista.append(num)
    respuesta = input("quieres poner un numero extra?(N/Y)")
    if respuesta == "N" or respuesta == "n":
        enable = False
        print("el numero es:", min(lista))
#-------------------------------------------------------------------------#
#Escribir un programa que identifique entre 4 personas cual es la de mnor edad
enable = True
lista = []
while(enable):
    num = int(input("edad"))
    num2 = int(input("edad"))
    num3 = int(input("edad"))
    num4 = int(input("edad"))
    lista.append(num)
    lista.append(num2)
    lista.append(num3)
    lista.append(num4)
    respuesta = input("quieres poner un nombre y edad extra?(N/Y)")
    if respuesta == "N" or respuesta == "n":
        enable = False
        print("la edad es:", min(lista))
#-------------------------------------------------------------------------#
#Escribir un programa que identifique si una letra es Mayusula o Minuscula de una palabra escrita por el usuario
minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
ent = input("ingresa la palabra")
letras = list(ent)
for letra in letras:
    if letra in minus:
        print("es una letra minuscula", letra)
    elif letra in mayus:
        print("es una mayuscula")
