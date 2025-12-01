package main

import "fmt"

// 21- Algoritmo que calcule o fatorial de um número N
func factorial(n int) int {
	if n < 0 {
		return 0 // Fatorial não definido para negativos
	}
	if n == 0 || n == 1 {
		return 1
	}
	return n * factorial(n-1)
}

func main() {
	testNumbers := []int{0, 1, 5, 10}

	for _, num := range testNumbers {
		result := factorial(num)
		fmt.Printf("Fatorial de %d = %d\n", num, result)
	}
}

// Output:
// Fatorial de 0 = 1
// Fatorial de 1 = 1
// Fatorial de 5 = 120
// Fatorial de 10 = 3628800
