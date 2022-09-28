from Usuario import Usuario

Maria = Usuario("Maria")
Laura = Usuario("Laura")

Maria.hacer_deposito(500).hacer_retiro(100)
Laura.hacer_retiro(100)

Maria.hacer_transferencia(250,Laura)