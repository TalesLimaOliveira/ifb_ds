import numpy as np

def weighted_average(values, weights):
    values = np.array(values)
    weights = np.array(weights)
    
    if values.size != weights.size:
        raise ValueError("Os vetores de valores e pesos devem ter o mesmo tamanho.")
    
    total_weight = np.sum(weights)
    weighted_sum = np.sum(values * weights)
    
    return weighted_sum / total_weight

    
valores = [7.5, 8.0, 6.0]
pesos = [2, 3, 1]

media = weighted_average(valores, pesos)
print(f"Média ponderada: {media:.2f}")