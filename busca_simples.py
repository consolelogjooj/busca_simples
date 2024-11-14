TAM = 10

def busca_simples(vetor, valor_procurado):
    for cont in range(TAM):
        if vetor[cont] == valor_procurado:
            return cont  
    return -1 
def main():
    vetor = [1, 23, 34, 45, 56, 67, 78, 89, 90, 100] 
    valor_procurado = int(input("Qual valor deseja encontrar? "))

    # Exibindo meu vetor
    print("Vetor:", " - ".join(map(str, vetor)))

    posicao_encontrada = busca_simples(vetor, valor_procurado)
    if posicao_encontrada != -1:
        print(f"Valor encontrado na posição {posicao_encontrada}")
    else:
        print("Valor não encontrado")

if __name__ == "__main__":
    main()
