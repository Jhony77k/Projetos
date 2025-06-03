def calcular_fatorial(n):
    """
    Calcula o fatorial de um número inteiro positivo.
    """
    if n < 0:
        return "Não existe fatorial de números negativos"
    elif n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

# Exemplo de uso
numero = 5
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")