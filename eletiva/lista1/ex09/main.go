package main

import "fmt"

// 9- Imprimir uma variável e o endereço de uma variável (Ponteiros)
func main() {
	name := "João"
	age := 25

	// Imprimir valor das variáveis
	fmt.Printf("Variável name: %v\n", name)
	fmt.Printf("Variável age: %v\n", age)

	// Imprimir endereço das variáveis
	fmt.Printf("Endereço de name: %p\n", &name)
	fmt.Printf("Endereço de age: %p\n", &age)

	// Usando ponteiros
	ptrName := &name
	fmt.Printf("Valor via ponteiro: %v\n", *ptrName)
	fmt.Printf("Endereço do ponteiro: %p\n", ptrName)
}

// Output:
// Variável name: João
// Variável age: 25
// Endereço de name: 0xc0000461f0
// Endereço de age: 0xc000012340
// Valor via ponteiro: João
// Endereço do ponteiro: 0xc0000461f0
