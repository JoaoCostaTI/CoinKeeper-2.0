import sqlite3 as lite

#Criando a conexão com o Banco
conexao = lite.connect('dados.db')

#Criando tabela de categoria
with conexao:
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categoria (
                   id integer primary key autoincrement,
                   nome text
                   )
''')

#Criando tabela de receitas
with conexao:
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS receitas (
                   id integer primary key autoincrement,
                   categoria text,
                   adicionado_em DATE,
                   valor decimal
                   )
''')
    
#Criando tabela de gastos
with conexao:
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
                   id integer primary key autoincrement,
                   categoria text,
                   retirado_em date,
                    valor decimal
                   )
''')