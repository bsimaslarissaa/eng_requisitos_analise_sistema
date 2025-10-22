
NUM_ALUNOS = 5
nomes = []
notas = []
total_notas = 0.0

print("=== SISTEMA DE CADASTRO DE ALUNOS ===")


for i in range(NUM_ALUNOS):
    nome = input(f"Digite o nome do aluno {i + 1}: ").strip()
    nota = float(input(f"Digite a nota de {nome}: "))

    nomes.append(nome)
    notas.append(nota)

    total_notas += nota


media_alunos = total_notas / NUM_ALUNOS


print("\n=== LISTA DE ALUNOS ===")
for i in range(NUM_ALUNOS):
    print(f"{nomes[i]} | Nota: {notas[i]:.2f}")

print(f"\nMédia da turma: {media_alunos:.2f}")