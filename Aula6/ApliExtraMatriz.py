import numpy as np
import matplotlib.pyplot as plt

preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])

acoes_acao1 = np.array([100])  # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = np.array([50])   # Exemplo: o investidor possui 50 ações da Ação 2

# Calculando o valor do investimento em cada dia
valorInvestido1 = acoes_acao1 * preco_medio_acao1
valorInvestido2 = acoes_acao2 * preco_medio_acao2
print(f"Valor investido 1 :{valorInvestido1}\n Valor Investido 2 :{valorInvestido2}")

# Calculando o patrimônio total do investidor em cada dia
totalInvestido = valorInvestido1 + valorInvestido2
print(f"Valor total Investido é: {totalInvestido}")

#plot Evolução Patrimonial
dias = np.arange(1, len(preco_medio_acao1) + 1)

plt.plot(dias, totalInvestido, label='Total Investido', marker='o')
plt.plot(dias, valorInvestido1, label='Investimento 1', marker='o')
plt.plot(dias, valorInvestido2, label='Investimento 2', marker='o')
plt.xlabel('Dias')
plt.ylabel('Patrimônio')
plt.title('Evolução Patrimonial do Investidor')
plt.grid(True)
plt.legend()
plt.show()


