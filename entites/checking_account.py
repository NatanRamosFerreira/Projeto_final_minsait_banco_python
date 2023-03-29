from .account import Account

class checking_account(Account):
    def __init__(self, id: str, balance: float, credit_limit: float):
        super().__init__(id, balance)
        self.credit_limit = credit_limit

    def deposit(self, value: float): #depositar vanila
        self.balance += value
        
    def withdraw(self, value: float): #sacar vanila
        # Verifica se o valor do saque é maior do que o saldo da conta
        if value > self.balance:
            return print(" \nO valor utrapassa o saldo disponivel")

        # Realiza o saque apenas com o saldo da conta
        self.balance -= value
        print("\nSaque realizado com sucesso.")

    def withdraw_from_special_check(self, value: float): #saque com a utilização do cheque especial/limite de credito
        try:
            # Verifica se o valor do saque é maior do que o saldo da conta
            if value > self.balance:
                    limit_used = value - self.balance
                    if limit_used > self.credit_limit:
                        raise ValueError("\nLimite de crédito insuficiente")
                    else:
                        # Realiza o saque com o limite de crédito e bloqueia o limite
                        self.balance = 0
                        self.credit_limit -= limit_used
                        print("\nSaque realizado com sucesso.")
            else:
                print("\nOperação cancelada.")
        except ValueError:
            print("Erro:")
