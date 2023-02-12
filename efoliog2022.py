import numpy as np
import matplotlib.pyplot as plt
 
# Define os parâmetros
m = 2.0 # kg
b = 8.0 # kg/m

# Define a força do motor
def F_motor(t):
    return 10 + 5 * t

# Define a equação diferencial
def aceleracao(v, t):
    return (F_motor(t) - b * v**2) / m

# Define o intervalo de tempo
t = np.linspace(0, 3.0, 30) # s

# Define as condições iniciais
v0 = 0 # m/s
x0 = 0 # m

# Inicializa os arrays de tempo, velocidade e posição
v = np.zeros(len(t))
x = np.zeros(len(t))

# Define as condições iniciais
v[0] = v0
x[0] = x0
h = t[1] - t[0]
for i in range(1, len(t)):
    k1 = aceleracao(v[i-1], t[i-1])
    k2 = aceleracao(v[i-1] + h * k1, t[i] + h)
    v[i] = v[i-1] + h / 2 * (k1 + k2)
    x[i] = x[i-1] + h * v[i-1] + h**2 / 2 * k1

for i in range(1, len(t)):
    if v[i] >= 0.04:
        tempo = t[i]
    break
print("O tempo para atingir a velocidade de 4 cm/s é de {:.2f} s".format(tempo))
  
plt.plot(t, v)
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.title("Gráfico da Velocidade como Função do Tempo")
plt.show()