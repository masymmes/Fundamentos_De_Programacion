from random import randint
num1 = int(input("Ingrese límite inferior: "))
num2 = int(input("Ingrese límite superior: "))
numero = randint(num1, num2)
if numero % 2 != 0:
    if numero + 1 <= num2:
        numero = numero + 1
    else:
        numero = numero - 1
intento1 = int(input("Intente adivinar: "))
if intento1 == numero:
    print("Felicitaciones, adivinó en el primer intento.")
else:
    if intento1 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    intento2 = int(input("Intente de nuevo: "))
    if intento2 == numero:
        print("Felicitaciones, adivinó en su segundo intento.")
    else:
        if intento2 < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        distancia1 = numero - intento1
        if distancia1 < 0:
            distancia1 = distancia1 * -1
        distancia2 = numero - intento2
        if distancia2 < 0:
            distancia2 = distancia2 * -1
        print("Te daré una pista:")
        if distancia1 <= distancia2:
            print("El número que buscas está más cerca de", intento1, "que de", intento2)
        else:
            print("El número que buscas está más cerca de", intento2, "que de", intento1)
        intento3 = int(input("Intente la última vez: "))
        if intento3 == numero:
            print("Felicitaciones, pudiste adivinar.")
        else:
            print("Perdiste.")
            print("El número era:", numero)
