Para construir a equação de movimento do bloco, precisamos da segunda lei de Newton:

F = m * a

Onde 𝑎 é a aceleração do bloco, 𝑚 é a massa e 𝐹 é a força resultante atuando sobre ele. A força resultante inclui a força do motor e a força de arrasto do ar, que podem ser escritas como:

F = F_motor - b * v^2

Substituindo as equações acima na segunda lei de Newton, temos:

m * a = F_motor - b * v^2

Como a força do motor é variável no tempo, usaremos a equação 𝐹(𝑡) = 10 + 5,0𝑡 (SI). Assim, a equação de movimento fica:

m * a = 10 + 5 * t - b * v^2

Para resolver numericamente essa equação diferencial, usaremos o método de integração de Heun. Este método consiste em estimar a aceleração no próximo passo de tempo a partir da média ponderada das acelerações calculadas com as velocidades estimadas pelo método de Euler.

Para isso, precisamos da equação da velocidade:

v = v0 + a * t

e da equação da posição:

x = x0 + v * t

Também precisamos das condições iniciais:

v0 = 0 m/s (o bloco está inicialmente em repouso)
x0 = 0 m (o bloco está inicialmente na posição inicial)
