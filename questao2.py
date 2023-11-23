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
