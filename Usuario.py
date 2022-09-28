from CuentaBancaria import CuentaBancaria

class Usuario:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = CuentaBancaria()
        
    
    def hacer_deposito(self, cantidad):
        self.cuenta.deposito(cantidad)
        self.mostrar_info()
        return self

    def hacer_retiro(self, cantidad):
        self.cuenta.retiro(cantidad)
        self.mostrar_info()
        return self
    
    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Balance: {self.cuenta.balance}")

    def hacer_transferencia(self, cantidad, otro_usuario):
        self.cuenta.retiro(cantidad)
        otro_usuario.cuenta.deposito(cantidad)
        self.mostrar_info()
        otro_usuario.mostrar_info()
        return self