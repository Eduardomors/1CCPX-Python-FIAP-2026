# BST e AVL - DSA
# Eduardo Moreira Silva - RM 569923
#
# BST: menores à esquerda, maiores à direita (regra estrita).
# Mínimo = nó mais à esquerda | Máximo = nó mais à direita.
# A busca pelo extremo para quando não há filho na direção procurada,
# mesmo que exista filho do outro lado.


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        # inserção iterativa: desce comparando até achar uma posição vazia
        novo = No(dado)
        if self.raiz is None:
            self.raiz = novo
            return
        atual = self.raiz
        while True:
            if dado == atual.dado:
                return  # não aceita repetidos
            if dado < atual.dado:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita

    def buscar(self, valor):
        atual = self.raiz
        while atual is not None and atual.dado != valor:
            if valor < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return atual

    def minimo(self, no=None):
        if self.raiz is None:
            return None
        no = no or self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.dado

    def maximo(self, no=None):
        if self.raiz is None:
            return None
        no = no or self.raiz
        while no.direita:
            no = no.direita
        return no.dado

    def em_ordem(self, no, saida):
        if no:
            self.em_ordem(no.esquerda, saida)
            saida.append(no.dado)
            self.em_ordem(no.direita, saida)
        return saida

    def pre_ordem(self, no, saida):
        if no:
            saida.append(no.dado)
            self.pre_ordem(no.esquerda, saida)
            self.pre_ordem(no.direita, saida)
        return saida

    def pos_ordem(self, no, saida):
        if no:
            self.pos_ordem(no.esquerda, saida)
            self.pos_ordem(no.direita, saida)
            saida.append(no.dado)
        return saida

    def altura(self, no):
        if no is None:
            return 0
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))


# ======================================================================
# AVL
# ======================================================================
# FB = altura da esquerda - altura da direita (precisa ficar entre -1 e 1)
# LL -> gira à direita | RR -> gira à esquerda
# LR -> gira o filho à esquerda e depois o nó à direita
# RL -> gira o filho à direita e depois o nó à esquerda


class NoAVL:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1


def h(no):
    return no.altura if no else 0


def calcular_fb(no):
    return h(no.esquerda) - h(no.direita) if no else 0


def recalcular(no):
    no.altura = max(h(no.esquerda), h(no.direita)) + 1


class AVL:
    def __init__(self):
        self.raiz = None
        self.casos = []

    def girar_direita(self, no):
        nova_raiz = no.esquerda
        no.esquerda = nova_raiz.direita
        nova_raiz.direita = no
        recalcular(no)
        recalcular(nova_raiz)
        return nova_raiz

    def girar_esquerda(self, no):
        nova_raiz = no.direita
        no.direita = nova_raiz.esquerda
        nova_raiz.esquerda = no
        recalcular(no)
        recalcular(nova_raiz)
        return nova_raiz

    def inserir(self, dado):
        self.raiz = self._inserir(self.raiz, dado)

    def _inserir(self, no, dado):
        if no is None:
            return NoAVL(dado)
        if dado < no.dado:
            no.esquerda = self._inserir(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self._inserir(no.direita, dado)
        else:
            return no

        recalcular(no)
        return self.balancear(no)

    def balancear(self, no):
        fb = calcular_fb(no)
        if fb > 1:
            if calcular_fb(no.esquerda) < 0:
                self.casos.append("LR")
                no.esquerda = self.girar_esquerda(no.esquerda)
            else:
                self.casos.append("LL")
            return self.girar_direita(no)
        if fb < -1:
            if calcular_fb(no.direita) > 0:
                self.casos.append("RL")
                no.direita = self.girar_direita(no.direita)
            else:
                self.casos.append("RR")
            return self.girar_esquerda(no)
        return no

    def em_ordem(self, no, saida):
        if no:
            self.em_ordem(no.esquerda, saida)
            saida.append(no.dado)
            self.em_ordem(no.direita, saida)
        return saida

    def exibir(self, no, nivel=0, lado=""):
        if no is None:
            return
        print(f"{'      ' * nivel}{lado}{no.dado}  [altura {no.altura} | FB {calcular_fb(no)}]")
        self.exibir(no.esquerda, nivel + 1, "E-> ")
        self.exibir(no.direita, nivel + 1, "D-> ")

    def esta_balanceada(self, no):
        if no is None:
            return True
        return (-1 <= calcular_fb(no) <= 1
                and self.esta_balanceada(no.esquerda)
                and self.esta_balanceada(no.direita))


# Por que a AVL continua rápida com inserções em ordem crescente?
# Porque cada inserção recalcula a altura e o FB no caminho de volta. Quando
# o lado direito fica pesado demais (FB -2) acontece uma rotação, o nó do meio
# sobe e a altura fica perto de log(n). Uma BST comum viraria uma fila.


def testar_bst():
    print("----- BST -----")
    bst = BST()
    for v in [45, 25, 70, 12, 33, 58, 90, 5, 40, 64]:
        bst.inserir(v)
    print("Em ordem:", bst.em_ordem(bst.raiz, []))
    print("Pré-ordem:", bst.pre_ordem(bst.raiz, []))
    print("Pós-ordem:", bst.pos_ordem(bst.raiz, []))
    print("Mínimo:", bst.minimo(), "| Máximo:", bst.maximo())
    print("Mínimo da subárvore 70:", bst.minimo(bst.buscar(70)))
    print("Máximo da subárvore 25:", bst.maximo(bst.buscar(25)))
    print("Altura:", bst.altura(bst.raiz))
    print("Buscar 33:", "achou" if bst.buscar(33) else "não achou")
    print("Buscar 34:", "achou" if bst.buscar(34) else "não achou")


def testar_avl():
    print("\n----- AVL: testes de calibração -----")
    for sequencia, caso in [([30, 20, 10], "LL"), ([10, 20, 30], "RR"),
                            ([30, 10, 20], "LR"), ([10, 30, 20], "RL")]:
        avl = AVL()
        for v in sequencia:
            avl.inserir(v)
        ok = avl.casos == [caso] and avl.raiz.dado == 20
        print(f"{sequencia} -> {avl.casos} esperado {caso}: {'OK' if ok else 'ERRO'}")

    print("\n----- AVL: estresse 10, 20, 25, 30, 40, 50 -----")
    avl = AVL()
    for v in [10, 20, 25, 30, 40, 50]:
        avl.inserir(v)
    avl.exibir(avl.raiz)
    print("Em ordem:", avl.em_ordem(avl.raiz, []))
    print("Balanceada:", avl.esta_balanceada(avl.raiz))

    print("\n----- BST comum x AVL (1 a 7 em ordem) -----")
    bst, avl = BST(), AVL()
    for v in range(1, 8):
        bst.inserir(v)
        avl.inserir(v)
    print("Altura BST:", bst.altura(bst.raiz), "| Altura AVL:", avl.raiz.altura)


testar_bst()
testar_avl()
