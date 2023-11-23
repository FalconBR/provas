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
