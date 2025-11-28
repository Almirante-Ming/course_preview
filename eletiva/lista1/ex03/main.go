package main

import "fmt"

// 3- Algoritmo que receba número inteiro e imprima o sucessor e o antecessor
func main() {
	num := 5
	successor := num + 1
	predecessor := num - 1

	fmt.Printf("Número: %d\n", num)
	fmt.Printf("Sucessor: %d\n", successor)
	fmt.Printf("Antecessor: %d\n", predecessor)
}

// Output:
// Número: 5
// Sucessor: 6
// Antecessor: 4
