def best_exam(scores):
    if not scores or not scores[0]:
        return None  # Lista vazia ou mal formatada

    # Supondo que todas as linhas têm o mesmo tamanho
    num_exams = len(scores[0])
    total_by_exam = [0] * num_exams

    # Soma das colunas
    for row in scores:
        for i in range(num_exams):
            total_by_exam[i] += row[i]

    # Encontrar o índice da prova com maior soma
    max_index = total_by_exam.index(max(total_by_exam))
    return max_index  # ou retornar "Prova 1", "Prova 2", etc.

# Cada linha: jogador -> [prova1, prova2, prova3]
pontuacoes = [
    [10, 8, 6],
    [7, 9, 5],
    [8, 6, 9]
]

print(f"A prova com maior soma de pontuações é a Prova {best_exam(pontuacoes) + 1}")