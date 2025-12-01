package main

import (
	"fmt"
	"strings"
)

// 14- Algoritmo que verifica se uma sequência de caracteres é um palíndromo
func isPalindrome(text string) bool {
	// Remover espaços e converter para minúsculas
	cleaned := strings.ToLower(strings.ReplaceAll(text, " ", ""))

	// Verificar se é palíndromo
	for i := 0; i < len(cleaned)/2; i++ {
		if cleaned[i] != cleaned[len(cleaned)-1-i] {
			return false
		}
	}

	return true
}

func main() {
	testCases := []string{
		"ama",
		"A mala nala",
		"Socorram me subi no onibus em marrocos",
		"golang",
		"racecar",
	}

	for _, text := range testCases {
		result := isPalindrome(text)
		fmt.Printf("\"%s\" é palíndromo? %v\n", text, result)
	}
}

// Output:
// "ama" é palíndromo? true
// "A mala nala" é palíndromo? true
// "Socorram me subi no onibus em marrocos" é palíndromo? true
// "golang" é palíndromo? false
// "racecar" é palíndromo? true
