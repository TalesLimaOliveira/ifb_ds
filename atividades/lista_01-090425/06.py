import numpy as np

# Passo 1: Gerar array A com números ímpares de 0 a 100
A = np.arange(1, 100, 2)

# Passo 2: Filtrar elementos divisíveis por 3 e 5 (ou seja, por 15)
divisible_by_15 = A[(A % 15 == 0)]

# Passo 3: Calcular a soma cumulativa
cumulative_sum = np.cumsum(divisible_by_15)

# Exibir os resultados
print("Array A (ímpares):", A)
print("Divisíveis por 3 e 5:", divisible_by_15)
print("Soma cumulativa:", cumulative_sum)