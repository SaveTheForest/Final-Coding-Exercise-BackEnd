from Funcionario import Funcionario
from conexaoDB import ConexaoDB

class Professor(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, salario, titulacao, formacao):
        super().__init__(nome, endereco, telefone, cpf, salario)
        self.titulacao = titulacao
        self.formacao = formacao
    def cadastrar(self):
        c = ConexaoDB()
        sql = f"insert into professor (nome, endereco, telefone, cpf, salario, titulacao, formacao)"
        sql += f"values ('{self.nome}','{self.endereco}','{self.telefone}','{self.cpf}','{self.salario}','{self.titulacao}','{self.formacao}')"
        c.executarDML(sql)

    def alterar(nome, cpf):
        c = ConexaoDB()
        sql = f"update professor "
        sql += f"set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(sql)

    def excluir(cpf):
        c = ConexaoDB()
        sql = f"delete from professor where cpf='{cpf}'"
        c.executarDML(sql)

    def consultar(self):
        objetoBD = ConexaoDB()



