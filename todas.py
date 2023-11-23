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
