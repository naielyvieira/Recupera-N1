livros = []
tamanho = int(input("Digite o tamanho da lista: "))
for i in range(tamanho):
    livro = input("Digite o nome do livro: ")
    ranking = input("Digite em que ranking o livro está: ")
    livros.append((ranking, livro))
livro_ranking = sorted(livros)
print("Ranking de livros mais vendidos")
print("-=-" * 20)
for ranking, livro in livro_ranking:
    print(f"{ranking} - {livro}")
    print("-=-" * 20)
