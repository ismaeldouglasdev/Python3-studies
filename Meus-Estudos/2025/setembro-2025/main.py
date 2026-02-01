notas = []

contador = 1

while contador <= 5:
    cod_aluno = input("RM: ")
    nota = float(input("Nota: "))
    result = [cod_aluno, nota]
    notas.append(result)

    # alternativa: contador += 1
    contador = contador + 1

print("quantidade de notas", len(notas))

for n in notas:
    cod_aluno = n[0]
    nota = n[1]
    print("O RM", cod_aluno, "tirou a nota:", nota)