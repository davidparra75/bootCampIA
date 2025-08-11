# #determinar si un numero es positivo o negativo

# def positivoOnegativo(num):
#     if num > 0:
#         print("el numero es positivo")
#     else:
#         print("el numero es negativo")

# positivoOnegativo(-1)

# def ParImpar(num):
#     if num % 2 == 0:
#         print("el numero es par")
#     else:
#         print("el numero es impar")

# ParImpar(7)

# #determinar si un numero es divisible exactamente por 3 y por 5 al mismo tiempo

# def divisible(num):
#     if num % 5 == 0 and num % 3 == 0:
#         print("el numero es divisible por 5 y 3 al mismo tiempo")
#     else:
#         print("numero no divisible por 3 y 5")

# #determinar si un caracter dado es una vocal
# def esVocal(string):
#     if string == 'A' or string == 'E' or string == 'I' or string == 'O' or string == 'U'or string == 'a' or string == 'e'or string == 'i'or string == 'o'or string == 'u':
#         return True
#     else:
#         return False
    
# caracter = input("ingrese caracter: ")
# if esVocal(caracter):
#     print(True)
# else:
#     print(False)

# #leer una letra por teclado y determinar si es vocal, consonante, o numero

# def caracter(caracter):
#     if ord(caracter)>=48 and ord(caracter)<=57:
#         print("el caracter es un numero")
#     elif ord(caracter)>=65 and ord(caracter)<=90:
#         print("el caracter es una mayuscula")
#     elif ord(caracter)>=97 and ord(caracter)<=122:
#         print("el caracter es una minuscula")

# caracter('1')

# #leer 3 numeros mostraarlos y deducir si se introducen de forma creciente

# def creciente(numero1,numero2,numero3):
#     if numero1>numero2 or numero2>numero3:
#         print("no se ingresaron en forma creciente")
#     else:
#         print("se ingresaron de forma creciente")
# numero1 = input("ingrese numero 1: ")
# numero2 = input("ingrese numero 2: ")
# numero3 = input("ingrese numero 3: ")

# creciente(numero1,numero2,numero3)

# #leer numero de mes e indicar nombre del mes

# def nombreMes(numeroMes):
#     if numeroMes >= 1 and numeroMes<=12:
#         if numeroMes == 1:
#             print("ENERO")
#         elif numeroMes == 2:
#             print("FEBRERO")
#         elif numeroMes == 3:
#             print("MARZO")
#         elif numeroMes == 4:
#             print("ABRIL")
#         elif numeroMes == 5:
#             print("MAYO")
#         elif numeroMes == 6:
#             print("JUNIO")
#         elif numeroMes == 7:
#             print("JULIO")
#         elif numeroMes == 8:
#             print("AGOSTO")
#         elif numeroMes == 9:
#             print("SEPTIEMBRE")
#         elif numeroMes == 10:
#             print("OCTUBRE")
#         elif numeroMes == 11:
#             print("NOVIEMBRE")
#         elif numeroMes == 12:
#             print("DICIEMBRE")
#     else:
#         print(f"el mes numero {numeroMes} no existe")

# nombreMes(2)

# def operacion(numero1,numero2,operador):
#     if operador == '+':
#         return numero1 + numero2
#     elif operador == '-':
#         return numero1-numero2
#     elif operador == '*':
#         return numero1 * numero2
#     elif operador == '/':
#         if numero2 == 0:
#             print("Error, no se puede dividir por 0")
#         else:
#             return numero1 / numero2
#     elif operador != '+' or operador!='-' or operador!='*' or operador!='/':
#         print("operador no encontrado")

# operacion(1,2,'+')

#dado un numero de 3 digitos determinar si es capicua o no
def invertir(a):
    x = 0
    z = len(str(a))
    for i in range(z):
        b = a%10
        a=a//10
        x = x*10+b
    return x


def capicua(numero):
    while len(str(numero)) > 3:
        numero = int(input("ingrese un numero de 3 digitos: "))
    numero = invertir(numero)
    if numero == invertir(numero):
        print("el numero ES capicua")
    else:
        print("el numero NO ES capicua")

capicua(122)

#dados 3 numeros mostrarlos de menor a mayor

def mayorMenor():
    num1 = int(input("ingrese numero 1: "))
    num2 = int(input("ingrese numero 2: "))
    num3 = int(input("ingrese numero 3: "))
    if num1 < num2 and num1 < num3:
        resp =[num1]
        if num2 < num3:
            resp = [num1,num2,num3]
        else:
            resp = [num1,num3,num2]

    elif num2 < num1 and num2 < num3:
        resp = [num2]
        if num1 < num3:
            resp = [num2, num1, num3]
        else:
            resp = [num2,num3,num1]
    elif num3 < num1 and num3 < num2:
        resp = [num3]
        if num1 < num2:
            resp =[num3, num1, num2]
        else:
            resp =[num3, num2,num1]

