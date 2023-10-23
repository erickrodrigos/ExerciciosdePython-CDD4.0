from Biblioteca import *

conta = ContaBancaria(1900.78, 10.50, "ERICK", "Corrente", 5000)

conta.VerificarSaldo()
conta.Depositar(100)
conta.VerificarSaldo()
conta.Sacar(600)
conta.VerificarSaldo()
conta.Sacar(600)
conta.Ativarconta(True)
conta.VerificarSaldo()
conta.Emprestimo(6000)
conta.Sacar(600)
conta.VerificarSaldo()
conta.SolicitarLimite(10000)