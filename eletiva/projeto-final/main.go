package main

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type Pessoa struct {
	gorm.Model
	Name string
	Age  int
	City string
}

func main() {
	db, err := gorm.Open(sqlite.Open("inventario.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&Pessoa{})

	db.Create(&Pessoa{Name: "Victor Guilhrme", Age: 24, City: "Tres Lagoas"})

}
