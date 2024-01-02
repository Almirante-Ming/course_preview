import random

def random_between_1_and_10():
    d = random.random() * 10
    i = int(d) + 1
    return i

if __name__ == "__main__":
    print("Gerando 100 números aleatórios entre 1 e 10:")
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(100):
        v[random_between_1_and_10()] += 1

    for i in range(1, len(v)):
        if v[i] > 0:
            print(f"Número {i} gerado {v[i]} vezes.")