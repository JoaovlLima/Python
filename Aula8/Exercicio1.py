# Crie graficos com uma tabela de excel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl 

df = pd.read_excel('Aula8/filmes.xlsx')

# Plotar gráfico de barras das Avaliacoes com Seaborn
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
sns.barplot(data=df, x='Nome', y='avaliacao', palette='pastel')  # Plotar gráfico de barras com Seaborn
plt.title('Gráfico de Barras das Notas - Seaborn')  # Definir título do gráfico
plt.xlabel('Nomes')  # Definir rótulo do eixo x
plt.ylabel('avaliacao')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.xticks(rotation = 45, ha = 'right')
plt.show()  # Mostrar o gráfico


