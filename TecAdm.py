from conexaoDB import *
from Funcionario import Funcionario
class TecAdm(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.salario = salario

    def cadastrar(self):
        c = ConexaoDB()
        sql = f"insert into tecadm (nome, endereco, telefone, cpf, salario)"
        sql += f"values ('{self.nome}','{self.endereco}','{self.telefone}','{self.cpf}','{self.salario}')"
        c.executarDML(sql)

    def alterar(nome, cpf):
        c = ConexaoDB()
        sql = f"update tecadm "
        sql += f"set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(sql)

    def excluir(cpf):
        c = ConexaoDB()
        sql = f"delete from tecadm where cpf='{cpf}'"
        c.executarDML(sql)

    def consultar(self):
        objetoBD = ConexaoDB()



