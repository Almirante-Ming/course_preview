package main

import (
	"fmt"
	"strings"
	"unicode"
)

// 19- Algoritmo que conte vogais e consoantes de um texto
func countVowelsAndConsonants(text string) (int, int) {
	vowels := 0
	consonants := 0

	text = strings.ToLower(text)
	vowelMap := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}

	for _, char := range text {
		if unicode.IsLetter(char) {
			if vowelMap[char] {
				vowels++
			} else {
				consonants++
			}
		}
	}

	return vowels, consonants
}

func main() {
	text := "Olá, mundo! Bem vindo ao programa."

	vowels, consonants := countVowelsAndConsonants(text)

	fmt.Printf("Texto: %s\n", text)
	fmt.Printf("Vogais: %d\n", vowels)
	fmt.Printf("Consoantes: %d\n", consonants)
}

// Output:
// Texto: Olá, mundo! Bem vindo ao programa.
// Vogais: 13
// Consoantes: 19
