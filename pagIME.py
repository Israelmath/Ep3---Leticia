import numpy as np

class Paguime:

    def __init__(self, saldoInicial):
        self.saldo = np.array(saldoInicial)
        self.coeficientes = [0 for v in self.saldo]

    def pague(self, valor):
        self.resetCoefs()
        pagamento = []
        for indice in range(0, len(self.saldo)):
            self.coeficientes[indice] = self.combLinRecursiva(valor, indice)
            pagamento.append([self.saldo[indice][0], self.coeficientes[indice]])
        if self.prodMatrix() < valor:
            return None

        self.subFCoins()
        return np.array(pagamento)

    def combLinRecursiva(self, valor, indice):
        self.coeficientes[indice] += 1
        resp = self.prodMatrix()
        if resp == valor:
            return self.coeficientes[indice]
        if resp > valor or self.coeficientes[indice] > self.saldo[indice][1]:
            self.coeficientes[indice] -= 1
            return self.coeficientes[indice]
        else:
            return self.combLinRecursiva(valor, indice)

    def subFCoins(self):
        indice = 0
        for fcoin in self.coeficientes:
            self.saldo[indice][1] -= fcoin
            indice += 1

    def resetCoefs(self):
        self.coeficientes = [0 for v in self.saldo]

    def prodMatrix(self):
        fvalores = np.array([fvalor[0] for fvalor in self.saldo])
        return np.matmul(fvalores, self.coeficientes)

    def __str__(self):
        stringReturn = 'O saldo da máquina é:\n'
        for fvalor, fcoin in self.saldo:
            stringReturn = stringReturn + f'{fcoin} fcoins de {fvalor} Frogs\n'
        return stringReturn


def main():
    saldoInicial = np.array([[9, 2], [5, 2], [3, 2], [2, 2], [1, 2]])
    maq = Paguime(saldoInicial)
    print(maq)
    maq.prodMatrix()

    for v in range(0, 20, 3):
        print('')
        pag = maq.pague(v)
        if pag is None:
            print(f'Não consegui pagar {v}')
        else:
            print(f'Paguei {v} usando:')
            print(pag)
            print(maq)


if __name__ == '__main__':
    main()