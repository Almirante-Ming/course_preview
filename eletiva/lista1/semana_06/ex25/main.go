package main

import "fmt"

// 25- Algoritmo que calcule a média entre dois ou mais números
func calculateAverage(numbers ...float64) float64 {
	if len(numbers) == 0 {
		return 0
	}

	sum := 0.0
	for _, num := range numbers {
		sum += num
	}

	return sum / float64(len(numbers))
}

func main() {
	// Teste com diferentes quantidades de números
	avg1 := calculateAverage(10, 20)
	fmt.Printf("Média de 10 e 20: %.2f\n", avg1)

	avg2 := calculateAverage(5, 10, 15, 20)
	fmt.Printf("Média de 5, 10, 15 e 20: %.2f\n", avg2)

	avg3 := calculateAverage(7.5, 8.5, 9.0, 8.0, 9.5)
	fmt.Printf("Média de 7.5, 8.5, 9.0, 8.0 e 9.5: %.2f\n", avg3)
}

// Output:
// Média de 10 e 20: 15.00
// Média de 5, 10, 15 e 20: 12.50
// Média de 7.5, 8.5, 9.0, 8.0 e 9.5: 8.50
