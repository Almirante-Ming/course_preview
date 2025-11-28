package main

import "fmt"

// 24- Algoritmo que calcule o MMC (Mínimo Múltiplo Comum)
func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func lcm(a, b int) int {
	return (a * b) / gcd(a, b)
}

func main() {
	testCases := []struct {
		a, b int
	}{
		{12, 18},
		{20, 30},
		{7, 11},
	}

	fmt.Println("=== Cálculo de MMC ===")
	for _, tc := range testCases {
		result := lcm(tc.a, tc.b)
		fmt.Printf("MMC de %d e %d = %d\n", tc.a, tc.b, result)
	}
}

// Output:
// === Cálculo de MMC ===
// MMC de 12 e 18 = 36
// MMC de 20 e 30 = 60
// MMC de 7 e 11 = 77
