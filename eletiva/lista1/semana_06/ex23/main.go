package main

import (
	"fmt"
)

// 23- Algoritmo que calcule o IMC (Índice de Massa Corporal)
// Fórmula padrão brasileira: IMC = peso (kg) / altura² (m²)
func calculateIMC(weight float64, height float64) (float64, string) {
	imc := weight / (height * height)

	var category string
	if imc < 18.5 {
		category = "Abaixo do peso"
	} else if imc < 24.9 {
		category = "Peso normal"
	} else if imc < 29.9 {
		category = "Sobrepeso"
	} else if imc < 34.9 {
		category = "Obesidade Grau I"
	} else if imc < 39.9 {
		category = "Obesidade Grau II"
	} else {
		category = "Obesidade Grau III"
	}

	return imc, category
}

func main() {
	testCases := []struct {
		name   string
		weight float64
		height float64
	}{
		{"João", 70, 1.75},
		{"Maria", 60, 1.65},
		{"Pedro", 85, 1.80},
	}

	fmt.Println("=== Cálculo de IMC ===")
	for _, tc := range testCases {
		imc, category := calculateIMC(tc.weight, tc.height)
		fmt.Printf("%s: %.2f kg, %.2f m\n", tc.name, tc.weight, tc.height)
		fmt.Printf("IMC: %.2f - %s\n\n", imc, category)
	}
}

// Output:
// === Cálculo de IMC ===
// João: 70.00 kg, 1.75 m
// IMC: 22.86 - Peso normal
//
// Maria: 60.00 kg, 1.65 m
// IMC: 22.04 - Peso normal
//
// Pedro: 85.00 kg, 1.80 m
// IMC: 26.23 - Sobrepeso
