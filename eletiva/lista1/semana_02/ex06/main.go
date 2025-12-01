package main

import (
	"fmt"
	"sort"
)

// 6- Algoritmo que faça a ordenação de uma sequência numérica
func main() {
	numbers := []int{64, 34, 25, 12, 22, 11, 90}

	fmt.Println("Array original:", numbers)

	sort.Ints(numbers)

	fmt.Println("Array ordenado:", numbers)
}

// Output:
// Array original: [64 34 25 12 22 11 90]
// Array ordenado: [11 12 22 25 34 64 90]
