package main

import "fmt"

// 13- Algoritmo que retorne a moda de uma sequência numérica
func findMode(numbers []int) int {
	frequencyMap := make(map[int]int)

	// Contar frequência de cada número
	for _, num := range numbers {
		frequencyMap[num]++
	}

	maxFreq := 0
	mode := 0

	// Encontrar o número com maior frequência
	for num, freq := range frequencyMap {
		if freq > maxFreq {
			maxFreq = freq
			mode = num
		}
	}

	return mode
}

func main() {
	numbers := []int{1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5}

	fmt.Printf("Sequência: %v\n", numbers)

	mode := findMode(numbers)
	fmt.Printf("Moda: %d\n", mode)
}

// Output:
// Sequência: [1 2 2 3 3 3 4 4 4 4 5]
// Moda: 4
