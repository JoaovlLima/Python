import yaml

with open('Aula8/Projeto/empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file)
    
total_gasto_por_cliente = {}
alteraCliente = {}


for venda in dados['vendas']:
    cliente_id = venda['cliente_id']
    preco_unitario = venda['preco_unitario']
    quantidade = venda['quantidade']
    total_gasto = preco_unitario * quantidade
    

    if cliente_id in total_gasto_por_cliente:
        total_gasto_por_cliente[cliente_id] += total_gasto
    else:
        total_gasto_por_cliente[cliente_id] = total_gasto


for cliente_id, total_gasto in total_gasto_por_cliente.items():
    print(f"Cliente ID {cliente_id}: R$ {total_gasto:.2f}")
    
for cliente in dados['comportamento_do_cliente']:
    cliente_id = cliente['id']
    if cliente_id in total_gasto_por_cliente:
        cliente['valor_gasto_total'] = total_gasto_por_cliente[cliente_id]

# Salva as alterações de volta no arquivo YAML
with open('Aula8/Projeto/empresa.yaml', 'w') as file:
    yaml.dump(dados, file)

print("Valor total gasto por cliente foi adicionado à tabela de comportamento do cliente.")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Supondo que df_cliente seja o DataFrame dos clientes e df_vendas seja o DataFrame das vendas

# Mesclar os DataFrames de cliente e vendas com base no ID do cliente
df_merged = pd.merge(df_vendas, df_cliente, left_on='cliente_id', right_on='id', how='left')

# Calcular a frequência de compra por cliente
frequencia_compra = df_merged.groupby(['cliente_id', 'nome']).size().reset_index(name='frequencia')

# Plotar o gráfico de barras
sns.barplot(data=frequencia_compra, x='nome', y='frequencia')
plt.xlabel('Nome do Cliente')
plt.ylabel('Frequência de Compra')
plt.title('Histograma da Frequência de Compra por Cliente')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para facilitar a leitura
plt.show()
