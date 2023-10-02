import json

nota_aluno = {}

try:
    with open("BANCO_DE_NOTAS.json", "r") as json_file:
        dados = json.load(json_file)
        if json_file != None:
            with open("BANCO_DE_NOTAS.json", "r") as json_file:
                nota_aluno.update(dados)
except:
    None

print("\nProjeto: \033[1mPROGRAMA ESCOLAR PARA ARMAZENAMENTO E CALCULO DE MÉDIA\033[0m")

def media(a):
    return sum(nota_aluno.get(aluno)) / len(nota_aluno.get(aluno))

pergunta_aluno = input("\nGostaria de inserir notas?: ").upper()
while pergunta_aluno == 'SIM':
    aluno = input("\nDigite o nome do Aluno: ")
    if aluno in nota_aluno:
        nota_aluno.pop(aluno)
    else:
        print("\nEsse aluno não foi identificado. Adicionando...")
    nota_aluno[aluno] = [
        float(input("Insira sua nota: ")),
        float(input("Insira sua nota: ")),
        float(input("Insira sua nota: ")),
        float(input("Insira sua nota: "))
    ]
    pergunta_aluno = input("\nGostaria de inserir notas?: ").upper()
    with open("BANCO_DE_NOTAS.json", "w") as json_file:
        json.dump(nota_aluno, json_file)

pergunta = input("\nVocê deseja calcular a média de algum aluno?: ").upper()
if pergunta == 'SIM':
    print("\nAlunos (Inserir os nomes iguais inseridos anteriormente): ")
    for chave in nota_aluno.keys():  # Imprimindo todos os alunos
        print("->", chave)
while True:
    if pergunta == 'SIM':
        aluno = input("\nDigite o nome do Aluno: ")
        print("A média do aluno inserido é: ", media(aluno))
        pergunta = input("\nVocê deseja calcular a média de algum aluno?: ").upper()
    elif pergunta != 'SIM':
        print("\nO programa foi encerrado. Caso queira consultar novamente, inicie o programa")
        break


