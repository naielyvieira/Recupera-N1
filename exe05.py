alunos = 10
soma = 0

print("Digite as notas dos alunos")

for i in range(alunos):
    nota = float(input(f"Nota do aluno {i+1}: "))
    soma += nota

media = soma / alunos
print("A média das notas dos alunos é: {:.2f}".format(media))
