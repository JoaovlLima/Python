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