import sqlite3

class BancoDeDados:
    def __init__(self, nome_banco):
        self.banco = nome_banco
        self.conexao = None
    
    def conectar(self):
        self.conexao = sqlite3.connect(self.banco)
    
    def desconectar(self):
        if self.conexao:
            self.conexao.close()
    
    def criar_tabela(self):
        self.conectar()
        cursor = self.conexao.cursor()

        cursor.execute('''
                    create table if not exists teste(
                       id integer primary key autoincrement,
                       tipo text,
                       categoria text
                       )
                    ''')
        self.conexao.commit()
        self.desconectar()

db = BancoDeDados('financas.db')
db.criar_tabela()