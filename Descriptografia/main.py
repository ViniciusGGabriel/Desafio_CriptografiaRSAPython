# Capturando entrada do usuário para chave_N
chave_N = int(input("Digite o valor para chave_N: "))
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Capturando entrada do usuário para chave_D
chave_D = int(input("Digite o valor para chave_D: "))
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Pegando dados da mensagem do usuário em armazenando tem texto cifra (como uma lista de números)
texto_cifra = input("Digite os valores da mensagem separados por espaço: ")
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Convertendo os valores para inteiros e dividindo a entrada com espaços
texto_cifra = list(map(int, texto_cifra.split()))
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Descriptografa
mensagem_descriptografada = [chr((numero ** chave_D) % chave_N) for numero in texto_cifra]
mensagem_original = ''.join(mensagem_descriptografada)
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# Mostra a mensagem
print("Mensagem descriptografada:", mensagem_original)