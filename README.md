# Desafio I - Tabelas Hash com Encadeamento Exterior

## Descrição do Problema

As **tabelas Hash** (também conhecidas como **tabelas de dispersão**) são estruturas de dados que armazenam elementos com base no valor das suas chaves, utilizando técnicas de **tratamento de colisões**. 

Neste problema, a tabela hash usa uma **função de dispersão** (`h(x) = x % M`) para calcular o endereço onde uma chave deve ser armazenada. Se houver colisão (isto é, duas ou mais chaves são mapeadas para o mesmo endereço), a tabela utiliza um **encadeamento externo** para resolver o conflito, armazenando as chaves em uma lista.

### Exemplo Explicativo
Se a tabela hash tem 13 endereços (de 0 a 12) e queremos armazenar as seguintes chaves:

```
44, 45, 49, 70, 27, 73, 92, 97, 95
```

A função de dispersão `h(x) = x % 13` mapeia:
- `44 % 13 = 5`
- `45 % 13 = 6`
- `49 % 13 = 10`

Assim, a tabela resultante seria:
```
5 -> 44 -> \
6 -> 45 -> \
10 -> 49 -> \
```

## Entrada

A entrada contém vários casos de teste:

1. A **primeira linha** contém um inteiro `N` que indica a quantidade de casos de teste.
2. Para cada caso de teste:
   - A **primeira linha** contém dois inteiros `M` e `C`, onde:
     - `M` é o número de endereços na tabela hash.
     - `C` é a quantidade de chaves a serem inseridas.
   - A **segunda linha** contém `C` inteiros, representando as chaves que devem ser inseridas na tabela.

### Restrições
- `1 ≤ N ≤ 100` (casos de teste)
- `1 ≤ M ≤ 100` (endereços na tabela)
- `1 ≤ C ≤ 200` (chaves a serem inseridas)
- `1 ≤ x ≤ 200` (valor das chaves)

## Saída

Para cada caso de teste, você deve imprimir:
- Para cada índice da tabela (0 a `M-1`):
  - O índice seguido pelos valores encadeados (se houver) separados por `->`, terminando com `\`.
- Uma **linha em branco** deve separar os casos de teste.

### Exemplo de Entrada
```
2
13 9
44 45 49 70 27 73 92 97 95
7 8
35 12 2 17 19 51 88 86
```

### Exemplo de Saída
```
0 -> \
1 -> 27 -> 92 -> \
2 -> \
3 -> \
4 -> 95 -> \
5 -> 44 -> 70 -> \
6 -> 45 -> 97 -> \
7 -> \
8 -> 73 -> \
9 -> \
10 -> 49 -> \
11 -> \
12 -> \

0 -> 35 -> \
1 -> \
2 -> 2 -> 51 -> 86 -> \
3 -> 17 -> \
4 -> 88 -> \
5 -> 12 -> 19 -> \
6 -> \
```

## Explicação do Exemplo
No primeiro caso:
- Usando `M = 13` e a função `h(x) = x % 13`, as chaves são mapeadas para os seguintes índices:
  - `44 % 13 = 5`, então `44` vai para o índice `5`.
  - `45 % 13 = 6`, então `45` vai para o índice `6`.
  - `49 % 13 = 10`, então `49` vai para o índice `10`, e assim por diante.

No segundo caso:
- Usando `M = 7`:
  - `35 % 7 = 0`, então `35` vai para o índice `0`.
  - `12 % 7 = 5`, então `12` vai para o índice `5`, e assim por diante.

## Solução em Python

```python
def hash_table(M, keys):
    # Inicializar a tabela hash como uma lista de listas vazias
    table = [[] for _ in range(M)]
    
    # Inserir cada chave na tabela usando a função de dispersão
    for key in keys:
        index = key % M
        table[index].append(key)
    
    # Gerar a saída formatada
    result = []
    for i in range(M):
        if table[i]:
            result.append(f"{i} -> {' -> '.join(map(str, table[i]))} -> \\")
        else:
            result.append(f"{i} -> \\")
    return result

def main():
    N = int(input())
    first_case = True

    for _ in range(N):
        M, C = map(int, input().split())
        keys = list(map(int, input().split()))
        
        if not first_case:
            print()  # Linha em branco entre casos de teste
        first_case = False
        
        result = hash_table(M, keys)
        for line in result:
            print(line)

if __name__ == "__main__":
    main()
```

### Como Funciona o Código
1. **Função `hash_table()`**:
   - Inicializa uma tabela com `M` endereços (listas vazias).
   - Para cada chave, calcula o índice usando `key % M` e insere a chave na lista correspondente.
   - Gera uma lista de strings formatada para cada índice.

2. **Função `main()`**:
   - Lê o número de casos de teste.
   - Para cada caso, lê os valores `M` e `C`, e as chaves.
   - Chama a função `hash_table()` para gerar o resultado e imprime.

## Como Executar
Salve o código em um arquivo chamado `tabela_hash.py` e execute com:
```bash
python3 tabela_hash.py
```

## Possíveis Erros
- **Presentation Error**: Verifique se a linha em branco entre os casos está sendo impressa corretamente.
- **Runtime Error**: Certifique-se de que todas as entradas estejam corretas.

## Dicas Finais
- Teste com entradas grandes para garantir que o programa seja eficiente.
- Preste atenção à formatação da saída, pois erros de formatação podem resultar em "Presentation Error".
