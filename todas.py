# Questao 1

# Item a

def calcular_quadrados_concatenar(numero):
    # Converte o número para uma string para iterar sobre seus dígitos
    numero_str = str(numero)

    # Calcula os quadrados dos dígitos e os concatena
    resultado = ''.join(str(int(digito) ** 2) for digito in numero_str)

    # Converte o resultado de volta para um número inteiro
    resultado_int = int(resultado)

    return resultado_int

# Exemplo de uso:
numero = 6122
resultado = calcular_quadrados_concatenar(numero)
print(resultado)

# Item b

def algarismos_nao_aparecem_na_unidade():
    algarismos = set(range(10))  # Algarismos de 0 a 9
    quadrados = set()

    for i in algarismos:
        quadrados.add((i**2) % 10)  # Calcula o quadrado e pega a unidade

    nao_aparecem = sorted(list(algarismos - quadrados))
    return nao_aparecem

# Exemplo de uso:
algarismos_nao_aparecem = algarismos_nao_aparecem_na_unidade()
print("Algarismos que nunca aparecem na casa das unidades:", algarismos_nao_aparecem)

# Fim questao 1 ----------------------

# Questao 2 

# Item a

def indice_primeiro_termo_fibonacci_com_n_digitos(n):
    fib = [0, 1]  # Inicializa os dois primeiros termos da sequência de Fibonacci
    index = 2  # Índice inicial

    while True:
        next_term = fib[-1] + fib[-2]
        fib.append(next_term)

        # Verifica se o próximo termo tem n dígitos
        if len(str(next_term)) == n:
            return index

        index += 1

# Exemplo de uso:
n = 5
resultado = indice_primeiro_termo_fibonacci_com_n_digitos(n)
print("O índice do primeiro termo da sequência de Fibonacci com", n, "dígitos é:", resultado)

# Item b

O primeiro elemento da sequencia com 1000 dígitos ocorre na posição 4782

# Fim questao 2 ----------------------

# Questao 3

def decodificar_huffman(codigo, tabela):
    mensagem_decodificada = ""
    codigo_atual = ""

    for bit in codigo:
        codigo_atual += bit

        # Verifica se o código atual está na tabela
        for caractere, cod in tabela.items():
            if cod == codigo_atual:
                mensagem_decodificada += caractere
                codigo_atual = ""  # Reinicia o código atual

    return mensagem_decodificada

# Tabela de codificação Huffman corrigida
tabela_huffman_corrigida = {'A': '0', 'B': '111', 'C': '1100', 'D': '1101', 'R': '10'}

# Exemplo de uso com a mensagem "BARCA"
codigo_corrigido = '11101011000'
mensagem_original_corrigida = decodificar_huffman(codigo_corrigido, tabela_huffman_corrigida)
print("Mensagem decodificada:", mensagem_original_corrigida)

# Item B

# Exemplo de uso com a mensagem "Questao B"
codigo_corrigido = '0110001111001111001101001100011010010010100100'
mensagem_original_corrigida = decodificar_huffman(codigo_corrigido, tabela_huffman_corrigida)
print("Mensagem decodificada:", mensagem_original_corrigida)

# Fim Questao 3 ----------------------
