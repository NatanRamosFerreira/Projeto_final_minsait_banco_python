from entites.checking_account import checking_account
from entites.savings_account import Savings_account


conta_corrente = checking_account("133222-1", 5000.00, 1000.00)
conta_poupanca = Savings_account("133222-14", 10000.00, 10)

def status_checking_accont():#mostrar status da conta corrente
    print("\n-=-=-=-=-=-=-=-=-=-")
    print("Conta Corrente: ",conta_corrente.id )
    print("Saldo Atual: " , conta_corrente.balance)
    print("Limite de Credito: ", conta_corrente.credit_limit)
    print("-=-=-=-=-=-=-=-=-=-")   

def status_savings_accont():#mostrar status da conta poupança
    print("\n-=-=-=-=-=-=-=-=-=-")
    print("Conta Poupança: ",conta_poupanca.id )
    print("Saldo Atual: " , conta_poupanca.balance)
    print("-=-=-=-=-=-=-=-=-=-")   
    
def interaction_checking_account(): #interação só se a conta for corrente

        while True:
            status_checking_accont()
            print("\nSelecione uma opção:")
            print("1 - Sacar")
            print("2 - Depositar")
            print("3 - Saque com limite de credito")
            print("4 - Voltar")

            try:
                option = int(input("Digite o número da opção desejada: "))

                if option == 1:
                    valor_saque = float(input("Digite o valor que deseja sacar: "))
                    conta_atual.withdraw(valor_saque)

                elif option == 2:
                    valor_deposito = float(input("Digite o valor que deseja depositar: "))
                    conta_atual.deposit(valor_deposito)
                    print(f"\nDepósito de R$ {valor_deposito:.2f} efetuado com sucesso.")

                elif option == 3:
                    valor_saque = float(input("Digite o valor que deseja sacar: "))
                    conta_atual.withdraw_from_special_check(valor_saque)
                    print("\nsaque realizado com sucesso, Obrigado por usar os nossos serviços")
    
                elif option == 4:
                    break

                else:
                    print("\nOpção inválida. Por favor, selecione uma opção válida.")

            except ValueError:
                print("\nOpção inválida. Por favor, selecione uma opção válida.")

def interaction_savings_account(): #interação só se a conta for poupança
        while True:
                status_savings_accont()
                print("\nSelecione uma opção:")
                print("1 - Sacar")
                print("2 - Depositar")
                print("3 - Simular Investimento")
                print("4 - Voltar")

                try:
                    option = int(input("Digite o número da opção desejada: "))

                    if option == 1:
                        valor_saque = float(input("Digite o valor que deseja sacar: "))
                        conta_atual.withdraw(valor_saque)

                    elif option == 2:
                        valor_deposito = float(input("Digite o valor que deseja depositar: "))
                        conta_atual.deposit(valor_deposito)
                        print(f"\nDepósito de R$ {valor_deposito:.2f} efetuado com sucesso.")

                    elif option == 3 and conta_atual == conta_poupanca:
                        conta_atual.calculate_interest(0, 0)

                    elif option == 4:
                        break

                    else:
                        print("\nOpção inválida. Por favor, selecione uma opção válida.")
                        

                except ValueError:
                    print("\nOpção inválida. Por favor, selecione uma opção válida.")
        
while True:#interação Vanila
    print("\n-=-=-=-=-=-=-=-=-=- Banco Lisos Venceremos -=-=-=-=-=-=-=-=-=-=")
    print("Selecione uma opção:")
    print("1 - Conta Corrente")
    print("2 - Poupança")
    print("3 - Sair")

    try:
        option = int(input("Digite o número da conta desejada: "))

        if option == 1:
            conta_atual = conta_corrente
            interaction_checking_account()

        elif option == 2:
            conta_atual = conta_poupanca
            interaction_savings_account()
            
        elif option == 3:
            print("\nObrigado por utilizar nossos serviços.")
            break

        else:
            print("\nOpção inválida. Por favor, selecione uma opção válida.")
            

    except ValueError:
        print("\nOpção inválida. Por favor, selecione uma opção válida.")
        
