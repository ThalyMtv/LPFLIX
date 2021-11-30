'''
Amanda
Talita

Faça um programa em Python para controlar os filmes/séries assistidos por uma pessoa:
Para isso crie um dicionário para armazenar o título do filme/série, ano de lançamento, resumo, gênero (romance, drama, suspense etc), avaliação (se gostou ou não).
Permita ao usuário escolher as seguintes opções:
• a inserção de um novo filme/série
• consulta a um determinado filme/série
• a listagem de todos os filmes/séries
• a listagem de todos os filmes/séries de um determinado gênero
'''

Generos = ['AÇÃO', 'AVENTURA', 'COMÉDIA', 'DRAMA', 'DOCUMENTÁRIO', 'FANTASIA', 'FICÇÃO', 'GUERRA', 'ROMANCE', 'SUSPENSE', 'TERROR']

def cadastraTitulo():
    faixa("CADASTRO DO FILME/SÉRIE")
    Titulo.clear()
    print("Informe os dados do Título assistido")
    Titulo['Nome'] = input("Nome do Título -> ").upper()
    while True:
        Titulo['Tipo'] = input("Filme ou Série? -> ").upper()
        if Titulo['Tipo'] == 'Filme'.upper() or Titulo['Tipo'] == 'Série'.upper() or Titulo['Tipo'] == 'Serie'.upper():
            break
        else:
            print("Por gentileza digite apenas 'Filme' ou Série'")
    Titulo['Lancamento'] = int(input("Ano de Lançamento -> "))
    Titulo['Sinopse'] = input("Sinopse: -> ").upper()
    while True:
        print("Gênero: >> \n1. Ação,\n2. Aventura,\n3. Comédia,\n4. Drama,\n5. Documentário,\n6. Fantasia,\n7. Ficção,\n8. Guerra,\n9. Romance,\n10. Suspense,\n11. Terror")
        TitGen = int(input("Gênero: -> "))
        TitGen = TitGen-1
        if TitGen in range(len(Generos)):
            Titulo['Gênero'] = Generos[TitGen].upper()
            break
        else:
            print("Gênero não encontrado")
    Titulo['Opinião'] = input("Gostou?[S/N]: -> ").upper()
    playList.append(Titulo.copy())
    print("Cadastro realizado com sucesso!!")




def consulta():
    faixa("CONSULTA")
    achou = False
    nomeTitulo = input("Nome do Filme/Série para consulta -> ").upper()
    for T in playList:
        if T['Nome'] == nomeTitulo:
            achou = True
            print()
            print("Título encontrado!!")
            print()
            print(f"\n Título: {T['Nome']}\n Estilo: {T['Tipo']}\n Ano de Lançamento: {T['Lancamento']}\n Sinopse: {T['Sinopse']}\n Gênero: {T['Gênero']}\n Gostou?: {T['Opinião']} ")
    if not achou:
        print()
        print("Título não encontrado!!")
        print()


def listagem():
    faixa("TODOS OS ASSISTIDOS")
    for T in playList:
        for chave, valor in T.items():
            print(f"{chave} -> {valor}")
        print('-' * 50)


def listagemGen():
    faixa("ASSISTIDOS >> LISTAGEM POR GÊNERO")
    achougen = False
    print("Escolha o Gênero: >> \n1. Ação,\n2. Aventura,\n3. Comédia,\n4. Drama,\n5. Documentário,\n6. Fantasia,\n7. Ficção,\n8. Guerra,\n9. Romance,\n10. Suspense,\n11. Terror")
    GenT = int(input("Opção >> "))
    GenT2 = GenT-1
    if GenT2 in range(len(Generos)):
        Ttl = Generos[GenT2]
        print(f"\nTítulos do Gênero {Ttl}!!")
        for T in playList:
            if T['Gênero'] == Ttl:
                achougen = True
                print("-" * 50)
                print(f"\n Título: {T['Nome']}\n Estilo: {T['Tipo']}\n Ano de Lançamento: {T['Lancamento']}\n Sinopse: {T['Sinopse']}\n Gênero: {T['Gênero']}\n Sua Opinião: {T['Opinião']} ")
        if not achougen:
            print("\nNenhum Encontrado!!")
            print()



def faixa(texto):
    print("=" * 50)
    print(f"{texto.upper()}".center(50))
    print("=" * 50)


playList = []
Titulo = {}

while True:
    faixa("MY FILMLIST - FILMES E SÉRIES")
    op = int(input("1. Cadastro\n2. Consultar"
                   "\n3. Listar Todos\n4. Listar por gênero\n5. Sair\nOpção -> "))
    if op == 5:
        break
    elif op == 1:
        cadastraTitulo()
    elif op == 2:
        consulta()
    elif op == 3:
        listagem()
    elif op == 4:
        listagemGen()
    else:
        print("Opção inválida!!!")