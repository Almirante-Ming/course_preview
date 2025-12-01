package main

import (
	"fmt"
	"strings"
)

// 20- Algoritmo que retorne a quantidade de ocorrências de uma palavra no texto
func countWordOccurrences(text, word string) int {
	text = strings.ToLower(text)
	word = strings.ToLower(word)

	words := strings.FieldsFunc(text, func(r rune) bool {
		return r == ' ' || r == ',' || r == '.' || r == '!' || r == '?'
	})

	count := 0
	for _, w := range words {
		if w == word {
			count++
		}
	}

	return count
}

func main() {
	text := "golang é ótimo, golang é rápido, golang é eficiente"
	word := "golang"

	count := countWordOccurrences(text, word)

	fmt.Printf("Texto: %s\n", text)
	fmt.Printf("Palavra buscada: \"%s\"\n", word)
	fmt.Printf("Ocorrências: %d\n", count)
}

// Output:
// Texto: golang é ótimo, golang é rápido, golang é eficiente
// Palavra buscada: "golang"
// Ocorrências: 3
