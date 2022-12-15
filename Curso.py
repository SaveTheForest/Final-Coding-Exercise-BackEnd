from conexaoDB import *

class Curso:
    def __init__(self, codigo, nome, duracao):
        self.codigo = codigo
        self.nome = nome
        self.duracao = duracao


    def cadastrar(self):
        c = ConexaoDB()
        sql = f"insert into curso (codigo, nome, duracao)"
        sql += f"values ('{self.codigo}','{self.nome}','{self.duracao}')"
        c.executarDML(sql)

    def alterar(nome, codigo):
        c = ConexaoDB()
        sql = f"update curso "
        sql += f"set nome ='{nome}' where codigo='{codigo}'"
        c.executarDML(sql)

    def excluir(codigo):
        c = ConexaoDB()
        sql = f"delete from curso where codigo='{codigo}'"
        c.executarDML(sql)

    def consultar(self):
        objetoBD = ConexaoDB()



