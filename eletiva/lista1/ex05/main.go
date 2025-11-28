package main

import "fmt"

// 5- Verificar se um número é primo ou não
func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := 3; i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	testNumbers := []int{2, 7, 10, 13, 15, 17}
	for _, num := range testNumbers {
		if isPrime(num) {
			fmt.Printf("%d é primo\n", num)
		} else {
			fmt.Printf("%d não é primo\n", num)
		}
	}
}

// Output:
// 2 é primo
// 7 é primo
// 10 não é primo
// 13 é primo
// 15 não é primo
// 17 é primo
