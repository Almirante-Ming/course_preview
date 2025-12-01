package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

// 17- Algoritmo que simule o jogo da adivinhação
func main() {
	rand.Seed(time.Now().UnixNano())
	secretNumber := rand.Intn(100) + 1
	attempts := 0
	guessed := false

	fmt.Println("=== Jogo da Adivinhação ===")
	fmt.Println("Pensei em um número entre 1 e 100")
	fmt.Println("Tente adivinhar!")

	reader := bufio.NewReader(os.Stdin)

	for !guessed {
		fmt.Print("Digite um número: ")
		input, _ := reader.ReadString('\n')
		guess, err := strconv.Atoi(input[:len(input)-1])

		if err != nil {
			fmt.Println("Entrada inválida!")
			continue
		}

		attempts++

		if guess < secretNumber {
			fmt.Println("Meu número é maior!")
		} else if guess > secretNumber {
			fmt.Println("Meu número é menor!")
		} else {
			fmt.Printf("Parabéns! Você acertou em %d tentativas!\n", attempts)
			guessed = true
		}
	}
}

// Output (exemplo):
// === Jogo da Adivinhação ===
// Pensei em um número entre 1 e 100
// Tente adivinhar!
// Digite um número: 50
// Meu número é maior!
// Digite um número: 75
// Meu número é menor!
// Digite um número: 60
// Parabéns! Você acertou em 3 tentativas!
