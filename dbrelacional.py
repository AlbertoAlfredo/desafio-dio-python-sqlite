from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine

# conexão com banco de dados
# engine = create_engine("sqlite:///banco.db", echo=True)
engine = create_engine("sqlite:///banco.db")

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(length=11))
    endereco = Column(String)
    
class Conta(Base):
    
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Float)


# cria classes como tabela no banco de dados
Base.metadata.create_all(engine)   

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()

    
