package main

import (
	"fmt"
	"sort"
	"strings"
)

// 7- Ordenação de sequência de caracteres em ordem ascendente
func main() {
	text := "golang"

	// Converter string para slice de caracteres
	chars := strings.Split(text, "")

	fmt.Printf("Texto original: %s\n", text)

	// Ordenar em ordem ascendente
	sort.Strings(chars)

	sorted := strings.Join(chars, "")
	fmt.Printf("Texto ordenado: %s\n", sorted)
}

// Output:
// Texto original: golang
// Texto ordenado: aglno
