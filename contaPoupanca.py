from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, conta_id: int, saldo: float, taxa_de_rendimento: float) -> None:
        super().__init__(conta_id, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento

    def depositar(self, valor_a_ser_depositado):
        self._saldo += valor_a_ser_depositado

    def sacar(self, valor_a_ser_sacado):
        self._saldo - + valor_a_ser_sacado


    def verificar_rendimento_ao_ano(self, tempo):
        time_units = {
            's': 31536000,   # segundos em um ano
            'min': 525600,   # minutos em um ano
            'h': 8760,       # horas em um ano
            'd': 365,        # dias em um ano
            'w': 52,         # semanas em um ano
            'm': 12,         # meses em um ano
            'a': 1,          # anos
        }
        time_unit = tempo[-1]
        if time_unit not in time_units:
            print("Unidade de tempo não suportada.")
            return
        time_frac = int(tempo[:-1]) / time_units[time_unit]

        # Cálculo do saldo com rendimento
        saldo_rendimento = self._saldo * (1 + self.taxa_de_rendimento/100) ** time_frac
        return saldo_rendimento
