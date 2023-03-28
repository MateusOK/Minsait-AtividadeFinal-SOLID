from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

conta1 = ContaPoupanca(conta_id=1, saldo=100, taxa_de_rendimento=10)

print(conta1.verificar_rendimento_ao_ano("1a"))  