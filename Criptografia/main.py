# Importações
import random
import math
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Pedir a mensagem que será encriptada 
with open('D:\\CriptografiaPython\\Criptografia\\msg.criptografar.txt', 'r') as arquivo:
    texto_base= arquivo.read()
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Vamos randomizar os valores de P e Q e verificar se eles são primos
def verificar_primos(number, y=5):
    # Faz a verificação para ver se não é 1, 2 ou 3 pois já são primos
    if number <= 1:
        return False
    if number <= 3:
        return True
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Testa se o valor é primo por meio do teste de Miller-Rabin
    r, d = 0, number - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for Miller in range(y):
        # A variável randomizado recebe um numero no intervalo de 2, number -2
        randomizado = random.randint(2, number - 2)
        x = pow(randomizado, d, number)
        if x == 1 or x == number - 1:
            continue
        for Rabin in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Gera números aleatórios em bits
def gerar_primo(bits):
    while True:
        numero = random.getrandbits(bits)
        # Faz a verificação para ver se o numero não é primo
        if numero % 2 != 0 and verificar_primos(numero):
            return numero
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #


# Numero de primero em bits formular de acordo com a necessidade
bits = 8
# Variáveis que vão receber os primos
chave_P = gerar_primo(bits)
chave_Q = gerar_primo(bits)
# Mostra na tela ambos os primos
print(f"Número primo P com {bits} bits: {chave_P}")
print(f"Número primo Q com {bits} bits: {chave_Q}")
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Calcula o valor de N
def calcular_N(p, q):
    n = p * q
    return n
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Mostra a chave N e chama a função 
chave_N = calcular_N(chave_P, chave_Q)
print(f"O valor de N é: {chave_N}")
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Calcula o valor de Z
def calcular_Z(p, q):
    z = (p - 1)*(q-1)
    return z
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Mostra a chave Z e chama a função
chave_Z = calcular_Z(chave_P, chave_Q)
print(f"O valor de Z é: {chave_Z}")
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Calcula a chave E
def calcular_E(z):
    # O valor para E é 65537
    e = 65537
    # Garante que E seja coprimo com Z
    while math.gcd(e, z) != 1:
        e = random.randint(2, z - 1)
    return e
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Chama a função para encontrar o expoente de cifragem E
chave_E = calcular_E(chave_Z)
print(f"O valor de E é: {chave_E}")
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Calcula o inverso modular
# usando o algoritmo de Euclides Estendido
def inverso_modulo(z, e):

    if e == 0:
        return (z, 1, 0)
    else:
        g, x, n = inverso_modulo(e, z % e)
        return (g, n, x - (z // e) * n)
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Calcula a chave D usando o algoritmo de Euclides Estendido
def calcular_D(z, e):
    # Formação da tupla para mostrar apenas o numero do meio e ignorar os outros dois valores
    _, d, _ = inverso_modulo(e, z)
    # Calcula o modulo desse valor
    d = (d + z) % z
    return d
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Mostra a chave D
chave_D = calcular_D(chave_Z, chave_E)
print(f"O valor de D é: {chave_D}")
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Converte a mensagem com a função ord() para Código Padrão Americano 
numeros = [ord(caractere) for caractere in texto_base]
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Criptografa
texto_cifra = [(numero ** chave_E) % chave_N for numero in numeros]
print("Texto encriptado:", texto_cifra)