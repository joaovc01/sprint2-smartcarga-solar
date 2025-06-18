import matplotlib.pyplot as plt
import numpy as np

# Dados de velocidade (m/s) simulados
velocidades = np.array([20, 25, 30, 35, 40, 45, 50])

# Função para calcular a escala Richter a partir da velocidade
def escala_richter(vel):
    # Fórmula simplificada de exemplo: Richter = log10(velocidade) + 1.5
    return np.log10(vel) + 1.5

# Calcula a escala Richter para cada velocidade
richter = escala_richter(velocidades)

# Encontrar máximo e mínimo
max_richter = np.max(richter)
min_richter = np.min(richter)
max_index = np.argmax(richter)
min_index = np.argmin(richter)

print(f'Máximo na escala Richter: {max_richter:.2f} (velocidade: {velocidades[max_index]} m/s)')
print(f'Mínimo na escala Richter: {min_richter:.2f} (velocidade: {velocidades[min_index]} m/s)')

# Plotar gráfico
plt.plot(velocidades, richter, marker='o', linestyle='-', color='blue')
plt.title('Escala Richter em função da Velocidade')
plt.xlabel('Velocidade (m/s)')
plt.ylabel('Escala Richter')
plt.grid(True)

# Destacar máximo e mínimo no gráfico
plt.scatter(velocidades[max_index], max_richter, color='red', label='Máximo')
plt.scatter(velocidades[min_index], min_richter, color='green', label='Mínimo')
plt.legend()

plt.show()

