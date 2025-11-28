package main

import "fmt"

// 12- Algoritmo que retorne um valor booleano indicando igualdade
func isEqual(a, b interface{}) bool {
	return a == b
}

func main() {
	// Teste com inteiros
	val1 := 10
	val2 := 10
	val3 := 20

	fmt.Printf("Comparação: %v == %v: %v\n", val1, val2, isEqual(val1, val2))
	fmt.Printf("Comparação: %v == %v: %v\n", val1, val3, isEqual(val1, val3))

	// Teste com strings
	str1 := "golang"
	str2 := "golang"
	str3 := "java"

	fmt.Printf("Comparação: %v == %v: %v\n", str1, str2, isEqual(str1, str2))
	fmt.Printf("Comparação: %v == %v: %v\n", str1, str3, isEqual(str1, str3))
}

// Output:
// Comparação: 10 == 10: true
// Comparação: 10 == 20: false
// Comparação: golang == golang: true
// Comparação: golang == java: false
