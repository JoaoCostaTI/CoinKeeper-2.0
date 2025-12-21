import sqlite3

conexao = sqlite3.connect('dados.db')

###############################################################
#Funções de INSERÇÃO
#inserir categorias 
def inserir_categoria(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'INSERT INTO categoria (nome) VALUES(?)'
        cursor.execute(query, i)

#inserir receita 
def inserir_receitas(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'INSERT INTO receitas (categoria, adicionado_em, valor) VALUES(?,?,?)'
        cursor.execute(query, i)

#inserir gastos 
def inserir_gastos(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'INSERT INTO gastos (categoria, retirado_em, valor) VALUES(?,?,?)'
        cursor.execute(query, i)

###############################################################
#Funções de Exclusão
#Deletar Receitas
def deletar_receitas(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'DELETE from receitas WHERE id = ?'
        cursor.execute(query, i)

#Deletar gastos
def deletar_gastos(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'DELETE from gastos WHERE id = ?'
        cursor.execute(query, i)

###############################################################
#Funções para exibir dados
#Ver categorias
def ver_categoria():
    lista_itens = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM  categoria')
        linha = cursor.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

#Ver receitas
def ver_receitas():
    lista_itens = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM  receitas')
        linha = cursor.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

#Ver Gastos
def ver_gastos():
    lista_itens = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM  gastos')
        linha = cursor.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

