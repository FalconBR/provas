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
