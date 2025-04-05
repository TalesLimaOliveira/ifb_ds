def remove_first_and_last(arr):
    if len(arr) <= 2:
        return []  # Retorna lista vazia se tiver 2 ou menos elementos
    return arr[1:-1]

lista = [10, 20, 30, 40, 50]
nova_lista = remove_first_and_last(lista)
print("Nova lista:", nova_lista)