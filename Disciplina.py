from conexaoDB import *



class Disciplina:
    def __init__(self, codigo, nome, cargahoraria):
        self.codigo = codigo
        self.nome = nome
        self.cargahoraria = cargahoraria


    def cadastrar(self):
        c = ConexaoDB()
        sql = f"insert into disciplina (codigo, nome, cargahoraria)"
        sql += f"values ('{self.codigo}','{self.nome}','{self.cargahoraria}')"
        c.executarDML(sql)

    def alterar(nome, codigo):
        c = ConexaoDB()
        sql = f"update disciplina "
        sql += f"set nome ='{nome}' where codigo='{codigo}'"
        c.executarDML(sql)

    def excluir(codigo):
        c = ConexaoDB()
        sql = f"delete from disciplina where codigo='{codigo}'"
        c.executarDML(sql)

    def consultar(self):
        objetoBD = ConexaoDB()





