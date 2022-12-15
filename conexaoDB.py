import mysql.connector

class ConexaoDB():
    def __init__(self, host="localhost", user="root", password="", database = "bd"):
        self.host = host
        self.user = user
        self.password = password
        self.db = database

    def conectar(self):
        self.con = mysql.connector.connect(host = self.host,
                                           user = self.user,
                                           password = self.password,
                                           database = self.db)
        self.cur = self.con.cursor()

    def desconectar(self):
        self.con.close()

    def executarDQL(self, sql):
        self.conectar()
        self.cur.execute(sql)
        resultado = self.cur.fetchall() #retornar todas as linhas
        self.desconectar()
        return print(resultado)

    def executarDML(self, sql):
        self.conectar()
        self.cur.execute(sql)
        self.con.commit() #confirmar alteracao
        self.desconectar()