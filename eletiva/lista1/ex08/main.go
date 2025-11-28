package main

import "fmt"

// 8- Árvore baseada em sequência de respostas (Árvore de Decisão Binária)
type Node struct {
	question string
	yes      *Node
	no       *Node
	answer   string
}

func createTree() *Node {
	return &Node{
		question: "É um animal?",
		yes: &Node{
			question: "Tem 4 patas?",
			yes: &Node{
				answer: "Cachorro",
			},
			no: &Node{
				answer: "Passaro",
			},
		},
		no: &Node{
			answer: "Objeto inanimado",
		},
	}
}

func askQuestion(node *Node) string {
	if node.answer != "" {
		return node.answer
	}

	fmt.Println(node.question)
	var response string
	fmt.Scanln(&response)

	if response == "s" || response == "S" {
		return askQuestion(node.yes)
	}
	return askQuestion(node.no)
}

func main() {
	tree := createTree()
	fmt.Println("Pense em algo...")
	fmt.Println("Responda com s ou n")
	result := askQuestion(tree)
	fmt.Printf("Você estava pensando em: %s\n", result)
}

// Output:
// Pense em algo...
// Responda com s ou n
// É um animal?
// s
// Tem 4 patas?
// s
// Você estava pensando em: Cachorro
