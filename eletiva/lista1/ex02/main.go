package main

import "fmt"

// 2- Divisão de dois números inteiros
func main() {
	num1 := 20
	num2 := 4

	if num2 == 0 {
		fmt.Println("Erro: divisão por zero")
		return
	}

	result := num1 / num2
	fmt.Printf("Divisão de %d / %d = %d\n", num1, num2, result)
}

// Output:
// Divisão de 20 / 4 = 5
