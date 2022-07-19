#pip install pyodbc
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-P9HRRQK;"
    "Database=PythonSQL"
)

# criano uma conexão
conexao = pyodbc.connect(dados_conexao)

print("Conexão feita com sucesso!")

#Criando um cursor
cursor = conexao.cursor()

def insert():
    comando = """
        INSERT INTO tblVendas(Cliente, Produto, Data_Venda, Preco, Quantidade)
        VALUES('Teste', 'Tablet', GETDATE(), 500, 2)
        """
    cursor.execute(comando)
    cursor.commit()
    cursor.close()


insert()