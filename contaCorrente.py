from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, conta_id: int, saldo: float, limite: float) -> None:
        super().__init__(conta_id, saldo)
        self.limite = limite

    def depositar(self, valor_a_ser_depositado: float):
        self._saldo += valor_a_ser_depositado
    
    def sacar(self, valor_a_ser_sacado: float):
        if valor_a_ser_sacado > self._saldo + self.limite:
            raise ValueError("Valor a ser sacado não pode ser maior que saldo e limite somados") #Caso o valor a ser sacado seja maior que o limite e saldo juntos uma Exception do tipo ValueError é jogada
        else:
            self._saldo -= valor_a_ser_sacado
    
    def verificar_saldo(self):
        print("Saldo atual: ", self._saldo)

    def verificar_limite(self):
        print("Seu limite é: ", self.limite)

