


import pyodbc
from datetime import datetime

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-P9HRRQK;"
    "Database=PythonSQL"
)

conexao = pyodbc.connect(dados_conexao)

print("Conexão feita com sucesso!")

cursor = conexao.cursor()

#data_atual = datetime.today()
#data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

cliente = "Edu"
produto = "óculos"
#data = data_em_texto
preco = "300"
quantidade = 1

'''
comando = """
INSERT INTO tblVendas(Cliente, Produto, Data_Venda, Preco, Quantidade)
VALUES('Alice', 'Tablet', GETDATE(), 800, 2)
"""
'''

comando = f"""
INSERT INTO tblVendas(Cliente, Produto, Data_Venda, Preco, Quantidade)
VALUES('{cliente}', '{produto}', GETDATE(), {preco}, {quantidade})
"""


cursor.execute(comando)
cursor.commit()
