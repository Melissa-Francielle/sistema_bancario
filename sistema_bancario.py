
import sys
menu = f"""
    Informe a operação que gostaria de operar:
                
                1 - Deposito 
                2- Saque
                3 - Ver Extrato
                4 - Sair 

    """
print(menu)
op = int(input("Informe aqui:"))
deposito = 0.0
saque = 0
contando_saque = 0
saldo = 20.00
armazenando_saldo = -1
armazenando_deposito = 0
armazenando_saque = 0
LIMIT_TOTAL = 500.00
extrato = ""

while op != 4:
    if op == 1:
        contando_deposito = 0
        intro = f'''
                    AVISO
            Se o deposito for igual a 0 
            Sairá da operação de deposito

        '''
        deposito = float(input("\nInforme quanto gostaria de depositar: "))
        
        if deposito < 0:
            print("\nNão é possivel realizar depositos negativos\n")
            print("Tente Novamente")
            deposito = float(input("\nInforme quanto gostaria de depositar: "))

        elif deposito == 0:
            print(menu)
            op = int(input("Informe aqui a ação que gostaria de fazer agora: "))
        else:        
            saldo += deposito 
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print("\nDeposito realizado com sucesso!")

    if op == 2:    
        limite = 500.00
        if contando_saque != 3:
            intro = f'''
                        AVISO
                Se o saque for igual a 0
                Sairá da operação de saque

            '''
            print(intro)
            saque = float(input("Informe a quantia que gostaria de retirar: "))
            if saque > LIMIT_TOTAL:
                print("\nexecedido o limite de saque")
                print(menu)
                op = int(input("\nInforme aqui a ação que gostaria de fazer agora: "))
            
            if saque == 0:
                print("\nSaiu")
                print(menu)
                op = int(input("\nInforme aqui a ação que gostaria de fazer agora: "))
            elif saque > 0:
                contando_saque  += 1
                saldo -= saque
                if saldo <= 0:
                    print("\nSaldo zerado")
                    print(menu)
                    op = int(input("\nInforme aqui a ação que gostaria de fazer agora: "))
                else:
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    print("\nSaque realizado com sucesso")
        else: 
            print("Execedeu a quantidade dos saques")
            print(menu)
            op = int(input("\nInforme aqui a ação que gostaria de fazer agora: "))
    
    if op == 3:
        mensagem = f"""
            ##############################################################
                                    EXTRATO 
                Horário: **:**                  Data: **/**/****
                Local: ********* ***********

                Conta: ************-07
                Nome: **** ****** *** ****

        """
        print(mensagem)
        print("Não houveram movimentações nessa conta" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("#################################################################")

        print("\nExtrato impresso.")
        print(menu)
        op = int(input("\nInforme a proxima ação: "))
        
    if op == 4:
        saida = f"""
        Obrigado por confiar seus dados 
        a nós e confiar em nossos serviços
                Volte sempre!

        """
        print(saida)
        sys.exit()