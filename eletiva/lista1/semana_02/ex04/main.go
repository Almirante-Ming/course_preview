package main

import "fmt"

// 4- Verificar se um número é par/impar, positivo/negativo
func main() {
	num := -7

	// Verificar par ou impar
	if num%2 == 0 {
		fmt.Printf("%d é par\n", num)
	} else {
		fmt.Printf("%d é impar\n", num)
	}

	// Verificar positivo ou negativo
	if num > 0 {
		fmt.Printf("%d é positivo\n", num)
	} else if num < 0 {
		fmt.Printf("%d é negativo\n", num)
	} else {
		fmt.Printf("%d é zero\n", num)
	}
}

// Output:
// -7 é impar
// -7 é negativo
