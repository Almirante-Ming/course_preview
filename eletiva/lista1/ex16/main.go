package main

import "fmt"

// 16- Algoritmo que faça conversão de unidades de temperatura
func celsiusToFahrenheit(celsius float64) float64 {
	return (celsius * 9 / 5) + 32
}

func fahrenheitToCelsius(fahrenheit float64) float64 {
	return (fahrenheit - 32) * 5 / 9
}

func celsiusToKelvin(celsius float64) float64 {
	return celsius + 273.15
}

func kelvinToCelsius(kelvin float64) float64 {
	return kelvin - 273.15
}

func main() {
	celsius := 25.0

	fahrenheit := celsiusToFahrenheit(celsius)
	kelvin := celsiusToKelvin(celsius)

	fmt.Printf("Temperatura: %.2f°C\n", celsius)
	fmt.Printf("Em Fahrenheit: %.2f°F\n", fahrenheit)
	fmt.Printf("Em Kelvin: %.2f K\n", kelvin)

	// Conversão inversa
	fmt.Printf("\nConversão inversa:\n")
	fmt.Printf("%.2f°F em Celsius: %.2f°C\n", fahrenheit, fahrenheitToCelsius(fahrenheit))
	fmt.Printf("%.2f K em Celsius: %.2f°C\n", kelvin, kelvinToCelsius(kelvin))
}

// Output:
// Temperatura: 25.00°C
// Em Fahrenheit: 77.00°F
// Em Kelvin: 298.15 K
//
// Conversão inversa:
// 77.00°F em Celsius: 25.00°C
// 298.15 K em Celsius: 25.00°C
