# 1 - Variáveis e Operações com Números:
# Crie duas variáveis, a e b, atribua valores e realize as seguintes operações:

a = 10
b = 20

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
restoDaDivisao = a % b
potenciacao = a ** b

pi= 3.14
raio = 8

area = pi*raio**2

print(soma, subtracao, multiplicacao, divisao, divisao_inteira, restoDaDivisao, potenciacao)
print(area)


# 2 - Manipulação de Strings:
# Declare duas strings, nome e sobrenome, e concatene-as para formar o nome completo. Imprima o resultado.

# Crie uma string que represente uma frase e use métodos de string para:

# Converter todas as letras para maiúsculas.
# Converter todas as letras para minúsculas.
# Substituir uma palavra por outra na frase.

nome = "Joao"
sobrenome = "Lima"
concactenar = nome +" "+ sobrenome
print(concactenar)

# 3 - Utilização de Listas e Tuplas:
# Crie uma lista com três cores diferentes. Adicione mais duas cores a essa lista e imprima-a.

# Declare uma tupla com as coordenadas (latitude, longitude) de um local e imprima cada valor separadamente.

cores = ["Verde", "Amarelo", "Azul"]
cores.append("Branco")
print(cores)

# 4 - Uso de Operadores Lógicos em Estruturas Condicionais:
# Crie duas variáveis booleanas, tem_sol e tem_chuva, representando condições climáticas. Utilize essas variáveis em uma estrutura condicional para decidir se é um dia agradável ou não.
tem_sol = True
tem_chuva = False

if tem_sol == False and tem_chuva == False:
    print("Clima Agradavel")
else: 
    print("Clima Desagradavel")

# Solicite ao usuário dois números e use operadores lógicos para verificar se ambos são números pares. Imprima o resultado.
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))

verifNum1=num1 % 2
verifNum2 = num2 % 2

if verifNum1 == 0:
    condNum1 = "Par"
else: condNum1 = "impar"
if verifNum2 == 0:
    condNum2 = "Par"
else: condNum2 = "impar"

print("1° numero é "+condNum1+"\n2° numero é "+condNum2)

# Crie uma lista de números e use uma estrutura de repetição para percorrer a lista. Utilize operadores lógicos para verificar e imprimir quais números são múltiplos de 3 e ímpares.
numeros = [2,4,9,6,12,346,546]

for listNumero in numeros:
    if listNumero %3 ==0 and listNumero %2 == 1: 
     print(listNumero)
    
# Peça ao usuário para digitar a sua idade e verifique se ela está dentro do intervalo de 18 a 65 anos. Imprima uma mensagem correspondente.
idade = int(input("Digite sua idade "))

if idade <= 65 and idade>=18:
  print("Idade Apropriada")
else:
   print("Idade Inapropriada")

# 1 - Variáveis e Operações com Números:
# Crie três variáveis, a, b e c, representando os coeficientes de uma equação quadrática (ax^2 + bx + c). Calcule as raízes da equação usando a fórmula de Bhaskara.

a = int(input("Valor do A "))
b = int(input("Valor do B "))
c = int(input("Valor do C "))

delta = (b ** 2) - 4 * a * c
print(delta)
if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
# Implemente um programa que converta um valor em dólares para outras moedas (por exemplo, euros e libras). Solicite ao usuário o valor em dólares e a taxa de conversão.
valorDolar = int(input("Digite seu valor em dolar "))
valorEuro = valorDolar * 0.93
valorLibra = valorDolar * 0.79
print(f"Seu Valor em Euro "+str(valorEuro)+"\n Seu Valor em Libras"+str(valorLibra))








    
  