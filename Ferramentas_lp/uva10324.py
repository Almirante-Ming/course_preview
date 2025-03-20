# # recebe a string e transforma em uma lista de inteiros
# # recebe a quantidade de cases
# # entra em um loop que recebe i e j, sao indices do array, se repete  pelo numero de cases
# # imprime Yes casos os valores sao iguais, caso contrario imprime No

def process_case(binary_string, queries):
    results=[]
    for i, j in queries:
        start, end = min(i, j), max(i, j)
        
        if binary_string[start:end+1] == binary_string[start] * (end - start + 1):
            results.append("Yes")
        else:
            results.append("No")
    
    return results

def main():
    case_number = 1
    while True:
        binary_string = input().strip()
        if not binary_string:
            break
        
        n = int(input().strip())
        
        queries = []
        for _ in range(n):
            i, j = map(int, input().strip().split())
            queries.append((i, j))
        
        results = process_case(binary_string, queries)
        
        print(f"Case {case_number}:")
        for result in results:
            print(result)
        
        case_number += 1

if __name__ == "__main__":
    main()