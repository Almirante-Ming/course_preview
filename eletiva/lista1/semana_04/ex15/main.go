package main

import "fmt"

// 15- Algoritmo que calcule a área de um retângulo
func calculateRectangleArea(width, height float64) float64 {
	return width * height
}

func main() {
	width := 5.0
	height := 3.0

	area := calculateRectangleArea(width, height)

	fmt.Printf("Retângulo com largura %.2f e altura %.2f\n", width, height)
	fmt.Printf("Área: %.2f\n", area)
}

// Output:
// Retângulo com largura 5.00 e altura 3.00
// Área: 15.00
