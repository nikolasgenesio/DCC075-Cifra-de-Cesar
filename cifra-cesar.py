# Função para criptografar a mensagem
def criptografar(mensagem, deslocamento):
    texto_encriptado = ""

    # Percorrendo o texto
    for i in range(len(mensagem)):
        char = mensagem[i]

        # Criptografando letras maiúsculas
        if char.isupper():
            texto_encriptado += chr((ord(char) - 65 + deslocamento) % 26 + 65)
        # Criptografando letras minúsculas
        else:
            texto_encriptado += chr((ord(char) - 97 + deslocamento) % 26 + 97)

    return texto_encriptado

# Função para descriptografar a cifra de César
def descriptografar(mensagem, deslocamento):
    texto_decriptado = ""

    # Percorrendo cada caractere do texto
    for char in mensagem:
        # Verificando se o caractere é uma letra
        if char.isalpha():
            # Verificando se o caractere é maiúsculo
            if char.isupper():
                # Descriptografando o caractere e adicionando ao texto
                texto_decriptado += chr((ord(char) - deslocamento - 65) % 26 + 65)
            else:
                # Descriptografando o caractere e adicionando ao texto
                texto_decriptado += chr((ord(char) - deslocamento - 97) % 26 + 97)
        else:
            # Se o caractere não for uma letra, adicionando ao texto como está
            texto_decriptado += char

    return texto_decriptado

# Função para o usuário digitar a mensagem e deslocamento para criptografar ou descriptografar uma mensagem
def main():
    while True:
        opcao = input("Digite 1 para criptografar e 2 para descriptografar a mensagem: ")

        if opcao == "1" or opcao == "2":
            mensagem = input("Digite a mensagem: ")
            deslocamento = int(input("Digite o deslocamento: "))

            if opcao == "1":
                resultado = criptografar(mensagem, deslocamento)
                print("Mensagem criptografada:", resultado)
            else:
                resultado = descriptografar(mensagem, deslocamento)
                print("Mensagem descriptografada:", resultado)
            break
        else:
            print("Opção inválida!")

# Chamando a função
main()