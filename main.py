from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

contaPoupanca = ContaPoupanca(conta_id=1, saldo=100, taxa_de_rendimento=10)
contaCorrente = ContaCorrente(conta_id=2, saldo=200, limite=1500)


#TESTES VERIFICAR RENDIMENTO AO ANO
print("Saldo após 1 segundo de rendimento: ", contaPoupanca.verificar_rendimento_ao_ano("1s")) #Verificação de qual seria o saldo após 1 segundo rendendo com uma taxa de 10% ao ano
print("Saldo após de 25.3 minutos de rendimento: ", contaPoupanca.verificar_rendimento_ao_ano("25.3min"))#Verificação com 25.3 minutos de rendimento
print("Saldo após de 3 dias de rendimento: ", contaPoupanca.verificar_rendimento_ao_ano("3D"))#Verificação com 3 dias (D maiusculo para testar se ocorrerá erro)
print("Saldo após de 5 semanas de rendimento: ", contaPoupanca.verificar_rendimento_ao_ano("5w"))
print("Saldo após de 7 meses de rendimento: ", contaPoupanca.verificar_rendimento_ao_ano("7m"))
print("Saldo após de 2 anos de rendimento: ", contaPoupanca.verificar_rendimento_ao_ano("2a"))
print("-----------------------------------------")

#TESTE DEPOSITO
contaCorrente.verificar_saldo() #Verificando saldo da conta
contaCorrente.depositar(200) #Depositando 200 na conta
contaCorrente.verificar_saldo() #Verificando saldo da conta após o depósito
print("-----------------------------------------")

#TESTE SAQUE
contaPoupanca.verificar_saldo() #Verificando saldo da conta
contaPoupanca.sacar(70) #Sacando 70 da conta
contaPoupanca.verificar_saldo()#Saldo após saque de 70

#TESTE EXCEPTION VALUEERROR
contaCorrente.verificar_saldo() #Verificando saldo
contaCorrente.verificar_limite() #Verificando limite da conta
contaCorrente.sacar(2000) #Saque maior que saldo e limites somados, Exception deve ser lançada