# Creation calculatrice 
nombre1 = int(input("Nombre 1 "))
operation = input()
nombre2 = int(input("Nombre 2 "))
if operation == '+':
    resultat = nombre1 + nombre2   
    print(resultat)
elif operation == '-':
    resultat = nombre1 - nombre2
    print(resultat)
elif operation == '*':
    resultat = nombre1 * nombre2
    print(resultat)
elif operation == '/':
    resultat = nombre1 / nombre2
    print(resultat)
else: 
    print("Opérateur non reconnue")

