from entites.account import Account

class Savings_account(Account):
    def __init__(self, id: str, balance: float, annual_income_rate):
        super().__init__(id, balance)

        self.annual_income_rate = annual_income_rate / 100  # converter para decimal

    def calculate_interest(self, time, unit_of_time):#Simulador de investimentos/rendimentos
        try:
            unit_of_time = str(
                input("Escolha sua unidade de tempo : anos , meses , dias , horas , minutos , segundos : "))
            time = int(input('digite quanto tempo voce deseja : '))
            time_in_years_conversion = {
                "anos": time,
                "meses": time / 12,
                "dias": time / 365,
                "horas": time / (365 * 24),
                "minutos": time / (365 * 24 * 60),
                "segundos": time / (365 * 24 * 60 * 60)
            }

            if unit_of_time not in time_in_years_conversion:
                return print("Opção Invalida")

            time_in_years = time_in_years_conversion[unit_of_time]

            rate_of_interest = (
                1 + self.annual_income_rate) ** time_in_years - 1

            total = self.balance * rate_of_interest
            print("\n-=-=-=-=-=-=-=-=-=-")
            print(f" Baseado na taxa de Rendimento do nosso banco que atualmente esta em {self.annual_income_rate * 100}% ao Ano, O Seu Rendimento Aplicado em {unit_of_time}: totaliza R${total:.2f}")
            print("-=-=-=-=-=-=-=-=-=-")
        except ValueError:
            print("\nEntrada inválida. Certifique-se de que a entrada de tempo seja um número inteiro.")
        return

    def deposit(self, value: float): #depositar vanila
        self.balance += value

    def withdraw(self, value: float): #sacar vanila
        # Verifica se o valor do saque é maior do que o saldo da conta
        if value > self.balance:
            return print("\nNão há saldo disponivel para esse valor.")

        # Realiza o saque apenas com o saldo da conta
        self.balance -= value
        print("\nSaque realizado com sucesso.")
