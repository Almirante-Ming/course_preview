package main

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/glebarez/sqlite"
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
		panic(err)
	}

	db.AutoMigrate(&Pessoa{})

	r := gin.Default()
	r.LoadHTMLGlob("templates/*")

	r.GET("/", func(c *gin.Context) {
		var pessoas []Pessoa
		db.Order("id asc").Find(&pessoas)
		c.HTML(http.StatusOK, "index.html", gin.H{
			"pessoas": pessoas,
		})
	})

	r.GET("/novo", func(c *gin.Context) {
		c.HTML(http.StatusOK, "form.html", gin.H{
			"pessoa": Pessoa{},
		})
	})

	r.GET("/editar/:id", func(c *gin.Context) {
		id, err := strconv.Atoi(c.Param("id"))
		if err != nil {
			c.String(http.StatusBadRequest, "ID inválido")
			return
		}

		var pessoa Pessoa
		if err := db.First(&pessoa, id).Error; err != nil {
			c.String(http.StatusNotFound, "Pessoa não encontrada")
			return
		}

		c.HTML(http.StatusOK, "form.html", gin.H{
			"pessoa": pessoa,
		})
	})

	r.POST("/salvar", func(c *gin.Context) {
		var payload struct {
			ID   uint   `json:"id" form:"id"`
			Name string `json:"name" form:"name"`
			Age  int    `json:"age" form:"age"`
			City string `json:"city" form:"city"`
		}

		if err := c.ShouldBind(&payload); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Dados inválidos"})
			return
		}

		if payload.ID == 0 {
			p := Pessoa{Name: payload.Name, Age: payload.Age, City: payload.City}
			db.Create(&p)

			if c.ContentType() == "application/json" {
				c.JSON(http.StatusCreated, p)
			} else {
				c.Redirect(http.StatusFound, "/")
			}
			return
		}

		var p Pessoa
		if err := db.First(&p, payload.ID).Error; err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": "Pessoa não encontrada"})
			return
		}

		p.Name = payload.Name
		p.Age = payload.Age
		p.City = payload.City
		db.Save(&p)

		if c.ContentType() == "application/json" {
			c.JSON(http.StatusOK, p)
		} else {
			c.Redirect(http.StatusFound, "/")
		}
	})

	r.GET("/deletar/:id", func(c *gin.Context) {
		id, err := strconv.Atoi(c.Param("id"))
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "ID inválido"})
			return
		}

		result := db.Delete(&Pessoa{}, id)
		if result.RowsAffected == 0 {
			c.JSON(http.StatusNotFound, gin.H{"error": "Pessoa não encontrada"})
			return
		}

		// Retorna JSON para a requisição AJAX e HTML para requisição normal
		if c.GetBool("wants_json") {
			c.JSON(http.StatusOK, gin.H{"ok": true, "deleted_id": id})
		} else {
			c.JSON(http.StatusOK, gin.H{"ok": true, "deleted_id": id})
		}
	})

	r.Run(":8080")
}
