from abc import abstractmethod

class Conta:
    def __init__(self, conta_id, saldo) -> None:
        self._conta_id: int = conta_id
        self._saldo: float = saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo
    
    def get_conta_id(self):
        return self._conta_id

    def set_conta_id(self, conta_id):
        self._conta_id = conta_id

    @abstractmethod
    def depositar(self, valor_a_ser_depositado):
        pass

    @abstractmethod
    def sacar(self, valor_a_ser_sacado):
        pass