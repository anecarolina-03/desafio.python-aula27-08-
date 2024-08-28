num1= float(input("Digite um número: "))
num2= float(input("Digite outro número: "))
num3= float(input("Digite mais um número: "))

def ler_numeros(num1, num2, num3):
    print('Os números são {} , {} e {}'.format(num1, num2, num3))

def calcular_soma(num1,num2,num3):
    calcular_soma= num1+num2+num3
    print('A soma é= {}' .format(calcular_soma))

def calcular_media(num1, num2, num3):
    media= (num1+num2+num3)/3
    print('A média é= {}'.format(media))

ler_numeros(num1, num2, num3)
calcular_soma(num1, num2, num3)
calcular_media(num1, num2, num3)

