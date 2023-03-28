from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, conta_id: int, saldo: float, taxa_de_rendimento: float) -> None:
        super().__init__(conta_id, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento

    def depositar(self, valor_a_ser_depositado):
        self._saldo += valor_a_ser_depositado

    def sacar(self, valor_a_ser_sacado):
        self._saldo - + valor_a_ser_sacado


    def verificar_rendimento_ao_ano(self, tempo_de_rendimento):
        unidades_de_tempo = {
            's': 31536000,   # segundos em um ano
            'min': 525600,   # minutos em um ano
            'h': 8760,       # horas em um ano
            'd': 365,        # dias em um ano
            'w': 52,         # semanas em um ano
            'm': 12,         # meses em um ano
            'a': 1,          # anos
        }
        if len(tempo_de_rendimento) < 2: #Verifica se a unidade de tempo fornecida tenha pelo menos dois caracteres
            print("Unidade de tempo não suportada.")
            
        tempo_de_rendimento = tempo_de_rendimento.lower() # Tranformamos a string tempo fornecida para minúsculas para não ocorrer problema caso o usuário forneca com maiúsculas
        
        unidade_de_tempo_escolhida = tempo_de_rendimento[-3:] if tempo_de_rendimento[-3:] == 'min' else tempo_de_rendimento[-1] #Verifica qual unidade de tempo fornecida, utiliza :-3 como padrão caso o usuário forneca o tempo em minutos, se o resultado nao for 'min', pegamos a ultima letra para usar como unidade de tempo
        if unidade_de_tempo_escolhida not in unidades_de_tempo:                                                                                           
            print("Unidade de tempo não suportada.")
        if unidade_de_tempo_escolhida == 'min': #Caso a unidade de tempo fornecida for em 'min', fazemos o casting da do tempo fornecido para int excluindo as ultimas 3 letras e dividimos unidade de tempo correspondente
            tempo_fracionado = int(tempo_de_rendimento[:-3]) / unidades_de_tempo['min']
        else:
            tempo_fracionado = int(tempo_de_rendimento[:-1]) / unidades_de_tempo[unidade_de_tempo_escolhida] #Se a unidade de tempo não for 'min', excluímos a ultima letra da string tempo fornecida e divimos pela unidade de tempo correspondente

        # Cálculo do saldo com rendimento
        return self._saldo * (1 + self.taxa_de_rendimento/100) ** tempo_fracionado
    