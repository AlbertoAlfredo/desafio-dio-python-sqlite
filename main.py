from dbrelacional import session, Cliente, Conta
from sqlalchemy import select

clientes = session.query(Cliente).all()

contas = session.query(Conta).all()

print("""
Lista de Clientes
_______________________________________________________
""")

for cliente in clientes:
    print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, endereço: {cliente.endereco}")
    
print("""
_______________________________________________________

Lista de Contas
_______________________________________________________
""")

for conta in contas:
    print("""
Dono da conta: {}
Ag: {}
Número: {}
Tipo de conta: {}
Saldo: {:.2f}
""".format(session.query(Cliente.nome).filter_by(id=conta.id_cliente).first(), conta.agencia, conta.num, conta.tipo, conta.saldo))