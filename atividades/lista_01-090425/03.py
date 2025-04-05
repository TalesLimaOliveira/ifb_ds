def count_long_words(word_list):
    return len([word for word in word_list if len(word) > 5])

words = ["banana", "sol", "computador", "livro", "água", "amizade"]
print(count_long_words(words))