import numpy as np
import matplotlib.pyplot as plt

# define a função a ser calculada junto aos parâmetros
def calcular_pitch(f, f0=1, p0=0):
    p=p0+12*np.log2(f/f0)
    return p

#coleta de dados
f = float(input("Digite a frequência desejada: "))
f0 = float(input("digite o valor da frequencia de referência (f⁰), ou pressione enter para usar o valor padrão: "))
p0 = float(input("Digite o valor do tom de referência (p⁰), ou pressione enter para usar o valor padrão: "))

# define o período do gráfico
tempos_grafico = np.linspace(0.1, 10, 100)

# calculo correspondente dos tons
pitch_grafico=[calcular_pitch(f) for f in tempos_grafico]

# gerando um gráfico
plt.plot(tempos_grafico, pitch_grafico, label="P(f)")
plt.xlabel("frequência (em hetz)")
plt.ylabel("Pitch")
plt.title("Gráfico da Função P(f) = P⁰ + 12*log2(f/f⁰)")
plt.legend()
plt.grid(True)
plt.show()
