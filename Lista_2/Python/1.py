def anoMaisPopuloso(B, D):
    ano_min = min(B)
    ano_max = max(D) # a faixa de pessoas vivas está entre esses anos
    anos = [0] * (ano_max - ano_min + 1) # lista com quantidade de todos os anos que podem estar vivas

    for i in range(len(B)):
        for ano in range(B[i] - ano_min, D[i] - ano_min + 1):
            anos[ano] += 1 # incrementa em 1 sempre que a pessoa estiver viva no respectivo ano

    max_pessoas_vivas = max(anos) # pega o maior valor de anos (+ num de pessoas vivas)
    max_ano_pessoas_vivas = anos.index(max_pessoas_vivas) + ano_min # pega o index desse valor e adiciona ao menor ano possível de alguem estar vivo
    return max_ano_pessoas_vivas

nascimento = [2000, 2002, 2003, 2003, 2005]
morte = [2010, 2010, 2006, 2010, 2009]

print(anoMaisPopuloso(nascimento, morte))

# a complexidade deste algoritmo é O(n + k), onde k é a diferença entre o menor e o maior valor dos vetores B e D
# sua complexidade de espaço é O(k), visto que aloca um vetor do tamanho da diferença entre o menor e o maior valor de B e D
