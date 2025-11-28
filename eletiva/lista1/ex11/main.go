package main

import (
	"fmt"
	"time"
)

// 11- Algoritmo de Zeller (calcula dia da semana pela data de nascimento)
func zellerAlgorithm(day, month, year int) string {
	daysOfWeek := []string{"Sábado", "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"}

	// Ajustar mês e ano para o algoritmo de Zeller
	if month < 3 {
		month += 12
		year--
	}

	q := day
	m := month
	k := year % 100
	j := year / 100

	h := (q + (13*(m+1))/5 + k + k/4 + j/4 - 2*j) % 7

	// Zeller retorna 0=Sábado, 1=Domingo, etc.
	return daysOfWeek[h]
}

func main() {
	// Exemplo: 15 de Novembro de 1889 (Proclamação da República)
	day := 15
	month := 11
	year := 1889

	dayOfWeek := zellerAlgorithm(day, month, year)
	fmt.Printf("Data: %02d/%02d/%d\n", day, month, year)
	fmt.Printf("Dia da semana: %s\n", dayOfWeek)

	// Verificação usando time package
	date := time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC)
	fmt.Printf("Verificação: %s\n", date.Weekday())
}

// Output:
// Data: 15/11/1889
// Dia da semana: Sexta
// Verificação: Friday
