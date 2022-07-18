#Proyecto final Solyblue
print("  ", sep="-")
print("  ", sep="-")
print(" ︵‿︵ Bienvenido al closet virtual de ゜。° ☀ Solyblue 🕊️"    )         
print('''
   _________________________________________________________________
  | Productos:              Ref:                 Valor:             |
  | BODY BASIC              A01                  $35.000            |
  | FALDA SHORT             A02                  $55.000            |
  | VESTIDO                 A03                  $60.000            |
  | SHORT                   A04                  $56.000            |
  | BLUSA PRINT             A05                  $45.000            |
  | CAMISA BASIC            A06                  $38.000            |
  |_________________________________________________________________|
''')

di=int(input("A continuación, escribe tu número de documento de identidad: "))
nombre=input("Ingresa tu nombre completo: ")
hb=input("Ingresa tu fecha de nacimiento para próximos beneficios (DD/MM/AAAA): ")



ref=input("Ingresa las referencias que quieres llevar, cuando finalices escribe 0: ")
total=0


while ref!="0":
    if (ref=="A01"):
        print("Body Basic por $35.000")
        total = total + 35000
    elif (ref=="A02"):
        print("falda por $55.000")
        total = total + 55000
    elif (ref=="A03"):
        print("vestido por $60.000")
        total = total + 60000
    elif (ref=="A04"):
        print("short por $56.000")
        total = total + 56000
    elif (ref=="A05"):
        print("blusa por $45.000")
        total = total + 45000
    elif (ref=="A06"):
        print("camisa por $38.000")
        total = total + 38000
    else:
        ref=input("La referencia no es valida, por favor verifica el closet virtual e intenta nuevamente: ")
        
    ref=input("Ingresa las referencias que quieres llevar, cuando finalices escribe 0: ")

print("tu costo sera de: $"+ str (total))