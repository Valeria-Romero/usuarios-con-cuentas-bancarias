class CuentaBancaria:
    
    cuentas = []
    
    def __init__(self):
        self.balance = 0
        self.interes = 0.3
        CuentaBancaria.cuentas.append(self)
    
    def deposito(self, cantidad):
        self.balance += cantidad
        return self
    
    def retiro(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes, cobrando una multa de $5")
            self.balance -= 5
        return self
    
    