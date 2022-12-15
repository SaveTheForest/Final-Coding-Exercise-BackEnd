from conexaoDB import *


class Aluno:
    def __init__(self, nome, matricula, cpf, curso):
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.curso = curso

    def cadastrar(self):
        c = ConexaoDB()
        sql = f"insert into aluno (nome,matricula,cpf,curso)"
        sql += f"values ('{self.nome}','{self.matricula}','{self.cpf}','{self.curso}')"
        c.executarDML(sql)


    def alterar(nome, cpf):
        c = ConexaoDB()
        sql = f"update aluno "
        sql += f"set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(sql)

    def excluir(cpf):
        c = ConexaoDB()
        sql = f"delete from aluno where cpf='{cpf}'"
        c.executarDML(sql)

    def consultar(self):
        objetoBD = ConexaoDB()
