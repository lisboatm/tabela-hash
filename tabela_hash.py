def hash_table(M, keys):
    # Inicializar a tabela hash como uma lista de listas vazias
    table = [[] for _ in range(M)]
    
    # Inserir cada chave na tabela usando a função de dispersão
    for key in keys:
        index = key % M
        table[index].append(key)
    
    # Exibir a tabela resultante
    result = []
    for i in range(M):
        if table[i]:
            result.append(f"{i} -> {' -> '.join(map(str, table[i]))} -> \\")
        else:
            result.append(f"{i} -> \\")
    return result

def main():
    N = int(input())
    first_case = True  # Flag para gerenciar a linha em branco entre os casos

    for _ in range(N):
        M, C = map(int, input().split())
        keys = list(map(int, input().split()))
        
        if not first_case:
            print()  # Imprime uma linha em branco entre os casos de teste
        first_case = False
        
        # Imprimir o resultado do hash_table
        result = hash_table(M, keys)
        for line in result:
            print(line)

if __name__ == "__main__":
    main()
