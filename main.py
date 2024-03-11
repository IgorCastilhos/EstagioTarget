# Questão 1 - 91
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# Questão 2
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

print(fibonacci(21))  # True
print(fibonacci(22))  # False

# Questão 3
# a) 1, 3, 5, 7, 9
# b) 2, 4, 8, 16, 32, 64, 128
# c) 0, 1, 4, 9, 16, 25, 36, 49
# d) 4, 16, 36, 64, 100
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2,10, 12, 16, 17, 18, 19, 20

# Questão 5 - A função itera pelos índices da string de trás pra frente, começando lá do último caractere até o 1º, daí em cada iteração ela concatena o caractere atual pra string invertida.
def reverse_string(string):
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

print(reverse_string('Hello World'))  # dlroW olleH
