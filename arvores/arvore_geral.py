# CP3 - Árvores Gerais - DSA
# Eduardo Moreira Silva - RM 569923

# ---------------------------------------------------------------
# DIAGNÓSTICO INICIAL
# ---------------------------------------------------------------
# 1) Nó x raiz: todo elemento da árvore é um nó (tem um dado e as ligações
#    com os filhos). A raiz é o nó do topo, o único que não tem pai, e é por
#    ela que a árvore é acessada.
# 2) no.esquerda / no.direita: são os dois "ponteiros" da árvore binária,
#    cada um apontando para uma subárvore (ou None quando ela não existe).
# 3) Função recursiva recebe um nó porque cada nó é o começo de uma
#    subárvore menor. Ela trata esse nó e repete o processo nos filhos até
#    receber None.
# 4) O percurso chega em todos os nós porque, a partir da raiz, sempre chama
#    a função para os filhos de cada nó visitado; como todo nó tem um pai,
#    nenhum fica de fora.
# 5) Para cinco filhos, troca esquerda/direita por uma lista (self.filhos).
#    A lista aceita quantos filhos forem necessários.
# ---------------------------------------------------------------


class NoGeral:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

# Não é preciso definir quantos filhos o nó terá porque a lista do Python
# cresce sozinha conforme os appends são feitos.


class ArvoreGeral:
    def __init__(self):
        self.raiz = None

    def criar_raiz(self, dado):
        if self.raiz is not None:
            raise ValueError("A árvore já possui raiz.")
        self.raiz = NoGeral(dado)
        return self.raiz

    def inserir(self, pai, dado):
        # sem regra de comparação: o pai precisa ser informado
        if pai is None:
            raise ValueError("O nó pai não foi informado.")
        novo = NoGeral(dado)
        pai.adicionar_filho(novo)
        return novo

    def pre_ordem(self, no):
        if no is None:
            return
        print(no.dado)
        for filho in no.filhos:
            self.pre_ordem(filho)

    # Continua recursivo mesmo com o for porque o laço só passa pelos filhos
    # diretos; quem desce para os netos, bisnetos etc. é a chamada
    # self.pre_ordem(filho) dentro do laço.

    def mostrar(self, no, nivel=0, recuo="    "):
        if no is None:
            return
        print(recuo * nivel + str(no.dado))
        for filho in no.filhos:
            self.mostrar(filho, nivel + 1, recuo)

    def buscar(self, no, valor):
        if no is None:
            return None
        if no.dado == valor:
            return no
        for filho in no.filhos:
            achou = self.buscar(filho, valor)
            if achou:
                return achou
        return None

    # - Não dá pra usar valor < no.dado porque os nós não seguem ordem
    #   nenhuma; o valor pode estar em qualquer galho.
    # - Se estiver no último ramo, a busca passa por todos os ramos
    #   anteriores primeiro.
    # - Pior caso: O(n), visitando todos os nós.
    # - Com valores repetidos, volta o primeiro achado na pré-ordem.

    def contar_nos(self, no):
        if no is None:
            return 0
        return 1 + sum(self.contar_nos(filho) for filho in no.filhos)

    # O total começa em 1 porque o próprio nó entra na conta; os filhos
    # somam o resto. Uma folha devolve só esse 1.

    def altura(self, no):
        if no is None:
            return 0
        if not no.filhos:
            return 1
        return 1 + max(self.altura(filho) for filho in no.filhos)

    def listar_folhas(self, no):
        if no is None:
            return
        if len(no.filhos) == 0:
            print(no.dado)
            return
        for filho in no.filhos:
            self.listar_folhas(filho)

    # Na binária, folha é quando esquerda e direita são None. Aqui basta a
    # lista de filhos estar vazia.

    def inserir_por_valor(self, valor_pai, dado):
        # depende de nomes únicos; o ideal seria um id para cada nó
        pai = self.buscar(self.raiz, valor_pai)
        if pai is None:
            return None
        return self.inserir(pai, dado)

    # ---------------- desafio ----------------

    def contar_folhas(self, no):
        if no is None:
            return 0
        if not no.filhos:
            return 1
        return sum(self.contar_folhas(filho) for filho in no.filhos)

    def grau_arvore(self, no):
        if no is None:
            return 0
        graus = [len(no.filhos)]
        for filho in no.filhos:
            graus.append(self.grau_arvore(filho))
        return max(graus)


