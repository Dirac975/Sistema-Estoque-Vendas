class Mercadoria:

    def __init__(self, nome, tipo, preco, estoque):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.estoque = estoque

    def exibir_informacoes(self):
        print(f"\nProduto {self.nome} | Tipo {self.tipo} | Preço R${self.preco:.2f} | Quanto em estoque {self.estoque}")    

estoque_loja = []
faturamento_total = 0.0

def cadastras_produto():
    print("\n==== Cadastro de Mercadorias ====")
    nome_user = input("Nome do produto: ")
    tipo_user= input("Tipo/Categoria do produto: ")
    preco_user = float(input("Preço do produto: R$ "))
    estoque_user = int(input("Quantidade em estoque: "))

    novo_produto = Mercadoria(nome_user, tipo_user, preco_user, estoque_user)
    estoque_loja.append(novo_produto)
    if len(estoque_loja) == 0:
        print("Nenhum produto em estoque")
    else:
        for produto in estoque_loja:
            produto.exibir_informacoes()

def estoque():
    print("\n==== Produtos em Estoque ====")
    if len(estoque_loja) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in estoque_loja:
            produto.exibir_informacoes()

def realizar_venda():
    global faturamento_total

    print("\n==== Simulação de Venda ====")
    if len(estoque_loja) == 0:
        print("Não há produtos no estoque para vender.")
        return
    
    nome_busca = input("Digite o nome do produto que deseja vender: ")

    produto_encontrado = None
    for produto in estoque_loja:
        if produto.nome.lower() == nome_busca.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("[Erro] Produto não encontrado no sistema.")
    else:
        quantidade_venda = int(input(f"Quantas unidades de {produto_encontrado.nome} deseja vender? "))


        if quantidade_venda <= produto_encontrado.estoque:
            produto_encontrado.estoque -= quantidade_venda
            valor_renda = quantidade_venda * produto_encontrado.preco
            faturamento_total += valor_renda
            print(f"\n[Venda Concluída] {quantidade_venda}x {produto_encontrado.nome} vendidos!")
            print(f"\n[Erro] Estoque insuficiente! Você só tem {produto_encontrado.estoque} unidades")


def exibir_caixa():
    print("\n==== Relatório Comercial ====")
    print(f"Faturamento Total Acumulado: R$ {faturamento_total:.2f}")
    total_itens = sum(p.estoque for p in estoque_loja)
    print(f"Total de mercadoria físicas em estoque: {total_itens} unidades.")


while True:
    print("\n==== Sistema de Estoque e Vendas v2.0 ====")
    print("1 - Cadastro de Mercadoria")
    print("2 - Estoque")
    print("3 - Realizar Venda")
    print("4 - Ver Relatório Financeiro")
    print("5 - Sair")

    opcao = input("Escolha um opção: ")

    match opcao:
        case "1":
            cadastras_produto()
        case "2":
            estoque()
        case "3":
            realizar_venda()
        case "4":
            exibir_caixa()
        case "5":
            print("\nFechando o sistema. Até logo!")
            break
        case _:
            print("\nOpção inválida. Selecione de 1 a 5")