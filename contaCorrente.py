from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, conta_id: int, saldo: float, limite: float) -> None:
        super().__init__(conta_id, saldo)
        self.limite = limite

    def depositar(self, valor_a_ser_depositado):
        self._saldo += valor_a_ser_depositado
    
    def sacar(self, valor_a_ser_sacado):
        if valor_a_ser_sacado > self._saldo + self.limite:
            raise ValueError("Valor a ser sacado não pode ser maior que saldo e limite juntos")
        else:
            self._saldo -= valor_a_ser_sacado

