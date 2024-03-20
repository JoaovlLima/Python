import yaml
import faker
import random

# Inicializando o gerador de dados fictícios
fake = faker.Faker('pt_BR')

# Gerando 100 nomes de alunos fictícios
nomes_alunos = [fake.name() for _ in range(100)]

# Gerando notas aleatórias para os alunos
notas = [random.randint(1, 10) for _ in range(100)]

# Gerando idades aleatórias para os alunos (entre 18 e 25 anos)
idades = [random.randint(18, 25) for _ in range(100)]

# Gerando alturas aleatórias para os alunos (entre 1.5 e 2.0 metros)
alturas = [round(random.uniform(1.5, 2.0), 2) for _ in range(100)]

# Construindo o dicionário de dados com os 100 alunos
dados = {
    'alunos': nomes_alunos,
    'notas': notas,
    'idade': idades,
    'altura': alturas
}

# Salvar os dados em um arquivo YAML
with open('Aula8/dados.yaml', 'w') as file:
    yaml.dump(dados, file)

print("Arquivo YAML criado com sucesso!")
