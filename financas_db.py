import sqlite3

from datetime import date, datetime

# 1. FUNÇÕES AUXILIARES (Ficam SOLTAS, fora da classe)

def adaptar_data(minha_data):
    # Essa função recebe um objeto 'date' e deve retornar uma STRING (texto)
    # Dica: use o método .isoformat() da data
    return minha_data.isoformat() 

def converter_data(dado_em_bytes):
    # Essa função recebe bytes do banco e deve retornar um objeto 'date'
    # Dica: use o datetime.strptime(dado_em_bytes.decode('utf-8'), '%Y-%m-%d').date()
    # Copie a lógica que usamos no exercício anterior aqui:
    return datetime.strptime(dado_em_bytes.decode('utf-8'), '%Y-%m-%d').date()

# 2. REGISTRO (Avisar o SQLite que essas funções existem)
sqlite3.register_adapter(date, adaptar_data)
sqlite3.register_converter("DATE", converter_data)

class BancoDeDados:
    def __init__(self, nome_banco):
        self.banco = nome_banco
        self.conexao = None
    
    def conectar(self):
        self.conexao = sqlite3.connect(self.banco)
    
    def desconectar(self):
        if self.conexao:
            self.conexao.close()
    
    def adaptar_data(self):
        pass

    def converter_data(self):
        pass

