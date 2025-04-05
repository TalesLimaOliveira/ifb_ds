import numpy as np

def remove_first_and_last(arr):
    if arr.size <= 2:
        return np.array([])  # Retorna array vazio se tiver 2 ou menos elementos
    return arr[1:-1]

array = np.array([10, 20, 30, 40, 50])
new_array = remove_first_and_last(array)
print("Novo array:", new_array)