#Forma 2

SaldoTotal=[1000]

def RetirarDinero(retiro):
    if retiro > SaldoTotal[0]:
        print("Lo siento su saldo no es suficiente, usted cuenta con:", SaldoTotal[0])
    else:
        SaldoTotal[0] -= retiro
        print("Haz retirado", retiro, "y tienes", SaldoTotal[0], "de saldo")

def DepositarDinero(deposito):
    if deposito <= 0:
        print("El monto a depositar debe ser mayor a 0")
    else:
        SaldoTotal[0] += deposito
        print("Haz depositado", deposito, "y ahora tu cuenta tiene", SaldoTotal[0])
        
def TransferirDinero(monto_a_transferir, numero_cuenta, nombre_destinatario,dni_destinatario):
    if monto_a_transferir > SaldoTotal[0] and SaldoTotal[0] > 0:
        print("Lo siento su saldo no es suficiente, usted cuenta con:", SaldoTotal[0])
    elif len(numero_cuenta) != 16:
        print("El numero de cuenta debe tener 16 digitos")
    elif len(dni_destinatario) != 8:
        print("El DNI debe tener 8 digitos")
    else:
        SaldoTotal[0] -= monto_a_transferir
        print("Haz transferido", monto_a_transferir, "a la cuenta", numero_cuenta, "a nombre de", nombre_destinatario)
        print("Te queda", SaldoTotal[0], "de saldo")

def MostrarSaldo():
    print("Su saldo es:",SaldoTotal[0])
    return SaldoTotal[0]
    

def CajeroAutomatico():
    print("\a\n=====BIENENIDO AL CAJERO AUTOMATICO======")
    print("[1]. Retirar dinero")
    print("[2]. Depositar dinero")
    print("[3]. Tranferir dinero")
    print("[4]. Mostrar saldo")
    print("[5]. Salir")

    op=int(input("Que desea realizar,estimado cliente:"))
    if op==1:
        retiro = float(input("Ingrese el monto a retirar:"))
        RetirarDinero(retiro)
    if op==2:
        deposito = float(input("Ingrese el monto a depositar:"))
        DepositarDinero(deposito)
    if op==3:
        monto_a_transferir = float(input("Ingrese el monto a transferir:"))
        numero_cuenta = input("Ingrese el numero de cuenta del destinatario:")
        nombre_destinatario = input("Ingrese el nombre del destinatario:")
        dni_destinatario = input("Ingrese el DNI del destinatario:")
        TransferirDinero(monto_a_transferir, numero_cuenta, nombre_destinatario, dni_destinatario)
    if op==4:
        MostrarSaldo()

    if op==5:
        print("\nGracias por el usar el cajero automatico")

while True:
    CajeroAutomatico()
    continuar=input("\nDeseas continuar con el cajero automatico(S/N):").lower()
    if continuar != "s":
        break