# ======================================================================
# TESTES
# ======================================================================

def checar(nome, obtido, esperado):
    print(f"{'OK  ' if obtido == esperado else 'ERRO'} | {nome}: {obtido} (esperado {esperado})")


def montar_arvore_tutorial():
    arvore = ArvoreGeral()
    instituicao = arvore.criar_raiz("Instituição")
    graduacao = arvore.inserir(instituicao, "Graduação")
    pos = arvore.inserir(instituicao, "Pós-graduação")
    arvore.inserir(graduacao, "Ciência da Computação")
    arvore.inserir(graduacao, "Sistemas de Informação")
    arvore.inserir(pos, "Mestrado")
    arvore.inserir_por_valor("Graduação", "Engenharia de Software")
    return arvore


arvore = montar_arvore_tutorial()

print("HIERARQUIA:")
arvore.mostrar(arvore.raiz)
print("\nHIERARQUIA COM HÍFENS:")
arvore.mostrar(arvore.raiz, recuo="--")
print("\nPRÉ-ORDEM:")
arvore.pre_ordem(arvore.raiz)
print("\nFOLHAS:")
arvore.listar_folhas(arvore.raiz)

print("\nVALIDAÇÃO:")
checar("Total de nós", arvore.contar_nos(arvore.raiz), 7)
checar("Altura", arvore.altura(arvore.raiz), 3)
checar("Filhos da raiz", len(arvore.raiz.filhos), 2)
checar("Filhos de Graduação", len(arvore.buscar(arvore.raiz, "Graduação").filhos), 3)
checar("Busca Mestrado", arvore.buscar(arvore.raiz, "Mestrado") is not None, True)
checar("Busca Doutorado", arvore.buscar(arvore.raiz, "Doutorado") is not None, False)
checar("Folhas", arvore.contar_folhas(arvore.raiz), 4)

total_antes = arvore.contar_nos(arvore.raiz)
checar("Pai inexistente", arvore.inserir_por_valor("Doutorado", "X"), None)
checar("Árvore sem mudança", arvore.contar_nos(arvore.raiz), total_antes)

print("\nCASOS ESPECIAIS:")
vazia = ArvoreGeral()
checar("Vazia - nós", vazia.contar_nos(vazia.raiz), 0)
checar("Vazia - altura", vazia.altura(vazia.raiz), 0)
checar("Vazia - busca", vazia.buscar(vazia.raiz, "X"), None)
unica = ArvoreGeral()
unica.criar_raiz("Raiz")
checar("Só raiz - nós", unica.contar_nos(unica.raiz), 1)
checar("Só raiz - altura", unica.altura(unica.raiz), 1)
checar("Só raiz - folhas", unica.contar_folhas(unica.raiz), 1)

print("\nDESAFIO - ESTRUTURA AMPLIADA:")
ampliada = ArvoreGeral()
raiz = ampliada.criar_raiz("Instituição")
setores = {
    "Graduação": ["Ciência da Computação", "Sistemas de Informação", "Engenharia de Software"],
    "Pós-graduação": ["Especialização", "Mestrado"],
    "Administração": ["Secretaria", "Biblioteca"],
}
for setor, itens in setores.items():
    no_setor = ampliada.inserir(raiz, setor)
    for item in itens:
        ampliada.inserir(no_setor, item)
ampliada.mostrar(ampliada.raiz)
# o enunciado fala em 10 nós, mas o desenho tem 11 elementos
checar("Nós", ampliada.contar_nos(ampliada.raiz), 11)
checar("Altura", ampliada.altura(ampliada.raiz), 3)
checar("Folhas", ampliada.contar_folhas(ampliada.raiz), 7)
checar("Grau", ampliada.grau_arvore(ampliada.raiz), 3)
