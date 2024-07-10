from dbrelacional import Cliente, Conta, session

cliente1 = Cliente(id=1, nome='Gustavo', cpf=11111111111, endereco='Rua dos bobos, numero 0')
cliente2 = Cliente(id=2, nome='Guanabara', cpf=22222222222, endereco='Rua dos bobos, numero 0')
cliente3 = Cliente(id=3, nome='Guri', cpf=33333333333, endereco='Rua dos bobos, numero 0')

conta1 = Conta(tipo='corrente', agencia='0001', num=123321123, id_cliente=1, saldo=127.5)
conta2 = Conta(tipo='poupanca', agencia='0001', num=123321123, id_cliente=1, saldo=0)
conta3 = Conta(tipo='corrente', agencia='0001', num=321321321, id_cliente=2, saldo=1)
conta4 = Conta(tipo='poupanca', agencia='0001', num=321321321, id_cliente=2, saldo=12000)
conta5 = Conta(tipo='corrente', agencia='0001', num=123123123, id_cliente=3, saldo=1200)
conta6 = Conta(tipo='poupanca', agencia='0001', num=123123123, id_cliente=3, saldo=400)


session.add(cliente1)
session.add(cliente2)
session.add(cliente3)
session.add(conta1)
session.add(conta2)
session.add(conta3)
session.add(conta4)
session.add(conta5)
session.add(conta6)


session.commit()